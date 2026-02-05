#!/usr/bin/env python3
"""
Fetch Zaps using Zapier's internal v1/v4 API.

This script uses cookies from your browser session to authenticate.
You need to copy cookies from your logged-in Zapier session.

Usage:
    1. Log into zapier.com in your browser
    2. Open DevTools (F12) -> Application -> Cookies -> zapier.com
    3. Copy the 'zapier_session' cookie value
    4. Set it as environment variable or pass directly:
       
       export ZAPIER_SESSION_COOKIE='your_session_cookie_here'
       python fetch_zaps_v1.py
       
    Or use browser export method (see SETUP.md)
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

try:
    import requests
except ImportError:
    print("Error: requests library required. Install with: pip install requests")
    sys.exit(1)

SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR / "data"


def fetch_zaps_with_cookie(session_cookie: str, limit: int = 100) -> Dict:
    """Fetch zaps using session cookie."""
    
    url = f"https://zapier.com/api/v4/zaps"
    
    params = {
        "limit": limit,
    }
    
    headers = {
        "Accept": "application/json",
        "Cookie": f"zapier_session={session_cookie}",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    }
    
    print(f"Fetching zaps from {url}...")
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 401:
        raise Exception("Unauthorized - session cookie may be expired or invalid")
    
    if response.status_code != 200:
        raise Exception(f"API error {response.status_code}: {response.text[:500]}")
    
    return response.json()


def fetch_all_zaps(session_cookie: str) -> List[Dict]:
    """Fetch all zaps with pagination."""
    all_zaps = []
    offset = 0
    limit = 100
    
    # Try different cookie formats
    cookie_formats = [
        f"zapier_session={session_cookie}",
        f"zapier-app-session={session_cookie}",
        f"session={session_cookie}",
        session_cookie,  # Raw cookie string
    ]
    
    working_cookie = None
    
    for cookie_fmt in cookie_formats:
        url = "https://zapier.com/api/v4/zaps"
        params = {"limit": 1}
        headers = {
            "Accept": "application/json",
            "Cookie": cookie_fmt,
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        }
        
        test_resp = requests.get(url, params=params, headers=headers)
        if test_resp.status_code == 200:
            working_cookie = cookie_fmt
            print(f"Found working cookie format!")
            break
    
    if not working_cookie:
        print("None of the cookie formats worked. Trying raw...")
        working_cookie = session_cookie
    
    while True:
        url = f"https://zapier.com/api/v4/zaps"
        params = {"limit": limit, "offset": offset}
        headers = {
            "Accept": "application/json",
            "Cookie": working_cookie,
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        }
        
        print(f"Fetching zaps (offset={offset})...")
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break
        
        data = response.json()
        zaps = data.get("objects", data.get("data", []))
        
        if not zaps:
            break
        
        all_zaps.extend(zaps)
        
        # Check if more pages
        if len(zaps) < limit:
            break
        
        offset += limit
    
    return all_zaps


def process_zap(zap: Dict) -> Dict:
    """Process raw zap data."""
    return {
        "id": zap.get("id"),
        "title": zap.get("title", "Untitled"),
        "is_enabled": zap.get("state") == "on" or zap.get("is_enabled", False),
        "state": zap.get("state", "unknown"),
        "created_at": zap.get("created_at"),
        "updated_at": zap.get("updated_at"),
        "last_successful_run": zap.get("last_successful_run_at"),
        "url": zap.get("url") or f"https://zapier.com/editor/{zap.get('id')}",
        "steps": zap.get("steps", []),
        "steps_count": len(zap.get("steps", [])),
    }


def categorize_zap(title: str) -> str:
    """Categorize zap based on title."""
    title_lower = title.lower()
    
    if "demo" in title_lower or "inbound" in title_lower:
        return "sales"
    if "arr" in title_lower or "target" in title_lower or "revenue" in title_lower:
        return "finance"
    if "intercom" in title_lower:
        return "communication"
    if "delivery" in title_lower or "s3" in title_lower or "log" in title_lower:
        return "delivery"
    if "landscape" in title_lower or "download" in title_lower:
        return "marketing"
    if "deal" in title_lower or "hubspot" in title_lower:
        return "crm"
    if "product" in title_lower or "sign" in title_lower:
        return "product"
    if "slack" in title_lower:
        return "communication"
    
    return "other"


def generate_inventory(zaps: List[Dict]) -> Dict:
    """Generate inventory from processed zaps."""
    processed = [process_zap(z) for z in zaps]
    
    for z in processed:
        z["category"] = categorize_zap(z["title"])
    
    active = [z for z in processed if z["is_enabled"]]
    disabled = [z for z in processed if not z["is_enabled"]]
    
    return {
        "extracted_at": datetime.now().isoformat(),
        "source": "Zapier Internal API v4",
        "total": len(processed),
        "active": len(active),
        "disabled": len(disabled),
        "zaps": processed,
        "by_category": {
            cat: [z for z in processed if z["category"] == cat]
            for cat in ["sales", "finance", "communication", "delivery", "marketing", "crm", "product", "other"]
        },
    }


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Fetch Zaps from Zapier")
    parser.add_argument("--cookie", type=str, help="Zapier session cookie")
    parser.add_argument("--output", type=str, default="zaps_export.json", help="Output filename")
    args = parser.parse_args()
    
    # Get session cookie
    session_cookie = args.cookie or os.getenv("ZAPIER_SESSION_COOKIE")
    
    if not session_cookie:
        print("=" * 60)
        print("No session cookie provided!")
        print("=" * 60)
        print()
        print("To get your session cookie:")
        print("1. Log into https://zapier.com")
        print("2. Open DevTools (F12) → Application → Cookies → zapier.com")
        print("3. Copy the 'zapier_session' cookie value")
        print("4. Run again with:")
        print()
        print("   python fetch_zaps_v1.py --cookie 'YOUR_COOKIE_VALUE'")
        print()
        print("   Or set environment variable:")
        print("   export ZAPIER_SESSION_COOKIE='YOUR_COOKIE_VALUE'")
        print()
        sys.exit(1)
    
    try:
        # Fetch all zaps
        print("\n=== Fetching Zaps from Zapier ===\n")
        zaps = fetch_all_zaps(session_cookie)
        
        print(f"\nFetched {len(zaps)} zaps")
        
        # Generate inventory
        inventory = generate_inventory(zaps)
        
        # Save output
        DATA_DIR.mkdir(exist_ok=True)
        output_path = DATA_DIR / args.output
        
        with open(output_path, "w") as f:
            json.dump(inventory, f, indent=2)
        
        print(f"Saved to {output_path}")
        
        # Summary
        print(f"\n=== Summary ===")
        print(f"Total: {inventory['total']}")
        print(f"Active: {inventory['active']}")
        print(f"Disabled: {inventory['disabled']}")
        print(f"\nBy Category:")
        for cat, zaps_list in inventory["by_category"].items():
            if zaps_list:
                print(f"  {cat}: {len(zaps_list)}")
        
        # List active zaps
        print(f"\n=== Active Zaps ===")
        for z in inventory["zaps"]:
            if z["is_enabled"]:
                print(f"  ✓ {z['title'][:60]}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
