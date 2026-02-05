#!/usr/bin/env python3
"""
Zapier Workflow API Client - Enhanced Documentation Generator

Fetches full zap details with step information and generates comprehensive README documentation.

Usage:
    python zapier_api.py --setup              # Run OAuth flow to get tokens
    python zapier_api.py --fetch              # Fetch all zaps with step details
    python zapier_api.py --document           # Generate READMEs for mapped zaps
    python zapier_api.py --document --zap-id 262386682  # Generate README for specific zap
    python zapier_api.py --runs --zap-id 262386682      # Fetch run history

Environment Variables:
    ZAPIER_CLIENT_ID: Your OAuth client ID
    ZAPIER_CLIENT_SECRET: Your OAuth client secret
    ZAPIER_ACCESS_TOKEN: Access token (after OAuth flow)
    ZAPIER_REFRESH_TOKEN: Refresh token (for token renewal)
"""

import json
import os
import re
import sys
import webbrowser
from datetime import datetime, timedelta
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import parse_qs, urlencode, urlparse

try:
    import requests
except ImportError:
    print("Error: requests library required. Install with: pip install requests")
    sys.exit(1)


# ============================================================================
# Configuration
# ============================================================================

ZAPIER_AUTH_URL = "https://zapier.com/oauth/authorize"
ZAPIER_TOKEN_URL = "https://zapier.com/oauth/token"
ZAPIER_API_BASE = "https://api.zapier.com"

# OAuth scopes needed
SCOPES = ["zap:all", "zap:read"]  # zap:all to see all owned zaps

# Local server for OAuth callback
REDIRECT_URI = "http://localhost:8080/callback"
REDIRECT_PORT = 8080

# Output paths
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR / "data"
TOKENS_FILE = SCRIPT_DIR / ".zapier_tokens.json"
ZAPIER_ROOT = SCRIPT_DIR.parent  # zapier_automations folder

# ============================================================================
# Zap-to-Folder Mapping (by zap title patterns and IDs)
# ============================================================================

# Map zap IDs to documentation folders
# Note: Some folders represent Code by Zapier steps embedded in other zaps
ZAP_FOLDER_MAP = {
    # === LEADS FOLDER ZAPS ===
    262386682: "demo_requests",           # Demo Requests (Getform > Sheets > Hubspot > Slack) - MAIN ACTIVE
    341760432: None,                      # etn. Demo Requests (copy/test) - skip
    330771370: None,                      # (Copy) Demo Requests - skip
    268969745: "product_sign_ups",        # Product Sign Ups - ACTIVE
    340050649: None,                      # (Copy) Product Sign Ups - skip
    
    # === CS FOLDER ZAPS ===
    266596665: "intercom_bot_reply",      # Intercom Bot Reply / Slack (PAUSED)
    207157349: "intercom_demo_email",     # Intercom Demo Email / Slack - ACTIVE
    206743152: "intercom_request_slack",  # Intercom Request / Slack - ACTIVE
    
    # === HUBSPOT/SALES AUTOMATIONS ===
    300616653: "auto_set_lifecycle",      # Auto-set: Previous Customer / Customer - ACTIVE
    240869492: "contacts_deals_associations",  # Contacts to Deals Associations (PAUSED)
    236426171: "deal_renewed",            # Deal Renewed - ACTIVE
    247549034: "sales_target_update",     # SALES TARGET UPDATE - ACTIVE
    164077234: "deal_signed",             # Deal Signed - ACTIVE
    186806230: "arr_update",              # ARR UPDATE - ACTIVE
}

# Folders that are CODE STEPS (embedded in other zaps, not standalone)
# These have Python code tracked separately
EMBEDDED_CODE_FOLDERS = {
    "deal_owner_assignment": {
        "parent_zap_id": 262386682,
        "parent_name": "demo_requests",
        "step_name": "Deal Owner Assignment",
        "code_file": "hubspot_automations/scripts/hs_zapier_code/assign_deal_owner/zapier_deal_owner.py",
    },
    # Add more embedded code steps here
}

# Folders that are ASSET FOLDERS (not zaps)
ASSET_FOLDERS = [
    "screenshots",  # Screenshots for documentation
]

# Folders WITHOUT IDENTIFIED ZAPS (may need manual mapping or creation)
UNMAPPED_FOLDERS = [
    "arr_update",           # ARR tracking - may be in Google Sheets automation
    "deal_signed",          # Deal signed notification - may be embedded
    "intercom_request_slack",  # May be same as intercom_bot_reply
    "product_import_requests",  # Product import flow - may not exist
]

# Title-based mapping fallback (regex patterns)
ZAP_TITLE_PATTERNS = {
    r"arr.*update|update.*arr": "arr_update",
    r"auto.*set.*lifecycle|lifecycle.*auto": "auto_set_lifecycle",
    r"contacts.*deals.*association|association.*contacts": "contacts_deals_associations",
    r"deal.*owner.*assignment|assign.*deal.*owner": "deal_owner_assignment",
    r"deal.*renewed|renewed.*deal": "deal_renewed",
    r"deal.*signed|signed.*deal": "deal_signed",
    r"demo.*request|request.*demo|getform.*hubspot": "demo_requests",
    r"intercom.*bot.*reply|bot.*reply.*slack": "intercom_bot_reply",
    r"intercom.*demo.*email": "intercom_demo_email",
    r"intercom.*request.*slack|intercom.*slack": "intercom_request_slack",
    r"product.*import.*request": "product_import_requests",
    r"product.*sign.*up": "product_sign_ups",
    r"sales.*target.*update|target.*update": "sales_target_update",
    r"screenshot": "screenshots",
}

# App name mappings for cleaner display (from selected_api field)
APP_NAMES = {
    "hubspot": "HubSpot",
    "google_sheets": "Google Sheets",
    "slack": "Slack",
    "intercom": "Intercom",
    "getform": "GetForm",
    "formatter": "Formatter by Zapier",
    "code": "Code by Zapier",
    "filter": "Filter by Zapier",
    "paths": "Paths by Zapier",
    "delay": "Delay by Zapier",
    "gmail": "Gmail",
    "webhooks": "Webhooks by Zapier",
    "schedule": "Schedule by Zapier",
    # From v4 API selected_api field
    "hubspotcliapi": "HubSpot",
    "googlesheetsv2cliapi": "Google Sheets",
    "googlesheetscliapi": "Google Sheets",
    "slackcliapi": "Slack",
    "intercomcliapi": "Intercom",
    "getformcliapi": "GetForm",
    "zapierformattercliapi": "Formatter by Zapier",
    "codecliapi": "Code by Zapier",
    "branchingapi": "Paths by Zapier",
    "filtercliapi": "Filter by Zapier",
    "delaycliapi": "Delay by Zapier",
    "googlemailv2cliapi": "Gmail",
    "webhookscliapi": "Webhooks by Zapier",
    "schedulecliapi": "Schedule by Zapier",
    "tallycliapi": "Tally",
    "loopscliapi": "Loops by Zapier",
    "digestcliapi": "Digest by Zapier",
    "storagecliapi": "Storage by Zapier",
}

# Action name mappings for cleaner display
ACTION_NAMES = {
    "submission": "New Form Submission",
    "add_row": "Create Spreadsheet Row",
    "update_row": "Update Spreadsheet Row",
    "channel_message": "Send Channel Message",
    "direct_message": "Send Direct Message",
    "create_contact": "Create Contact",
    "update_contact": "Update Contact",
    "create_company": "Create Company",
    "update_company": "Update Company",
    "create_deal": "Create Deal",
    "update_deal": "Update Deal",
    "deal_crmSearch": "Find Deal",
    "contact_crmSearch": "Find Contact",
    "company_crmSearch": "Find Company",
    "create_associations": "Create Associations",
    "update_crm_deal": "Update CRM Deal",
    "update_crm_contact": "Update CRM Contact",
    "message": "Send Email",
    "filter": "Filter",
    "paths": "Paths (Branching)",
}

# Owner ID to name mapping
OWNER_NAMES = {
    "35673999": "Marco Squarci",
    "77583320": "Philipp Berhoerster",
    "49928941": "Dominik Vacikar",
    "200411144": "Francisco Terpolilli",
    "713358197": "Isabella Garcia Foster",
    "1509688330": "David Looby",
    "6924914": "Dominik Vacikar",  # Account owner
}


# ============================================================================
# OAuth Flow
# ============================================================================

class OAuthCallbackHandler(BaseHTTPRequestHandler):
    """Handle OAuth callback."""
    
    auth_code = None
    
    def do_GET(self):
        """Handle GET request from OAuth redirect."""
        query = parse_qs(urlparse(self.path).query)
        
        if "code" in query:
            OAuthCallbackHandler.auth_code = query["code"][0]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"""
                <html><body>
                <h1>Authorization successful!</h1>
                <p>You can close this window and return to the terminal.</p>
                </body></html>
            """)
        else:
            error = query.get("error", ["Unknown error"])[0]
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f"""
                <html><body>
                <h1>Authorization failed</h1>
                <p>Error: {error}</p>
                </body></html>
            """.encode())
    
    def log_message(self, format, *args):
        """Suppress HTTP logs."""
        pass


def get_authorization_url(client_id: str, state: str = "zapier_auth") -> str:
    """Generate OAuth authorization URL."""
    params = {
        "client_id": client_id,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": " ".join(SCOPES),
        "state": state,
    }
    return f"{ZAPIER_AUTH_URL}?{urlencode(params)}"


def exchange_code_for_tokens(
    client_id: str, 
    client_secret: str, 
    auth_code: str
) -> Dict[str, str]:
    """Exchange authorization code for access/refresh tokens."""
    data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "client_secret": client_secret,
        "code": auth_code,
        "redirect_uri": REDIRECT_URI,
    }
    
    response = requests.post(ZAPIER_TOKEN_URL, data=data)
    
    if response.status_code != 200:
        raise Exception(f"Token exchange failed: {response.text}")
    
    return response.json()


def refresh_access_token(
    client_id: str,
    client_secret: str,
    refresh_token: str
) -> Dict[str, str]:
    """Refresh access token using refresh token."""
    data = {
        "grant_type": "refresh_token",
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
    }
    
    response = requests.post(ZAPIER_TOKEN_URL, data=data)
    
    if response.status_code != 200:
        raise Exception(f"Token refresh failed: {response.text}")
    
    return response.json()


def run_oauth_flow(client_id: str, client_secret: str) -> Dict[str, str]:
    """Run complete OAuth flow interactively."""
    print("\n=== Zapier OAuth Setup ===\n")
    
    # Generate auth URL
    auth_url = get_authorization_url(client_id)
    print(f"Opening browser for authorization...")
    print(f"If browser doesn't open, visit:\n{auth_url}\n")
    
    webbrowser.open(auth_url)
    
    # Start local server to receive callback
    print(f"Waiting for callback on {REDIRECT_URI}...")
    server = HTTPServer(("localhost", REDIRECT_PORT), OAuthCallbackHandler)
    server.handle_request()  # Handle single request
    
    if not OAuthCallbackHandler.auth_code:
        raise Exception("No authorization code received")
    
    print("Authorization code received, exchanging for tokens...")
    
    # Exchange code for tokens
    tokens = exchange_code_for_tokens(
        client_id, 
        client_secret, 
        OAuthCallbackHandler.auth_code
    )
    
    return tokens


def save_tokens(tokens: Dict[str, str]):
    """Save tokens to file."""
    tokens["saved_at"] = datetime.now().isoformat()
    with open(TOKENS_FILE, "w") as f:
        json.dump(tokens, f, indent=2)
    print(f"Tokens saved to {TOKENS_FILE}")


def load_tokens() -> Optional[Dict[str, str]]:
    """Load tokens from file."""
    if TOKENS_FILE.exists():
        with open(TOKENS_FILE) as f:
            return json.load(f)
    return None


# ============================================================================
# API Client
# ============================================================================

class ZapierAPIClient:
    """Client for Zapier Workflow API."""
    
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.base_url = ZAPIER_API_BASE
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        })
    
    def _request(self, method: str, endpoint: str, **kwargs) -> Dict:
        """Make API request."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        
        if response.status_code == 401:
            raise Exception("Unauthorized - token may be expired. Run --setup again.")
        
        if response.status_code != 200:
            raise Exception(f"API error {response.status_code}: {response.text}")
        
        return response.json()
    
    def get_zaps(
        self,
        expand: str = "steps",
        include_shared: bool = True,
        limit: int = 100,
        offset: int = 0,
    ) -> Dict:
        """
        Get list of zaps.
        
        Args:
            expand: Fields to expand ('steps' for step details)
            include_shared: Include shared zaps
            limit: Max results per page
            offset: Pagination offset
        
        Returns:
            API response with zaps data
        """
        params = {
            "expand": expand,
            "include_shared": str(include_shared).lower(),
            "limit": limit,
            "offset": offset,
        }
        return self._request("GET", "/v2/zaps", params=params)
    
    def get_all_zaps(self, expand: str = "steps") -> List[Dict]:
        """Fetch all zaps with pagination."""
        all_zaps = []
        offset = 0
        limit = 100
        
        while True:
            print(f"Fetching zaps (offset={offset})...")
            response = self.get_zaps(expand=expand, limit=limit, offset=offset)
            
            # Handle response format
            if isinstance(response, list):
                data = response[0] if response else {}
            else:
                data = response
            
            zaps = data.get("data", [])
            if not zaps:
                break
            
            all_zaps.extend(zaps)
            
            # Check pagination
            meta = data.get("meta", {})
            total = meta.get("count", len(all_zaps))
            
            if len(all_zaps) >= total:
                break
            
            offset += limit
        
        return all_zaps
    
    def get_zap_runs(self, zap_id: str, limit: int = 50) -> Dict:
        """
        Get recent runs/events for a specific zap.
        
        Note: This endpoint may require additional scopes.
        """
        params = {"limit": limit}
        return self._request("GET", f"/v2/zaps/{zap_id}/runs", params=params)
    
    def get_zap_details(self, zap_id: str) -> Dict:
        """
        Get full details for a specific zap including steps.
        """
        return self._request("GET", f"/v2/zaps/{zap_id}", params={"expand": "steps"})
    
    def get_execution_logs(
        self,
        zap_id: str = None,
        status: str = None,
        limit: int = 100,
        start_date: str = None,
        end_date: str = None,
    ) -> Dict:
        """
        Get execution logs (if available via API).
        
        Args:
            zap_id: Filter by specific zap
            status: Filter by status ('success', 'error', 'held')
            limit: Max results
            start_date: ISO date string for start of range
            end_date: ISO date string for end of range
        """
        params = {"limit": limit}
        if zap_id:
            params["zap_id"] = zap_id
        if status:
            params["status"] = status
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        
        # Try execution logs endpoint (may not be available)
        try:
            return self._request("GET", "/v2/execution-logs", params=params)
        except Exception:
            # Fallback to runs endpoint if logs not available
            if zap_id:
                return self.get_zap_runs(zap_id, limit)
            raise


# ============================================================================
# Data Processing & App Extraction
# ============================================================================

def extract_app_from_action(action: str) -> Tuple[str, str]:
    """
    Extract app name and action type from action string.
    
    Action formats:
    - "hubspot:create_contact" -> ("hubspot", "create_contact")
    - "uag:1f188536-6dd0-4172-8414-2b90914ddee9" -> ("zapier_internal", "custom_action")
    - "google_sheets:create_spreadsheet_row" -> ("google_sheets", "create_spreadsheet_row")
    
    Returns:
        Tuple of (app_name, action_type)
    """
    if not action:
        return ("unknown", "unknown")
    
    if ":" in action:
        parts = action.split(":", 1)
        app_key = parts[0].lower()
        action_type = parts[1] if len(parts) > 1 else "action"
        
        # Handle Zapier internal actions
        if app_key == "uag":
            return ("zapier_internal", "custom_action")
        
        return (app_key, action_type)
    
    return (action.lower(), "action")


def extract_app_from_selected_api(selected_api: str) -> str:
    """
    Extract app name from v4 API selected_api field.
    
    Format: "HubSpotCLIAPI@1.12.4" -> "hubspot"
    """
    if not selected_api:
        return "unknown"
    
    # Remove version suffix
    api_name = selected_api.split("@")[0]
    
    # Remove common suffixes
    api_name = api_name.replace("CLIAPI", "").replace("V2", "").replace("API", "")
    
    return api_name.lower()


def process_v4_node(node: Dict, index: int) -> Dict:
    """Process a node from v4 API format into step format."""
    selected_api = node.get("selected_api") or ""
    action = node.get("action") or ""
    type_of = node.get("type_of") or "write"
    
    # Extract app name
    app_key = extract_app_from_selected_api(selected_api)
    app_display = format_app_name(app_key) or (selected_api.split("@")[0] if selected_api else "Unknown")
    
    # Format action name
    action_display = ACTION_NAMES.get(action, action) if action else "Unknown Action"
    if action and action.startswith("0") and "-" in action:  # UUID for code actions
        action_display = "Custom Code"
    
    # Determine step type
    step_type_map = {
        "read": "trigger",
        "write": "action",
        "filter": "filter",
        "search": "search",
        "search_or_write": "search_or_create",
    }
    step_type = step_type_map.get(type_of, "action")
    if index == 0:
        step_type = "trigger"
    if selected_api and "branching" in selected_api.lower():
        step_type = "path"
    elif action and "filter" in action.lower():
        step_type = "filter"
    
    return {
        "index": index + 1,
        "title": f"{app_display}: {action_display}",
        "app": app_display,
        "app_key": app_key,
        "action": action,
        "action_display": action_display,
        "step_type": step_type,
        "type_of": type_of,
        "node_id": node.get("id"),
        "parent_id": node.get("parent_id"),
        "auth_id": node.get("auth_id"),
        "selected_api": selected_api,
    }


def format_app_name(app_key: str) -> str:
    """Convert app key to display name."""
    if app_key in APP_NAMES:
        return APP_NAMES[app_key]
    
    # Default: capitalize and replace underscores
    return app_key.replace("_", " ").title()


def format_action_name(action_type: str) -> str:
    """Convert action type to readable name."""
    # Replace underscores with spaces and capitalize
    return action_type.replace("_", " ").title()


def get_folder_for_zap(zap_id: int, title: str) -> Optional[str]:
    """
    Determine the documentation folder for a zap.
    
    Args:
        zap_id: Zapier zap ID
        title: Zap title
    
    Returns:
        Folder name or None if no match (or explicitly None in map)
    """
    # First try ID mapping
    if zap_id in ZAP_FOLDER_MAP:
        folder = ZAP_FOLDER_MAP[zap_id]
        # Return None if explicitly set to None (skip copies/test zaps)
        return folder
    
    # Handle None or empty title
    if not title:
        return None
    
    # Try title pattern matching (for zaps not in explicit map)
    title_lower = title.lower()
    
    # Skip copies and test zaps
    if "(copy)" in title_lower or "etn." in title_lower or "test" in title_lower:
        return None
    
    for pattern, folder in ZAP_TITLE_PATTERNS.items():
        if re.search(pattern, title_lower):
            return folder
    
    return None


def process_zap(zap: Dict) -> Dict:
    """Process raw zap data into comprehensive documentation format.
    
    Handles both v2 API format (steps array) and v4 API format (nodes array).
    """
    # Check which format we have
    nodes = zap.get("nodes", [])
    steps = zap.get("steps", [])
    
    processed_steps = []
    apps_used = set()
    
    if nodes:
        # V4 API format with nodes
        for i, node in enumerate(nodes):
            processed_step = process_v4_node(node, i)
            if processed_step["app_key"] not in ["unknown", "branching"]:
                apps_used.add(processed_step["app_key"])
            processed_steps.append(processed_step)
    elif steps:
        # V2 API format with steps
        for i, step in enumerate(steps):
            action = step.get("action", "")
            app_key, action_type = extract_app_from_action(action)
            
            if app_key != "zapier_internal":
                apps_used.add(app_key)
            
            processed_step = {
                "index": i + 1,
                "title": step.get("title", f"Step {i + 1}"),
                "action_raw": action,
                "app": format_app_name(app_key),
                "app_key": app_key,
                "action_type": format_action_name(action_type),
                "authentication": step.get("authentication"),
                "inputs": step.get("inputs", {}),
            }
            
            # Detect step type
            title_lower = processed_step["title"].lower()
            if i == 0:
                processed_step["step_type"] = "trigger"
            elif "filter" in title_lower or app_key == "filter":
                processed_step["step_type"] = "filter"
            elif "path" in title_lower or app_key == "paths":
                processed_step["step_type"] = "path"
            elif "code" in title_lower or app_key == "code":
                processed_step["step_type"] = "code"
            elif "delay" in title_lower or app_key == "delay":
                processed_step["step_type"] = "delay"
            else:
                processed_step["step_type"] = "action"
            
            processed_steps.append(processed_step)
    
    # Get zap ID (handle UUID format)
    zap_id_raw = zap.get("id", "")
    if isinstance(zap_id_raw, str) and zap_id_raw.startswith("00000000-"):
        zap_id = int(zap_id_raw.split("-")[-1])
    else:
        zap_id = int(zap_id_raw) if zap_id_raw else 0
    
    # Determine folder
    title = zap.get("title") or "Untitled"
    folder = get_folder_for_zap(zap_id, title)
    
    # Get state (v4 uses 'state', v2 uses 'is_enabled')
    is_enabled = zap.get("is_enabled", False)
    if "state" in zap:
        is_enabled = zap["state"] == "on"
    
    # Build editor URL
    editor_url = zap.get("links", {}).get("html_editor")
    if not editor_url and zap_id:
        editor_url = f"https://zapier.com/editor/{zap_id}"
    
    return {
        "id": zap_id,
        "id_raw": zap_id_raw,
        "title": title,
        "description": zap.get("description", ""),
        "is_enabled": is_enabled,
        "state": zap.get("state", "on" if is_enabled else "off"),
        "last_successful_run": zap.get("last_successful_run_date") or zap.get("last_live_at"),
        "updated_at": zap.get("updated_at") or zap.get("lastchanged"),
        "editor_url": editor_url,
        "steps_count": len(processed_steps),
        "steps": processed_steps,
        "apps": list(set(format_app_name(a) for a in sorted(apps_used) if format_app_name(a))),
        "apps_keys": list(apps_used),
        "folder": folder,
        "trigger_app": processed_steps[0]["app"] if processed_steps else None,
        "trigger_event": processed_steps[0].get("action_display") or processed_steps[0].get("title") if processed_steps else None,
    }


def generate_inventory(zaps: List[Dict]) -> Dict:
    """Generate inventory from processed zaps."""
    processed = [process_zap(z) for z in zaps]
    
    active = [z for z in processed if z["is_enabled"]]
    disabled = [z for z in processed if not z["is_enabled"]]
    
    # Categorize
    def categorize(title: str) -> str:
        title_lower = title.lower()
        if "demo" in title_lower or "inbound" in title_lower:
            return "sales"
        if "arr" in title_lower or "target" in title_lower:
            return "finance"
        if "intercom" in title_lower:
            return "communication"
        if "delivery" in title_lower or "log" in title_lower and "s3" in title_lower:
            return "delivery"
        if "landscape" in title_lower or "download" in title_lower:
            return "marketing"
        if "deal" in title_lower:
            return "sales"
        if "product" in title_lower:
            return "product"
        return "other"
    
    for z in processed:
        z["category"] = categorize(z["title"])
    
    return {
        "extracted_at": datetime.now().isoformat(),
        "source": "Zapier Workflow API v2",
        "total": len(processed),
        "active": len(active),
        "disabled": len(disabled),
        "zaps": processed,
        "active_by_category": {
            cat: [z for z in active if z["category"] == cat]
            for cat in ["sales", "finance", "communication", "delivery", "marketing", "product", "other"]
        },
    }


# ============================================================================
# README Generation
# ============================================================================

def generate_readme(zap: Dict, include_inputs: bool = False) -> str:
    """
    Generate comprehensive README documentation for a zap.
    
    Args:
        zap: Processed zap data from process_zap()
        include_inputs: Whether to include detailed input mappings (may contain sensitive data)
    
    Returns:
        Markdown README content
    """
    # Header
    status = "✅ Active (ON)" if zap["is_enabled"] else "⏸️ Paused (OFF)"
    updated = zap.get("updated_at", "")
    if updated:
        try:
            dt = datetime.fromisoformat(updated.replace("Z", "+00:00"))
            updated_str = dt.strftime("%B %d, %Y")
        except:
            updated_str = updated
    else:
        updated_str = "Unknown"
    
    last_run = zap.get("last_successful_run", "")
    if last_run:
        try:
            dt = datetime.fromisoformat(last_run.replace("Z", "+00:00"))
            last_run_str = dt.strftime("%B %d, %Y at %H:%M UTC")
        except:
            last_run_str = last_run
    else:
        last_run_str = "Never / Unknown"
    
    # Build title from folder name if available
    folder = zap.get("folder", "")
    if folder:
        display_title = folder.replace("_", " ").title() + " Automation"
    else:
        display_title = zap["title"]
    
    readme = f"""# {display_title}

> **Status**: {status}  
> **Zap ID**: {zap['id']}  
> **Steps**: {zap['steps_count']}  
> **Last Modified**: {updated_str}  
> **Last Successful Run**: {last_run_str}  
> **Editor**: [Open in Zapier]({zap.get('editor_url', '#')})

## Table of Contents
1. [What This Zap Does](#what-this-zap-does)
2. [Apps Used](#apps-used)
3. [Flow Architecture](#flow-architecture)
4. [Step-by-Step Breakdown](#step-by-step-breakdown)
5. [Troubleshooting](#troubleshooting)
6. [How to Modify](#how-to-modify)

---

## What This Zap Does

"""
    
    # Auto-generate description based on apps and steps
    if zap["steps"]:
        trigger = zap["steps"][0]
        last_step = zap["steps"][-1]
        
        readme += f"""This automation is triggered by **{trigger['app']}** and performs {len(zap['steps']) - 1} subsequent actions.

**Trigger**: {trigger['title']}
"""
        
        # Describe main flow
        action_apps = [s['app'] for s in zap['steps'][1:] if s['step_type'] == 'action']
        if action_apps:
            unique_apps = list(dict.fromkeys(action_apps))
            readme += f"\n**Main Actions**: {' → '.join(unique_apps)}\n"
    
    readme += """
---

## Apps Used

"""
    
    # Apps table
    readme += "| App | Usage in Zap |\n"
    readme += "|-----|-------------|\n"
    
    app_usage = {}
    for step in zap.get("steps", []):
        app = step["app"]
        if app not in app_usage:
            app_usage[app] = []
        app_usage[app].append(step["title"])
    
    for app, usages in app_usage.items():
        usage_summary = f"{len(usages)} step(s): {', '.join(usages[:3])}"
        if len(usages) > 3:
            usage_summary += f" +{len(usages) - 3} more"
        readme += f"| {app} | {usage_summary} |\n"
    
    readme += """
---

## Flow Architecture

"""
    
    # Build ASCII flow diagram
    readme += "```\n"
    
    steps = zap.get("steps", [])
    if steps:
        # Group steps by type for cleaner diagram
        current_section = None
        
        for i, step in enumerate(steps):
            step_type = step.get("step_type", "action")
            
            # Determine section
            if i == 0:
                section = "TRIGGER"
            elif step_type in ["filter", "path"]:
                section = "LOGIC"
            elif step_type == "code":
                section = "PROCESSING"
            else:
                section = "ACTIONS"
            
            if section != current_section:
                if current_section:
                    readme += "└─────────────────────────────────────────────────────────────────┘\n"
                    readme += "                              │\n"
                    readme += "                              ▼\n"
                current_section = section
                readme += f"┌─────────────────────────────────────────────────────────────────┐\n"
                readme += f"│{section:^65}│\n"
            
            # Truncate long titles
            title_display = step['title'][:55] + "..." if len(step['title']) > 55 else step['title']
            readme += f"│  {i + 1}. {title_display:<60}│\n"
        
        if current_section:
            readme += "└─────────────────────────────────────────────────────────────────┘\n"
    
    readme += "```\n"
    
    readme += """
---

## Step-by-Step Breakdown

"""
    
    # Detailed step breakdown
    for step in zap.get("steps", []):
        step_icon = {
            "trigger": "⚡",
            "filter": "🔀",
            "path": "🔀",
            "code": "💻",
            "delay": "⏰",
            "action": "▶️",
            "search": "🔍",
            "search_or_create": "🔍",
        }.get(step.get("step_type", "action"), "▶️")
        
        # Handle both v2 (action_type) and v4 (action_display) formats
        action_name = step.get('action_display') or step.get('action_type') or step.get('action') or 'Action'
        
        readme += f"""### Step {step['index']}: {step['title']}

| Property | Value |
|----------|-------|
| **Type** | {step_icon} {step.get('step_type', 'action').title()} |
| **App** | {step['app']} |
| **Action** | {action_name} |

"""
        
        # Include inputs if requested and they exist
        if include_inputs and step.get("inputs"):
            readme += "**Input Mappings**:\n\n"
            readme += "| Field | Value |\n"
            readme += "|-------|-------|\n"
            for key, value in step["inputs"].items():
                # Sanitize value (truncate if too long, escape pipes)
                value_str = str(value)[:80]
                value_str = value_str.replace("|", "\\|")
                readme += f"| `{key}` | {value_str} |\n"
            readme += "\n"
    
    readme += """---

## Troubleshooting

### Common Issues

#### Zap Not Triggering

**Check**:
1. Verify the trigger app connection is active
2. Check if the trigger event actually occurred
3. Review Zap history for filtered out runs

#### Step Errors

**Check**:
1. Verify app authentication is current
2. Check if required fields have values
3. Review error message in Zap history

### Viewing Zap History

1. Open [Zap Editor]({editor_url})
2. Click "Zap runs" in left sidebar
3. Review individual runs for errors

---

## How to Modify

### Editing Steps

1. Open the Zap in Zapier Editor
2. Click on the step you want to modify
3. Update the configuration
4. Test the step
5. Publish the changes

### Adding New Steps

1. Click the "+" button between steps
2. Search for the app you want to add
3. Configure the action
4. Map fields from previous steps
5. Test and publish

### Changing Trigger

⚠️ **Warning**: Changing the trigger may require re-mapping all subsequent steps.

1. Click on the trigger step
2. Select new trigger event
3. Reconfigure trigger settings
4. Review and update all field mappings
5. Test entire Zap before publishing

---

## Version History

| Date | Changes |
|------|---------|
| {updated_date} | Last modified |
| - | Documentation auto-generated |

---

*This documentation was auto-generated from Zapier API data.*
*Last updated: {now}*
""".format(
        editor_url=zap.get('editor_url', '#'),
        updated_date=updated_str,
        now=datetime.now().strftime("%Y-%m-%d %H:%M")
    )
    
    return readme


def save_readme(zap: Dict, output_dir: Path = None, include_inputs: bool = False) -> Path:
    """
    Generate and save README for a zap.
    
    Args:
        zap: Processed zap data
        output_dir: Override output directory (otherwise uses zap's folder)
        include_inputs: Whether to include detailed input mappings
    
    Returns:
        Path to saved README file
    """
    readme_content = generate_readme(zap, include_inputs=include_inputs)
    
    # Determine output path
    if output_dir:
        folder_path = output_dir
    elif zap.get("folder"):
        folder_path = ZAPIER_ROOT / zap["folder"]
    else:
        # Create folder from sanitized title
        folder_name = re.sub(r'[^\w\s-]', '', zap["title"].lower())
        folder_name = re.sub(r'[-\s]+', '_', folder_name)
        folder_path = ZAPIER_ROOT / folder_name
    
    folder_path.mkdir(parents=True, exist_ok=True)
    readme_path = folder_path / "README.md"
    
    with open(readme_path, "w") as f:
        f.write(readme_content)
    
    return readme_path


def generate_embedded_code_readme(folder: str, config: Dict) -> str:
    """
    Generate README for embedded Code by Zapier steps.
    
    Args:
        folder: Documentation folder name
        config: Configuration from EMBEDDED_CODE_FOLDERS
    
    Returns:
        Markdown README content
    """
    parent_name = config.get("parent_name", "Unknown")
    step_name = config.get("step_name", folder.replace("_", " ").title())
    code_file = config.get("code_file", "")
    
    readme = f"""# {step_name}

> **Type**: Code by Zapier (embedded step)  
> **Parent Zap**: [{parent_name}](../{parent_name}/README.md)  
> **Parent Zap ID**: {config.get('parent_zap_id', 'Unknown')}  

## Overview

This is a **Code by Zapier** action embedded in the [{parent_name}](../{parent_name}/README.md) automation.

The code logic is maintained separately for version control and testing.

---

## Code Location

"""
    
    if code_file:
        readme += f"**Source File**: [`{code_file}`](../../{code_file})\n\n"
    
    readme += f"""
---

## Purpose

{step_name} is responsible for:

- [Document the main functionality]
- [Add business logic description]
- [Describe inputs/outputs]

---

## Input Variables

| Variable | Type | Description |
|----------|------|-------------|
| *Document inputs from Zapier* | - | - |

---

## Output Variables

| Variable | Type | Description |
|----------|------|-------------|
| *Document outputs to Zapier* | - | - |

---

## How to Update

1. Edit the Python code in the source file
2. Test locally with the test script (if available)
3. Copy updated code to Zapier Code by Zapier step
4. Test in Zapier with sample data
5. Publish the parent Zap

---

## Related Documentation

- [{parent_name}](../{parent_name}/README.md) - Parent automation
"""
    
    return readme


def document_all_zaps(zaps: List[Dict], folders: List[str] = None) -> Dict[str, Path]:
    """
    Generate documentation for multiple zaps and embedded code steps.
    
    Args:
        zaps: List of processed zap data
        folders: Optional list of folder names to document (None = all mapped zaps)
    
    Returns:
        Dict mapping folder names to README paths
    """
    results = {}
    
    # Document standalone zaps
    for zap in zaps:
        folder = zap.get("folder")
        
        # Skip if no folder mapping
        if not folder:
            continue
        
        # Skip if not in requested folders
        if folders and folder not in folders:
            continue
        
        try:
            readme_path = save_readme(zap)
            results[folder] = readme_path
            print(f"  ✓ {folder}: {readme_path}")
        except Exception as e:
            print(f"  ✗ {folder}: {e}")
            results[folder] = None
    
    # Document embedded code steps
    for folder, config in EMBEDDED_CODE_FOLDERS.items():
        if folders and folder not in folders:
            continue
        
        # Skip if already documented as zap
        if folder in results:
            continue
        
        try:
            readme_content = generate_embedded_code_readme(folder, config)
            folder_path = ZAPIER_ROOT / folder
            folder_path.mkdir(parents=True, exist_ok=True)
            readme_path = folder_path / "README.md"
            
            with open(readme_path, "w") as f:
                f.write(readme_content)
            
            results[folder] = readme_path
            print(f"  ✓ {folder}: {readme_path} (embedded code)")
        except Exception as e:
            print(f"  ✗ {folder}: {e}")
            results[folder] = None
    
    return results


def print_documentation_status():
    """Print status of all documentation folders."""
    print("\n=== Documentation Folder Status ===\n")
    
    # Check mapped zaps
    print("Standalone Zaps:")
    for zap_id, folder in ZAP_FOLDER_MAP.items():
        if folder:
            folder_path = ZAPIER_ROOT / folder
            has_readme = (folder_path / "README.md").exists()
            status = "✓" if has_readme else "○"
            print(f"  {status} {folder} (ID: {zap_id})")
    
    # Check embedded code
    print("\nEmbedded Code Steps:")
    for folder, config in EMBEDDED_CODE_FOLDERS.items():
        folder_path = ZAPIER_ROOT / folder
        has_readme = (folder_path / "README.md").exists()
        status = "✓" if has_readme else "○"
        parent = config.get("parent_name", "?")
        print(f"  {status} {folder} (in {parent})")
    
    # Check unmapped folders
    print("\nUnmapped Folders:")
    for folder in UNMAPPED_FOLDERS:
        folder_path = ZAPIER_ROOT / folder
        has_readme = (folder_path / "README.md").exists()
        status = "?" if has_readme else "○"
        print(f"  {status} {folder} (needs manual mapping)")
    
    # Check asset folders
    print("\nAsset Folders:")
    for folder in ASSET_FOLDERS:
        folder_path = ZAPIER_ROOT / folder
        exists = folder_path.exists()
        status = "📁" if exists else "○"
        print(f"  {status} {folder}")


# ============================================================================
# CLI
# ============================================================================

def get_access_token() -> Optional[str]:
    """Get access token from environment or saved tokens."""
    access_token = os.getenv("ZAPIER_ACCESS_TOKEN")
    
    if not access_token:
        tokens = load_tokens()
        if tokens:
            access_token = tokens.get("access_token")
    
    return access_token


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Zapier Workflow API Client - Fetch zaps and generate documentation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python zapier_api.py --setup                    # Initial OAuth setup
  python zapier_api.py --fetch                    # Fetch all zaps with steps
  python zapier_api.py --document                 # Generate READMEs for all mapped zaps
  python zapier_api.py --document --folder demo_requests  # Generate README for specific folder
  python zapier_api.py --list-mapped              # Show zap-to-folder mappings
  python zapier_api.py --runs --zap-id 262386682  # Fetch run history for specific zap
        """
    )
    
    # Authentication
    auth_group = parser.add_argument_group("Authentication")
    auth_group.add_argument("--setup", action="store_true", help="Run OAuth setup flow")
    auth_group.add_argument("--refresh", action="store_true", help="Refresh access token")
    auth_group.add_argument("--client-id", type=str, help="OAuth client ID")
    auth_group.add_argument("--client-secret", type=str, help="OAuth client secret")
    
    # Fetching
    fetch_group = parser.add_argument_group("Fetching Data")
    fetch_group.add_argument("--fetch", action="store_true", help="Fetch all zaps with step details")
    fetch_group.add_argument("--runs", action="store_true", help="Fetch zap runs/execution history")
    fetch_group.add_argument("--zap-id", type=str, help="Specific zap ID for --runs or --document")
    fetch_group.add_argument("--output", type=str, default="zaps_api_export.json", help="Output filename")
    
    # Documentation
    doc_group = parser.add_argument_group("Documentation")
    doc_group.add_argument("--document", action="store_true", help="Generate README documentation")
    doc_group.add_argument("--folder", type=str, help="Specific folder to document (e.g., demo_requests)")
    doc_group.add_argument("--folders", type=str, help="Comma-separated list of folders to document")
    doc_group.add_argument("--active-only", action="store_true", help="Only document active (state=on) zaps")
    doc_group.add_argument("--include-inputs", action="store_true", help="Include input mappings in docs (may contain sensitive data)")
    doc_group.add_argument("--list-mapped", action="store_true", help="Show zap-to-folder mappings")
    doc_group.add_argument("--status", action="store_true", help="Show documentation status for all folders")
    doc_group.add_argument("--from-cache", action="store_true", help="Use cached zap data instead of fetching")
    doc_group.add_argument("--from-file", type=str, help="Load zaps from specific JSON file (v4 export)")
    
    args = parser.parse_args()
    
    # Get credentials
    client_id = args.client_id or os.getenv("ZAPIER_CLIENT_ID")
    client_secret = args.client_secret or os.getenv("ZAPIER_CLIENT_SECRET")
    
    # ========== SETUP ==========
    if args.setup:
        if not client_id or not client_secret:
            print("Error: --client-id and --client-secret required for setup")
            print("Or set ZAPIER_CLIENT_ID and ZAPIER_CLIENT_SECRET env vars")
            sys.exit(1)
        
        tokens = run_oauth_flow(client_id, client_secret)
        save_tokens(tokens)
        
        print("\n=== Setup Complete ===")
        print(f"Access Token: {tokens.get('access_token', '')[:20]}...")
        print(f"Refresh Token: {tokens.get('refresh_token', '')[:20]}...")
        print(f"\nTokens saved. You can now run: python zapier_api.py --fetch")
        return
    
    # ========== REFRESH TOKEN ==========
    if args.refresh:
        tokens = load_tokens()
        if not tokens or "refresh_token" not in tokens:
            print("Error: No refresh token found. Run --setup first.")
            sys.exit(1)
        
        if not client_id or not client_secret:
            print("Error: Client credentials required for refresh")
            sys.exit(1)
        
        new_tokens = refresh_access_token(
            client_id, client_secret, tokens["refresh_token"]
        )
        save_tokens(new_tokens)
        print("Token refreshed successfully!")
        return
    
    # ========== LIST MAPPED ZAPS ==========
    if args.list_mapped:
        print("\n=== Zap-to-Folder Mappings ===\n")
        
        print("By Zap ID:")
        for zap_id, folder in sorted(ZAP_FOLDER_MAP.items()):
            if folder:  # Skip None entries
                print(f"  {zap_id}: {folder}")
        
        print("\nBy Title Pattern:")
        for pattern, folder in sorted(ZAP_TITLE_PATTERNS.items(), key=lambda x: x[1]):
            print(f"  {folder}: {pattern}")
        
        print(f"\nDocumentation root: {ZAPIER_ROOT}")
        return
    
    # ========== DOCUMENTATION STATUS ==========
    if args.status:
        print_documentation_status()
        return
    
    # ========== FETCH ZAPS ==========
    if args.fetch:
        access_token = get_access_token()
        
        if not access_token:
            print("Error: No access token found.")
            print("Run --setup first or set ZAPIER_ACCESS_TOKEN env var")
            sys.exit(1)
        
        client = ZapierAPIClient(access_token)
        
        print("\n=== Fetching Zaps from Zapier API v2 ===\n")
        zaps = client.get_all_zaps(expand="steps")
        
        print(f"\nFetched {len(zaps)} zaps")
        
        # Generate inventory with processed data
        inventory = generate_inventory(zaps)
        
        # Save raw and processed data
        DATA_DIR.mkdir(exist_ok=True)
        
        # Save processed inventory
        output_path = DATA_DIR / args.output
        with open(output_path, "w") as f:
            json.dump(inventory, f, indent=2)
        print(f"Saved processed data to {output_path}")
        
        # Summary
        print(f"\n=== Summary ===")
        print(f"Total: {inventory['total']}")
        print(f"Active: {inventory['active']}")
        print(f"Disabled: {inventory['disabled']}")
        
        # Show mapped zaps
        mapped_zaps = [z for z in inventory['zaps'] if z.get('folder')]
        if mapped_zaps:
            print(f"\n=== Mapped to Documentation Folders ({len(mapped_zaps)}) ===")
            for z in mapped_zaps:
                status = "✓" if z["is_enabled"] else "○"
                print(f"  {status} {z['folder']}: {z['title'][:50]}")
        
        print(f"\nBy Category:")
        for cat, zaps_list in inventory["active_by_category"].items():
            if zaps_list:
                print(f"  {cat}: {len(zaps_list)}")
        
        return
    
    # ========== GENERATE DOCUMENTATION ==========
    if args.document:
        print("\n=== Generating Zap Documentation ===\n")
        
        # Get zap data
        if args.from_file:
            # Load from specified file (v4 export format)
            file_path = Path(args.from_file)
            if not file_path.exists():
                print(f"Error: File not found: {file_path}")
                sys.exit(1)
            
            with open(file_path) as f:
                raw_zaps = json.load(f)
            
            # Handle both array and object formats
            if isinstance(raw_zaps, list):
                zaps = [process_zap(z) for z in raw_zaps]
            else:
                zaps = [process_zap(z) for z in raw_zaps.get("zaps", raw_zaps.get("results", []))]
            
            print(f"Loaded {len(zaps)} zaps from {file_path}")
            
        elif args.from_cache:
            # Load from cached file
            cache_file = DATA_DIR / "zaps_api_export.json"
            if not cache_file.exists():
                # Try v4 export file
                cache_file = DATA_DIR / "zaps_full_details.json"
            if not cache_file.exists():
                print(f"Error: Cache file not found")
                print("Run --fetch first, use --from-file, or export via browser")
                sys.exit(1)
            
            with open(cache_file) as f:
                data = json.load(f)
            
            # Handle both formats
            if isinstance(data, list):
                zaps = [process_zap(z) for z in data]
            else:
                zaps = data.get("zaps", [])
                if zaps and "steps" not in zaps[0] and "nodes" not in zaps[0]:
                    # Already processed
                    pass
                else:
                    zaps = [process_zap(z) for z in zaps]
            
            print(f"Loaded {len(zaps)} zaps from cache")
        
        # Filter to active only if requested
        if args.active_only:
            before_count = len(zaps)
            zaps = [z for z in zaps if z.get("is_enabled") or z.get("state") == "on"]
            print(f"Filtered to {len(zaps)} active zaps (from {before_count})")
        else:
            # Fetch fresh data
            access_token = get_access_token()
            
            if not access_token:
                print("Error: No access token found.")
                print("Run --setup first or set ZAPIER_ACCESS_TOKEN env var")
                sys.exit(1)
            
            client = ZapierAPIClient(access_token)
            print("Fetching zaps from API...")
            raw_zaps = client.get_all_zaps(expand="steps")
            zaps = [process_zap(z) for z in raw_zaps]
            print(f"Fetched {len(zaps)} zaps")
        
        # Determine which folders to document
        target_folders = None
        if args.folder:
            target_folders = [args.folder]
        elif args.folders:
            target_folders = [f.strip() for f in args.folders.split(",")]
        elif args.zap_id:
            # Find the zap and its folder
            zap_id_int = int(args.zap_id)
            for zap in zaps:
                if zap.get("id") == zap_id_int:
                    if zap.get("folder"):
                        target_folders = [zap["folder"]]
                    else:
                        print(f"Warning: Zap {args.zap_id} has no folder mapping")
                        # Create README in temp folder
                        save_readme(zap, output_dir=DATA_DIR / "unmapped")
                        print(f"  Saved to: {DATA_DIR / 'unmapped' / 'README.md'}")
                        return
                    break
        
        # Generate documentation
        print("\nGenerating READMEs...")
        results = document_all_zaps(zaps, folders=target_folders)
        
        # Summary
        successful = sum(1 for v in results.values() if v)
        print(f"\n=== Documentation Complete ===")
        print(f"Generated: {successful} README files")
        
        if target_folders:
            missing = set(target_folders) - set(results.keys())
            if missing:
                print(f"\nNot found (no matching zap): {', '.join(missing)}")
        
        return
    
    # ========== FETCH RUNS ==========
    if args.runs:
        access_token = get_access_token()
        
        if not access_token:
            print("Error: No access token found.")
            print("Run --setup first or set ZAPIER_ACCESS_TOKEN env var")
            sys.exit(1)
        
        client = ZapierAPIClient(access_token)
        DATA_DIR.mkdir(exist_ok=True)
        
        if args.zap_id:
            print(f"\n=== Fetching Runs for Zap {args.zap_id} ===\n")
            try:
                runs = client.get_zap_runs(args.zap_id)
                output_path = DATA_DIR / f"zap_runs_{args.zap_id}.json"
                with open(output_path, "w") as f:
                    json.dump(runs, f, indent=2)
                print(f"Saved runs to {output_path}")
                
                if isinstance(runs, list):
                    print(f"Total runs: {len(runs)}")
                elif "data" in runs:
                    print(f"Total runs: {len(runs['data'])}")
            except Exception as e:
                print(f"Error fetching runs: {e}")
                sys.exit(1)
        else:
            print("\n=== Fetching Runs for All Active Zaps ===\n")
            
            zaps = client.get_all_zaps(expand="steps")
            active_zaps = [z for z in zaps if z.get("is_enabled", False)]
            
            print(f"Found {len(active_zaps)} active zaps")
            
            all_runs = {}
            for zap in active_zaps:
                zap_id = zap.get("id")
                zap_title = zap.get("title", "Untitled")
                print(f"  Fetching runs for: {zap_title[:50]}...")
                
                try:
                    runs = client.get_zap_runs(zap_id)
                    all_runs[zap_id] = {
                        "title": zap_title,
                        "runs": runs,
                    }
                except Exception as e:
                    print(f"    Warning: Could not fetch runs - {e}")
                    all_runs[zap_id] = {
                        "title": zap_title,
                        "error": str(e),
                    }
            
            output_path = DATA_DIR / "all_zap_runs.json"
            with open(output_path, "w") as f:
                json.dump({
                    "fetched_at": datetime.now().isoformat(),
                    "zaps": all_runs,
                }, f, indent=2)
            
            print(f"\nSaved all runs to {output_path}")
        
        return
    
    # No action specified
    parser.print_help()


if __name__ == "__main__":
    main()
