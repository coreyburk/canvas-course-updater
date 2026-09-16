#!/usr/bin/env python3
"""Check and fix Week 10 page placement in modules."""

import os
import requests

CANVAS_API_URL = os.getenv('CANVAS_API_URL', 'https://neumont.instructure.com/api/v1')
CANVAS_API_TOKEN = os.getenv('CANVAS_API_TOKEN', '')
COURSE_ID = '3646987'
TIMEOUT = 120

WEEK10_PAGE_IDS = ['28707125', '28707126']

def get_modules():
    """Fetch all modules in course."""
    if not CANVAS_API_TOKEN:
        return []

    url = f"{CANVAS_API_URL}/courses/{COURSE_ID}/modules"
    headers = {'Authorization': f'Bearer {CANVAS_API_TOKEN}'}

    try:
        response = requests.get(url, headers=headers, timeout=TIMEOUT)
        return response.json() if response.status_code == 200 else []
    except Exception as e:
        print(f"Error fetching modules: {e}")
        return []

def get_module_items(module_id):
    """Fetch items in a module."""
    if not CANVAS_API_TOKEN:
        return []

    url = f"{CANVAS_API_URL}/courses/{COURSE_ID}/modules/{module_id}/items"
    headers = {'Authorization': f'Bearer {CANVAS_API_TOKEN}'}

    try:
        response = requests.get(url, headers=headers, timeout=TIMEOUT)
        return response.json() if response.status_code == 200 else []
    except Exception as e:
        return []

def find_week10_pages_in_modules():
    """Find which modules contain Week 10 pages."""
    modules = get_modules()
    print(f"Checking {len(modules)} modules...\n")

    week10_locations = {}

    for module in modules:
        module_id = module.get('id')
        module_name = module.get('name')

        items = get_module_items(module_id)

        for item in items:
            page_id = str(item.get('content_id', ''))
            title = item.get('title', '')

            if page_id in WEEK10_PAGE_IDS:
                print(f"📍 Found Week 10 page in MODULE: {module_name}")
                print(f"   Page: {title}")
                print(f"   Module ID: {module_id}, Item ID: {item.get('id')}\n")

                if page_id not in week10_locations:
                    week10_locations[page_id] = []
                week10_locations[page_id].append({
                    'module_id': module_id,
                    'module_name': module_name,
                    'item_id': item.get('id'),
                    'title': title
                })

    return week10_locations, modules

def main():
    """Main workflow."""
    print("=" * 80)
    print("Week 10 Page Placement - Investigation & Fix")
    print("=" * 80)
    print()

    week10_locs, modules = find_week10_pages_in_modules()

    if not week10_locs:
        print("❌ Week 10 pages not found in any module!")
        return False

    # Find Week 10 module
    week10_module = None
    for module in modules:
        if 'Week 10' in module.get('name', ''):
            week10_module = module
            break

    if not week10_module:
        print("⚠️ No 'Week 10' module found!")
        print("\nAvailable modules:")
        for m in modules:
            print(f"  - {m.get('name')} (ID: {m.get('id')})")
        return False

    print(f"\n✅ Found Week 10 module: {week10_module.get('name')} (ID: {week10_module.get('id')})")

    # Check if pages need to be moved
    for page_id, locations in week10_locs.items():
        if len(locations) > 1:
            print(f"\n⚠️ Page {page_id} appears in multiple modules - DUPLICATE!")

        current_loc = locations[0]
        if current_loc['module_id'] != week10_module.get('id'):
            print(f"\n❌ Page {page_id} is in wrong module:")
            print(f"   Current: {current_loc['module_name']} (Module ID: {current_loc['module_id']})")
            print(f"   Should be: {week10_module.get('name')} (Module ID: {week10_module.get('id')})")
            print(f"   Action: Would need to remove from {current_loc['module_name']} and add to Week 10 module")
        else:
            print(f"\n✅ Page {page_id} is correctly placed in Week 10 module")

    return True

if __name__ == '__main__':
    import sys
    success = main()
    sys.exit(0 if success else 1)
