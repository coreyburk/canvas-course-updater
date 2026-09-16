#!/usr/bin/env python3
"""Unpublish redundant older reference pages from Canvas."""

import os
import requests

CANVAS_API_URL = os.getenv('CANVAS_API_URL', 'https://neumont.instructure.com/api/v1')
CANVAS_API_TOKEN = os.getenv('CANVAS_API_TOKEN', '')
COURSE_ID = '3646987'  # ITH216
TIMEOUT = 120

# Pages to unpublish (superseded by comprehensive Weeks 1-10 series)
PAGES_TO_UNPUBLISH = {
    '28697934': 'Definitions: Cisco IOS',
    '28697938': 'Definitions: Point-to-Point WANS',
    '28697941': 'Notes: Implementing EIGRP for IPv4',
    '28697943': 'Notes: Troubleshooting IPv4 Routing Protocols',
    '28697944': 'Notes: Understanding EIGRP Concepts',
    '28697906': 'Basic Cisco Router Configuration Step-By-Step Commands',
    '28697907': 'Cisco CLI Switch Command Cheat Sheet',
    '28697908': 'Cisco Switch and Router Configuration Guides',
    '28697905': 'Activity: Troubleshooting Routing',
    '28697933': 'Definitions: Cisco IOS Licensing',
    '28697935': 'Definitions: EIGRP',
    '28697936': 'Definitions: Frame Relay',
    '28697937': 'Definitions: OSPF',
}

def unpublish_page(page_id, title):
    """Unpublish a page from Canvas."""
    if not CANVAS_API_TOKEN:
        print("ERROR: CANVAS_API_TOKEN not set")
        return False

    url = f"{CANVAS_API_URL}/courses/{COURSE_ID}/pages/{page_id}"
    headers = {
        'Authorization': f'Bearer {CANVAS_API_TOKEN}',
        'Content-Type': 'application/json'
    }

    payload = {
        'wiki_page': {
            'published': False
        }
    }

    try:
        print(f"  Unpublishing: {title[:50]}...")
        response = requests.put(url, json=payload, headers=headers, timeout=TIMEOUT)

        if response.status_code == 200:
            print(f"    ✅ Unpublished successfully")
            return True
        else:
            print(f"    ❌ Error {response.status_code}")
            return False
    except Exception as e:
        print(f"    ❌ Exception: {e}")
        return False

def main():
    """Main cleanup workflow."""
    print("=" * 80)
    print("ITH216 - Unpublishing Redundant Older Pages")
    print("=" * 80)

    if not CANVAS_API_TOKEN:
        print("\nERROR: CANVAS_API_TOKEN not set")
        return False

    print(f"\nCourse ID: {COURSE_ID}")
    print(f"Pages to unpublish: {len(PAGES_TO_UNPUBLISH)}\n")

    results = {}
    for page_id, title in PAGES_TO_UNPUBLISH.items():
        success = unpublish_page(page_id, title)
        results[page_id] = success

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    successful = sum(1 for v in results.values() if v)
    total = len(results)

    print(f"\nUnpublished: {successful}/{total}")

    if successful == total:
        print("\n✅ All redundant pages successfully unpublished!")
    else:
        print(f"\n⚠️ {total - successful} pages failed to unpublish")

    return successful == total

if __name__ == '__main__':
    import sys
    success = main()
    sys.exit(0 if success else 1)
