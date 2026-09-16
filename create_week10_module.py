#!/usr/bin/env python3
"""Create Week 10 module and add BGP pages to it."""

import os
import requests

CANVAS_API_URL = os.getenv('CANVAS_API_URL', 'https://neumont.instructure.com/api/v1')
CANVAS_API_TOKEN = os.getenv('CANVAS_API_TOKEN', '')
COURSE_ID = '3646987'
TIMEOUT = 120

WEEK10_PAGE_IDS = {
    '28707125': 'Week 10 | Page 1 - BGP Fundamentals and Configuration',
    '28707126': 'Week 10 | Page 2 - BGP Advanced Topics and Route Manipulation'
}

def create_module(name, position):
    """Create a new module in Canvas."""
    if not CANVAS_API_TOKEN:
        print("ERROR: CANVAS_API_TOKEN not set")
        return None

    url = f"{CANVAS_API_URL}/courses/{COURSE_ID}/modules"
    headers = {
        'Authorization': f'Bearer {CANVAS_API_TOKEN}',
        'Content-Type': 'application/json'
    }

    payload = {
        'module': {
            'name': name,
            'position': position
        }
    }

    try:
        print(f"Creating module: {name} (position {position})...")
        response = requests.post(url, json=payload, headers=headers, timeout=TIMEOUT)

        if response.status_code == 201:
            module = response.json()
            print(f"  ✅ Module created with ID: {module.get('id')}")
            return module
        else:
            print(f"  ❌ Error {response.status_code}: {response.text[:200]}")
            return None
    except Exception as e:
        print(f"  ❌ Exception: {e}")
        return None

def add_page_to_module(module_id, page_id, title, position):
    """Add a page to a module."""
    if not CANVAS_API_TOKEN:
        return False

    url = f"{CANVAS_API_URL}/courses/{COURSE_ID}/modules/{module_id}/items"
    headers = {
        'Authorization': f'Bearer {CANVAS_API_TOKEN}',
        'Content-Type': 'application/json'
    }

    payload = {
        'module_item': {
            'type': 'Page',
            'content_id': page_id,
            'position': position
        }
    }

    try:
        print(f"  Adding page to module: {title}...")
        response = requests.post(url, json=payload, headers=headers, timeout=TIMEOUT)

        if response.status_code == 201:
            item = response.json()
            print(f"    ✅ Page added with item ID: {item.get('id')}")
            return True
        else:
            print(f"    ❌ Error {response.status_code}")
            return False
    except Exception as e:
        print(f"    ❌ Exception: {e}")
        return False

def main():
    """Main workflow."""
    print("=" * 80)
    print("Create Week 10 Module and Add BGP Pages")
    print("=" * 80)
    print()

    # Create Week 10 module at position 10
    module = create_module('Week 10', 10)

    if not module:
        print("\n❌ Failed to create Week 10 module")
        return False

    module_id = module.get('id')

    # Add pages to module
    print(f"\nAdding {len(WEEK10_PAGE_IDS)} pages to Week 10 module:\n")

    position = 1
    results = {}

    for page_id, title in WEEK10_PAGE_IDS.items():
        success = add_page_to_module(module_id, page_id, title, position)
        results[page_id] = success
        position += 1

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    successful = sum(1 for v in results.values() if v)
    total = len(results)

    print(f"\nModule Created: Week 10 (ID: {module_id})")
    print(f"Pages Added: {successful}/{total}")

    if successful == total:
        print("\n✅ Week 10 module successfully created and configured!")
        return True
    else:
        print(f"\n⚠️ {total - successful} pages failed to add")
        return False

if __name__ == '__main__':
    import sys
    success = main()
    sys.exit(0 if success else 1)
