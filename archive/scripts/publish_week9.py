#!/usr/bin/env python3
"""Publish Week 9 IPv6 student resource pages to Canvas."""

import os
import json
import requests
from pathlib import Path

# Canvas API configuration
CANVAS_API_URL = os.getenv('CANVAS_API_URL', 'https://neumont.instructure.com/api/v1')
CANVAS_API_TOKEN = os.getenv('CANVAS_API_TOKEN', '')
COURSE_ID = '3646987'  # ITH216 Networking II
TIMEOUT = 120

# Week 9 pages mapping
PAGES = {
    '40329310': {
        'title': 'Week 9 | Page 1 - IPv6 Fundamentals and Static Routing',
        'html_file': 'C:\\Users\\cburk\\AppData\\Local\\Temp\\claude\\D--GitHub-Repos-Canvas-Course-Updater\\c0df45c2-8bef-44b9-b91f-8ccd2afa994e\\scratchpad\\week9_page1_expanded.html',
        'description': 'IPv6 addressing, static routing configuration, and dual-stack enterprise networks'
    },
    '40329311': {
        'title': 'Week 9 | Page 2 - IPv6 EIGRP Dynamic Routing',
        'html_file': 'C:\\Users\\cburk\\AppData\\Local\\Temp\\claude\\D--GitHub-Repos-Canvas-Course-Updater\\c0df45c2-8bef-44b9-b91f-8ccd2afa994e\\scratchpad\\week9_page2_expanded.html',
        'description': 'EIGRP for IPv6, neighbor formation, convergence, and advanced deployment'
    }
}

def read_html(filepath):
    """Read HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"ERROR reading {filepath}: {e}")
        return None

def publish_page(page_id, title, html_content):
    """Publish page to Canvas via REST API."""
    if not CANVAS_API_TOKEN:
        print("ERROR: CANVAS_API_TOKEN not set in environment")
        return False

    url = f"{CANVAS_API_URL}/courses/{COURSE_ID}/pages/{page_id}"
    headers = {
        'Authorization': f'Bearer {CANVAS_API_TOKEN}',
        'Content-Type': 'application/json'
    }

    payload = {
        'wiki_page': {
            'title': title,
            'body': html_content,
            'published': True
        }
    }

    try:
        print(f"\nPublishing: {title}")
        print(f"  URL: {url}")
        print(f"  HTML size: {len(html_content)} bytes")

        response = requests.put(
            url,
            json=payload,
            headers=headers,
            timeout=TIMEOUT
        )

        print(f"  Status: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print(f"  ✓ Published successfully")
            print(f"  Canvas URL: https://neumont.instructure.com/courses/{COURSE_ID}/pages/{data.get('url', page_id)}")
            return True
        else:
            print(f"  ERROR: {response.status_code}")
            try:
                print(f"  Response: {response.json()}")
            except:
                print(f"  Response: {response.text[:200]}")
            return False

    except Exception as e:
        print(f"  ERROR: {e}")
        return False

def main():
    """Main publication workflow."""
    print("=" * 60)
    print("Canvas Week 9 Student Resource Pages Publisher")
    print("=" * 60)

    # Verify API token
    if not CANVAS_API_TOKEN:
        print("\nERROR: CANVAS_API_TOKEN environment variable not set")
        print("Set it before running: $env:CANVAS_API_TOKEN='your_token'")
        return False

    print(f"\nCanvas API URL: {CANVAS_API_URL}")
    print(f"Course ID: {COURSE_ID}")
    print(f"Pages to publish: {len(PAGES)}")

    # Publish each page
    results = {}
    for page_id, page_info in PAGES.items():
        html_content = read_html(page_info['html_file'])
        if not html_content:
            results[page_id] = False
            continue

        success = publish_page(page_id, page_info['title'], html_content)
        results[page_id] = success

    # Summary
    print("\n" + "=" * 60)
    print("Publication Summary")
    print("=" * 60)

    successful = sum(1 for v in results.values() if v)
    total = len(results)

    print(f"\nPublished: {successful}/{total}")

    for page_id, success in results.items():
        status = "✓ SUCCESS" if success else "✗ FAILED"
        print(f"  {PAGES[page_id]['title'][:50]}... {status}")

    return all(results.values())

if __name__ == '__main__':
    import sys
    success = main()
    sys.exit(0 if success else 1)
