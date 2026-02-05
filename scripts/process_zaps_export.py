#!/usr/bin/env python3
"""
Process Zapier Zaps Export

Processes a JSON export from Zapier (obtained via browser) and generates
comprehensive documentation.

Usage:
    1. Export zaps from browser (see SETUP.md)
    2. Run: python process_zaps_export.py path/to/export.json

This will:
    - Update zaps_inventory.json with detailed info
    - Generate individual README files for each active zap
    - Update the main README.md with summary tables
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


SCRIPT_DIR = Path(__file__).parent
ZAPIER_DIR = SCRIPT_DIR.parent
INVENTORY_FILE = ZAPIER_DIR / "zaps_inventory.json"


def sanitize_folder_name(name: str) -> str:
    """Convert zap name to valid folder name."""
    # Remove special characters, replace spaces with underscores
    sanitized = re.sub(r'[^\w\s-]', '', name)
    sanitized = re.sub(r'\s+', '_', sanitized).strip('_')
    return sanitized.lower()


def extract_apps_from_zap(zap: Dict) -> List[str]:
    """Extract unique app names from zap steps."""
    apps = []
    
    # Try different data structures based on API version
    steps = zap.get('steps', []) or zap.get('nodes', [])
    
    for step in steps:
        app_name = (
            step.get('app', {}).get('name') or
            step.get('app_name') or
            step.get('selected_api') or
            step.get('type_of', '').split('.')[0]
        )
        if app_name and app_name not in apps:
            apps.append(app_name)
    
    # Fallback: check title for known app names
    if not apps:
        title = zap.get('title', '') or zap.get('name', '')
        known_apps = ['HubSpot', 'Slack', 'Gmail', 'Google Sheets', 'Intercom', 
                      'GetForm', 'AWS S3', 'Webhook', 'Code by Zapier', 'Filter', 
                      'Formatter', 'Schedule']
        for app in known_apps:
            if app.lower() in title.lower():
                apps.append(app)
    
    return apps


def categorize_zap(zap: Dict) -> tuple[str, str]:
    """Return (category, priority) for a zap."""
    title = (zap.get('title', '') or zap.get('name', '')).lower()
    
    # Determine category
    if 'demo' in title or 'inbound' in title:
        category = 'sales'
        priority = 'critical'
    elif 'arr' in title:
        category = 'finance'
        priority = 'critical'
    elif 'deal' in title and ('signed' in title or 'renewed' in title):
        category = 'sales'
        priority = 'high'
    elif 'target' in title or 'sales target' in title:
        category = 'finance'
        priority = 'high'
    elif 'intercom' in title:
        category = 'communication'
        priority = 'high'
    elif 'product' in title:
        category = 'product'
        priority = 'high'
    elif 'delivery' in title or 's3' in title or 'log' in title:
        category = 'delivery'
        priority = 'medium'
    elif 'landscape' in title or 'download' in title:
        category = 'marketing'
        priority = 'low'
    elif 'hubspot' in title or 'contact' in title or 'lifecycle' in title:
        category = 'hubspot'
        priority = 'medium'
    else:
        category = 'other'
        priority = 'low'
    
    return category, priority


def check_has_code(zap: Dict) -> bool:
    """Check if zap contains Code by Zapier steps."""
    steps = zap.get('steps', []) or zap.get('nodes', [])
    
    for step in steps:
        step_str = json.dumps(step).lower()
        if 'code by zapier' in step_str or 'codebyzapier' in step_str:
            return True
    
    return False


def transform_zap(zap: Dict) -> Dict[str, Any]:
    """Transform raw zap data to documentation format."""
    title = zap.get('title', '') or zap.get('name', 'Untitled')
    category, priority = categorize_zap(zap)
    
    # Determine status
    is_enabled = zap.get('is_enabled') or zap.get('state') == 'on'
    
    return {
        "id": zap.get('id'),
        "name": title,
        "status": "ON" if is_enabled else "OFF",
        "steps": len(zap.get('steps', []) or zap.get('nodes', [])),
        "apps": extract_apps_from_zap(zap),
        "last_successful_run": zap.get('last_successful_run_date') or zap.get('last_successful_run_at'),
        "updated_at": zap.get('updated_at') or zap.get('modified_at'),
        "created_at": zap.get('created_at'),
        "editor_url": (
            zap.get('links', {}).get('html_editor') or 
            f"https://zapier.com/editor/{zap.get('id')}"
        ),
        "category": category,
        "priority": priority,
        "has_code": check_has_code(zap),
        "folder_name": sanitize_folder_name(title),
    }


def generate_zap_readme(zap: Dict) -> str:
    """Generate README.md content for a single zap."""
    return f"""# {zap['name']}

**Status**: {zap['status']} | **Priority**: {zap['priority'].upper()} | **Category**: {zap['category']}

## Overview

| Property | Value |
|----------|-------|
| Zap ID | `{zap.get('id', 'N/A')}` |
| Steps | {zap.get('steps', 'Unknown')} |
| Has Code | {'Yes' if zap.get('has_code') else 'No'} |
| Last Run | {zap.get('last_successful_run', 'Unknown')} |
| Updated | {zap.get('updated_at', 'Unknown')} |

## Apps Used

{chr(10).join(f'- {app}' for app in zap.get('apps', ['Unknown']))}

## Editor Link

[Open in Zapier Editor]({zap.get('editor_url', 'https://zapier.com/app/zaps')})

## What This Zap Does

*TODO: Add description of what this automation does*

## Trigger

*TODO: Document the trigger condition*

## Actions

*TODO: Document each action step*

## Notes

*TODO: Add any important notes or context*

---
*Auto-generated from Zapier API export on {datetime.now().strftime('%Y-%m-%d')}*
"""


def generate_inventory(zaps: List[Dict]) -> Dict[str, Any]:
    """Generate inventory structure from transformed zaps."""
    active = [z for z in zaps if z['status'] == 'ON']
    disabled = [z for z in zaps if z['status'] == 'OFF']
    
    # Categorize
    business_critical = [
        z for z in active 
        if z['category'] in ['sales', 'finance', 'hubspot', 'product', 'communication']
    ]
    delivery = [z for z in active if z['category'] == 'delivery']
    marketing = [z for z in active if z['category'] == 'marketing']
    other = [z for z in active if z['category'] == 'other']
    
    # Sort by priority
    priority_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
    business_critical.sort(key=lambda x: (priority_order.get(x['priority'], 4), x['name']))
    
    return {
        "extracted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source": "Browser export processed by process_zaps_export.py",
        "total_zaps": len(zaps),
        "active_count": len(active),
        "disabled_count": len(disabled),
        "note": "Only active (ON) Zaps documented - inactive/paused excluded",
        "active_business_critical_zaps": business_critical,
        "active_delivery_zaps": delivery,
        "active_landscape_zaps": [z['name'] for z in marketing],
        "other_active_zaps": other,
        "disabled_legacy_zaps": [f"{z['name']} - DISABLED" for z in disabled],
    }


def create_zap_folders(zaps: List[Dict], dry_run: bool = False) -> List[str]:
    """Create folder structure and README for each active business zap."""
    created = []
    
    for zap in zaps:
        if zap['status'] != 'ON':
            continue
        if zap['category'] in ['delivery', 'marketing']:  # Skip simple zaps
            continue
        
        folder_name = zap['folder_name']
        folder_path = ZAPIER_DIR / folder_name
        readme_path = folder_path / "README.md"
        
        if dry_run:
            print(f"Would create: {folder_path}")
            continue
        
        # Create folder if doesn't exist
        if not folder_path.exists():
            folder_path.mkdir(parents=True)
            created.append(str(folder_path))
            print(f"Created: {folder_path}")
        
        # Create/update README if doesn't exist or is placeholder
        if not readme_path.exists():
            with open(readme_path, 'w') as f:
                f.write(generate_zap_readme(zap))
            print(f"  Created README: {readme_path}")
    
    return created


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Process Zapier export and generate documentation")
    parser.add_argument("export_file", help="Path to JSON export file")
    parser.add_argument("--dry-run", action="store_true", help="Preview without saving")
    parser.add_argument("--skip-folders", action="store_true", help="Don't create zap folders")
    args = parser.parse_args()
    
    # Load export file
    export_path = Path(args.export_file)
    if not export_path.exists():
        print(f"Error: File not found: {export_path}")
        sys.exit(1)
    
    with open(export_path) as f:
        raw_data = json.load(f)
    
    # Handle different export formats
    if isinstance(raw_data, list):
        zaps_list = raw_data
    elif isinstance(raw_data, dict):
        zaps_list = raw_data.get('data', []) or raw_data.get('objects', []) or raw_data.get('zaps', [])
    else:
        print("Error: Unexpected data format")
        sys.exit(1)
    
    if not zaps_list:
        print("Error: No zaps found in export file")
        sys.exit(1)
    
    print(f"Processing {len(zaps_list)} zaps...")
    
    # Transform zaps
    transformed = [transform_zap(z) for z in zaps_list]
    
    # Generate inventory
    inventory = generate_inventory(transformed)
    
    if args.dry_run:
        print("\n=== Inventory Preview ===")
        print(f"Total: {inventory['total_zaps']}")
        print(f"Active: {inventory['active_count']}")
        print(f"Disabled: {inventory['disabled_count']}")
        print(f"\nBusiness Critical ({len(inventory['active_business_critical_zaps'])}):")
        for z in inventory['active_business_critical_zaps'][:5]:
            print(f"  - {z['name']} ({z['priority']})")
        print("  ...")
        return
    
    # Save inventory
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(inventory, f, indent=2)
    print(f"\nInventory saved to: {INVENTORY_FILE}")
    
    # Create folders
    if not args.skip_folders:
        print("\nCreating zap folders...")
        create_zap_folders(inventory['active_business_critical_zaps'])
    
    print("\nDone! Summary:")
    print(f"  - Total zaps: {inventory['total_zaps']}")
    print(f"  - Active: {inventory['active_count']}")
    print(f"  - Business critical: {len(inventory['active_business_critical_zaps'])}")
    print(f"  - Delivery: {len(inventory['active_delivery_zaps'])}")
    print(f"  - Marketing/Landscape: {len(inventory['active_landscape_zaps'])}")


if __name__ == "__main__":
    main()
