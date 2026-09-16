#!/usr/bin/env python3
"""Query Canvas for all pages in ITH216 course and analyze coverage."""

import os
import json
import requests

# Canvas API configuration
CANVAS_API_URL = os.getenv('CANVAS_API_URL', 'https://neumont.instructure.com/api/v1')
CANVAS_API_TOKEN = os.getenv('CANVAS_API_TOKEN', '')
COURSE_ID = '3646987'  # ITH216 Networking II
TIMEOUT = 120

def get_all_pages():
    """Fetch all pages from Canvas course."""
    if not CANVAS_API_TOKEN:
        print("ERROR: CANVAS_API_TOKEN not set")
        return []

    url = f"{CANVAS_API_URL}/courses/{COURSE_ID}/pages"
    headers = {
        'Authorization': f'Bearer {CANVAS_API_TOKEN}',
        'Content-Type': 'application/json'
    }

    all_pages = []
    page_num = 1

    try:
        while True:
            params = {'page': page_num, 'per_page': 100}
            response = requests.get(url, headers=headers, params=params, timeout=TIMEOUT)

            if response.status_code != 200:
                print(f"Error fetching pages (page {page_num}): {response.status_code}")
                break

            pages = response.json()
            if not pages:
                break

            all_pages.extend(pages)
            page_num += 1

            if len(pages) < 100:
                break

    except Exception as e:
        print(f"Exception: {e}")

    return all_pages

def main():
    """Main audit workflow."""
    print("=" * 80)
    print("ITH216 Canvas Pages Audit - Actual Published State")
    print("=" * 80)

    if not CANVAS_API_TOKEN:
        print("\nERROR: CANVAS_API_TOKEN not set")
        return False

    print(f"\nFetching all pages from Canvas...\n")

    pages = get_all_pages()

    if not pages:
        print("ERROR: No pages found")
        return False

    print(f"Total pages found: {len(pages)}\n")

    # Organize by week
    weeks = {i: [] for i in range(1, 11)}
    navigation = []
    older_ref = []
    unpub_stubs = []
    other = []

    for page in pages:
        title = page.get('title', 'Unknown')
        published = page.get('published', False)
        page_id = page.get('page_id', 'unknown')

        page_info = {
            'title': title,
            'published': published,
            'id': page_id
        }

        # Categorize
        found = False
        for i in range(1, 11):
            if f'Week {i}' in title:
                weeks[i].append(page_info)
                found = True
                break

        if not found:
            if title in ['Home', 'Remote Learning', 'Course Outline']:
                navigation.append(page_info)
            elif any(x in title for x in ['Definition', 'Notes:', 'Guide', 'Cisco', 'Troubleshoot']):
                older_ref.append(page_info)
            elif any(x in title for x in ['Day', 'Worksheet', 'Subnetting']):
                unpub_stubs.append(page_info)
            else:
                other.append(page_info)

    # Print by week
    print("=" * 80)
    print("PAGES BY WEEK")
    print("=" * 80)

    for week in range(1, 11):
        if weeks[week]:
            print(f"\n📅 WEEK {week}: ({len(weeks[week])} pages)")
            for page in sorted(weeks[week], key=lambda x: x['title']):
                status = "✅" if page['published'] else "⏸️"
                print(f"  {status} [{page['id']:10}] {page['title']}")
        else:
            print(f"\n📅 WEEK {week}: ❌ NO PAGES")

    # Navigation
    if navigation:
        print("\n" + "=" * 80)
        print("NAVIGATION/COURSE PAGES")
        print("=" * 80)
        for page in sorted(navigation, key=lambda x: x['title']):
            status = "✅" if page['published'] else "⏸️"
            print(f"  {status} [{page['id']:10}] {page['title']}")

    # Older reference
    if older_ref:
        print("\n" + "=" * 80)
        print("OLDER REFERENCE PAGES (Pre-comprehensive series)")
        print("=" * 80)
        for page in sorted(older_ref, key=lambda x: x['title']):
            status = "✅" if page['published'] else "⏸️"
            print(f"  {status} [{page['id']:10}] {page['title']}")

    # Unpublished stubs
    if unpub_stubs:
        print("\n" + "=" * 80)
        print(f"UNPUBLISHED STUBS ({len(unpub_stubs)} pages)")
        print("=" * 80)
        for page in sorted(unpub_stubs, key=lambda x: x['title'])[:15]:
            status = "✅" if page['published'] else "⏸️"
            print(f"  {status} [{page['id']:10}] {page['title']}")
        if len(unpub_stubs) > 15:
            print(f"  ... and {len(unpub_stubs) - 15} more")

    # Other
    if other:
        print("\n" + "=" * 80)
        print(f"OTHER PAGES ({len(other)} pages)")
        print("=" * 80)
        for page in sorted(other, key=lambda x: x['title']):
            status = "✅" if page['published'] else "⏸️"
            print(f"  {status} [{page['id']:10}] {page['title']}")

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY & ANALYSIS")
    print("=" * 80)

    pub_count = sum(1 for p in pages if p.get('published'))
    unpub_count = sum(1 for p in pages if not p.get('published'))

    print(f"\nTotal: {len(pages)} pages | Published: {pub_count} | Unpublished: {unpub_count}")

    print("\nWeek Coverage (Published Pages):")
    for week in range(1, 11):
        pub = sum(1 for p in weeks[week] if p['published'])
        total = len(weeks[week])
        if total > 0:
            status = "✅" if pub >= 2 else "⚠️ " if pub > 0 else "❌"
            print(f"  {status} Week {week:2d}: {pub}/{total}")
        else:
            print(f"  ❌ Week {week:2d}: 0/0 (NO PAGES)")

    # Canvas IDs for documentation
    print("\n" + "=" * 80)
    print("CANVAS IDS FOR ITH216.md DOCUMENTATION")
    print("=" * 80)

    for week in range(1, 11):
        pub_pages = [p for p in weeks[week] if p['published']]
        if pub_pages:
            ids = ', '.join(str(p['id']) for p in sorted(pub_pages, key=lambda x: x['title']))
            print(f"Week {week}: {ids}")

    print("\n" + "=" * 80)
    print("FINDINGS")
    print("=" * 80)

    # Check for gaps
    missing_weeks = [w for w in range(1, 11) if len(weeks[w]) == 0]
    incomplete_weeks = [w for w in range(1, 11) if 0 < len(weeks[w]) < 2]

    if missing_weeks:
        print(f"\n❌ MISSING: Weeks {missing_weeks} have NO student resource pages")

    if incomplete_weeks:
        print(f"\n⚠️  INCOMPLETE: Weeks {incomplete_weeks} have only 1 page (typically need 2-3)")

    if older_ref:
        print(f"\n🔴 REDUNDANT: {len(older_ref)} older reference pages should be retired")
        print("   - These are superseded by comprehensive Week 1-10 pages")

    return True

if __name__ == '__main__':
    import sys
    success = main()
    sys.exit(0 if success else 1)
