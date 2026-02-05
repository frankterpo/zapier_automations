#!/usr/bin/env python3
"""
Zapier Zaps Fetcher

Fetches all zaps from Zapier Workflow API and generates documentation.

Authentication Setup:
1. Go to https://developer.zapier.com/ and create an OAuth app
2. Use OAuth 2.0 Authorization Code flow to get a user access token
3. Set ZAPIER_ACCESS_TOKEN environment variable

Or use the interactive auth flow (see --auth flag)

Usage:
    python fetch_zaps.py                    # Fetch and update documentation
    python fetch_zaps.py --dry-run          # Preview without saving
    python fetch_zaps.py --output zaps.json # Save raw API response
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import urlencode

try:
    import requests
except ImportError:
    print("Error: requests library required. Install with: pip install requests")
    sys.exit(1)


# Zapier API Configuration
ZAPIER_API_BASE = "https://api.zapier.com"
ZAPS_ENDPOINT = "/v2/zaps"

# Output paths
SCRIPT_DIR = Path(__file__).parent
ZAPIER_DIR = SCRIPT_DIR.parent
OUTPUT_DIR = ZAPIER_DIR / "data"
INVENTORY_FILE = ZAPIER_DIR / "zaps_inventory.json"


def get_access_token() -> Optional[str]:
    """Get Zapier access token from environment."""
    token = os.getenv("ZAPIER_ACCESS_TOKEN")
    if not token:
        print("Error: ZAPIER_ACCESS_TOKEN environment variable not set")
        print("\nTo get a token:")
        print("1. Register an OAuth app at https://developer.zapier.com/")
        print("2. Complete OAuth 2.0 Authorization Code flow")
        print("3. Export the token: export ZAPIER_ACCESS_TOKEN='your_token'")
        return None
    return token


def fetch_zaps(
    token: str,
    expand: str = "steps",
    include_shared: bool = True,
    limit: int = 100,
) -> List[Dict[str, Any]]:
    """
    Fetch all zaps from Zapier API.
    
    Args:
        token: OAuth access token
        expand: Fields to expand (e.g., 'steps')
        include_shared: Include shared zaps
        limit: Max results per page
    
    Returns:
        List of zap objects
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    
    all_zaps = []
    offset = 0
    
    while True:
        params = {
            "expand": expand,
            "include_shared": str(include_shared).lower(),
            "limit": limit,
            "offset": offset,
        }
        
        url = f"{ZAPIER_API_BASE}{ZAPS_ENDPOINT}?{urlencode(params)}"
        
        print(f"Fetching zaps (offset={offset})...")
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Error: API returned {response.status_code}")
            print(response.text)
            break
        
        data = response.json()
        
        # Handle response format (could be list or dict with 'data' key)
        if isinstance(data, list):
            zaps = data[0].get("data", []) if data else []
        elif isinstance(data, dict):
            zaps = data.get("data", [])
        else:
            zaps = []
        
        if not zaps:
            break
        
        all_zaps.extend(zaps)
        
        # Check for pagination
        meta = data[0].get("meta", {}) if isinstance(data, list) else data.get("meta", {})
        total = meta.get("count", len(all_zaps))
        
        if len(all_zaps) >= total:
            break
        
        offset += limit
    
    print(f"Fetched {len(all_zaps)} zaps total")
    return all_zaps


def categorize_zap(zap: Dict[str, Any]) -> str:
    """Categorize a zap based on its title and apps used."""
    title = zap.get("title", "").lower()
    
    # Check title patterns
    if "demo" in title or "inbound" in title:
        return "sales"
    if "arr" in title or "target" in title or "finance" in title:
        return "finance"
    if "intercom" in title:
        return "communication"
    if "delivery" in title or "s3" in title:
        return "delivery"
    if "landscape" in title or "download" in title:
        return "marketing"
    if "hubspot" in title or "contact" in title or "deal" in title:
        return "crm"
    if "product" in title or "sign" in title:
        return "product"
    if "slack" in title:
        return "notification"
    
    return "other"


def extract_apps(zap: Dict[str, Any]) -> List[str]:
    """Extract app names from zap steps."""
    apps = set()
    steps = zap.get("steps", [])
    
    for step in steps:
        # Extract app from action ID (format: uag:app_id or app_name:action)
        action = step.get("action", "")
        if ":" in action:
            app_part = action.split(":")[0]
            if app_part != "uag":
                apps.add(app_part)
        
        # Also check title for app names
        title = step.get("title", "")
        if title:
            apps.add(title.split()[0] if title else "")
    
    return list(apps)


def determine_priority(zap: Dict[str, Any], category: str) -> str:
    """Determine zap priority based on category and status."""
    title = zap.get("title", "").lower()
    
    # Critical zaps
    if "demo" in title or "arr" in title:
        return "critical"
    
    # High priority
    if category in ["sales", "finance", "crm"]:
        return "high"
    
    # Medium priority
    if category in ["communication", "product"]:
        return "medium"
    
    return "low"


def transform_zap(zap: Dict[str, Any]) -> Dict[str, Any]:
    """Transform API zap object to documentation format."""
    category = categorize_zap(zap)
    
    return {
        "id": zap.get("id"),
        "name": zap.get("title", "Untitled"),
        "status": "ON" if zap.get("is_enabled") else "OFF",
        "steps": len(zap.get("steps", [])),
        "apps": extract_apps(zap),
        "last_successful_run": zap.get("last_successful_run_date"),
        "updated_at": zap.get("updated_at"),
        "editor_url": zap.get("links", {}).get("html_editor"),
        "category": category,
        "priority": determine_priority(zap, category),
        "has_code": any("code" in str(s).lower() for s in zap.get("steps", [])),
    }


def generate_inventory(zaps: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Generate inventory JSON from fetched zaps."""
    transformed = [transform_zap(z) for z in zaps]
    
    # Separate by status and category
    active = [z for z in transformed if z["status"] == "ON"]
    disabled = [z for z in transformed if z["status"] == "OFF"]
    
    # Categorize active zaps
    business_critical = [
        z for z in active 
        if z["category"] in ["sales", "finance", "crm", "product", "communication"]
    ]
    delivery = [z for z in active if z["category"] == "delivery"]
    marketing = [z for z in active if z["category"] == "marketing"]
    other = [
        z for z in active 
        if z not in business_critical and z not in delivery and z not in marketing
    ]
    
    return {
        "extracted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source": "Zapier Workflow API",
        "total_zaps": len(transformed),
        "active_count": len(active),
        "disabled_count": len(disabled),
        "active_business_critical_zaps": sorted(
            business_critical, 
            key=lambda x: (x["priority"] != "critical", x["priority"] != "high", x["name"])
        ),
        "active_delivery_zaps": delivery,
        "active_landscape_zaps": [z["name"] for z in marketing],
        "other_active_zaps": other,
        "disabled_legacy_zaps": [f"{z['name']} - DISABLED" for z in disabled],
    }


def generate_readme_content(inventory: Dict[str, Any]) -> str:
    """Generate README.md content from inventory."""
    lines = [
        "# Zapier Automations",
        "",
        f"*Last updated: {inventory['extracted_at']} (via API)*",
        "",
        "## Overview",
        "",
        f"- **Total Zaps**: {inventory['total_zaps']}",
        f"- **Active**: {inventory['active_count']}",
        f"- **Disabled**: {inventory['disabled_count']}",
        "",
        "## Business Critical Zaps",
        "",
        "| Name | Status | Steps | Apps | Priority | Category |",
        "|------|--------|-------|------|----------|----------|",
    ]
    
    for zap in inventory.get("active_business_critical_zaps", []):
        apps = ", ".join(zap.get("apps", [])[:3])
        if len(zap.get("apps", [])) > 3:
            apps += "..."
        lines.append(
            f"| {zap['name']} | {zap['status']} | {zap.get('steps', '?')} | "
            f"{apps} | {zap['priority']} | {zap['category']} |"
        )
    
    lines.extend([
        "",
        "## Delivery Monitoring Zaps",
        "",
    ])
    
    for zap in inventory.get("active_delivery_zaps", []):
        lines.append(f"- {zap['name']}")
    
    lines.extend([
        "",
        "## Marketing/Landscape Zaps",
        "",
    ])
    
    for name in inventory.get("active_landscape_zaps", []):
        lines.append(f"- {name}")
    
    if inventory.get("disabled_legacy_zaps"):
        lines.extend([
            "",
            "## Disabled/Legacy",
            "",
        ])
        for name in inventory.get("disabled_legacy_zaps", []):
            lines.append(f"- {name}")
    
    return "\n".join(lines)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Fetch Zapier zaps and generate documentation")
    parser.add_argument("--dry-run", action="store_true", help="Preview without saving")
    parser.add_argument("--output", type=str, help="Output raw API response to file")
    parser.add_argument("--token", type=str, help="Zapier access token (or use env var)")
    args = parser.parse_args()
    
    # Get token
    token = args.token or get_access_token()
    if not token:
        sys.exit(1)
    
    # Fetch zaps
    zaps = fetch_zaps(token)
    
    if not zaps:
        print("No zaps found or error occurred")
        sys.exit(1)
    
    # Save raw output if requested
    if args.output:
        with open(args.output, "w") as f:
            json.dump(zaps, f, indent=2)
        print(f"Raw API response saved to {args.output}")
    
    # Generate inventory
    inventory = generate_inventory(zaps)
    
    if args.dry_run:
        print("\n=== Generated Inventory (dry run) ===")
        print(json.dumps(inventory, indent=2))
        return
    
    # Save inventory
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f, indent=2)
    print(f"Inventory saved to {INVENTORY_FILE}")
    
    # Save raw data
    raw_file = OUTPUT_DIR / f"zaps_raw_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(raw_file, "w") as f:
        json.dump(zaps, f, indent=2)
    print(f"Raw data saved to {raw_file}")
    
    # Generate README update
    readme_content = generate_readme_content(inventory)
    print("\n=== Generated README snippet ===")
    print(readme_content[:500] + "..." if len(readme_content) > 500 else readme_content)


if __name__ == "__main__":
    main()
