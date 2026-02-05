# Zapier Workflow API Setup Guide

## Quick Start

```bash
# Step 1: Set your OAuth credentials
export ZAPIER_CLIENT_ID='your_client_id'
export ZAPIER_CLIENT_SECRET='your_client_secret'

# Step 2: Run OAuth setup (opens browser)
python zapier_api.py --setup

# Step 3: Fetch all zaps with full step details
python zapier_api.py --fetch

# Step 4: Generate README documentation for all mapped zaps
python zapier_api.py --document
```

## All Commands Reference

```bash
# Authentication
python zapier_api.py --setup                    # Initial OAuth setup
python zapier_api.py --refresh                  # Refresh expired token

# Fetching Data
python zapier_api.py --fetch                    # Fetch all zaps with step details
python zapier_api.py --runs --zap-id 262386682  # Fetch run history

# Documentation Generation
python zapier_api.py --document                 # Generate READMEs for all mapped zaps
python zapier_api.py --document --folder demo_requests  # Document specific folder
python zapier_api.py --document --folders "demo_requests,product_sign_ups"  # Multiple
python zapier_api.py --document --from-cache    # Use cached data (skip API call)
python zapier_api.py --document --include-inputs  # Include input mappings (sensitive)

# Status & Information
python zapier_api.py --status                   # Show documentation status
python zapier_api.py --list-mapped              # Show zap-to-folder mappings
python zapier_api.py --help                     # Full help
```

## Authentication Requirements

The Zapier Workflow API (`/v2/zaps` endpoint) requires **OAuth 2.0 authentication**.

### Step 1: Register an OAuth App

1. Go to https://developer.zapier.com/
2. Create a new integration (or use existing)
3. Navigate to **Embed → Settings → Credentials**
4. Note your `Client ID` and `Client Secret`

### Step 2: Configure OAuth Settings

In your Zapier Developer Platform app settings:

1. Go to **Embed → Settings → OAuth**
2. Add redirect URI: `http://localhost:8080/callback`
3. Request scopes:
   - `zap:read` - Read zap details
   - `zap:all` - Access all owned zaps

### Step 3: Run OAuth Flow

```bash
# Set credentials as environment variables
export ZAPIER_CLIENT_ID='your_client_id'
export ZAPIER_CLIENT_SECRET='your_client_secret'

# Run the setup (opens browser for authorization)
python zapier_api.py --setup
```

This will:
1. Open your browser to Zapier's authorization page
2. After you authorize, redirect to localhost
3. Exchange the code for access/refresh tokens
4. Save tokens to `.zapier_tokens.json`

### Step 4: Fetch Zaps

```bash
# Fetch all zaps with step details
python zapier_api.py --fetch

# Output saved to data/zaps_api_export.json
```

### Step 5: Fetch Zap Events/Runs (Optional)

```bash
# Fetch run history for a specific zap
python zapier_api.py --runs --zap-id YOUR_ZAP_ID

# Output saved to data/zap_runs_{id}.json
```

### Step 6: Generate Documentation

```bash
# Generate READMEs for all mapped zaps
python zapier_api.py --document

# Or document specific folders
python zapier_api.py --document --folder demo_requests
```

The documentation generator:
- Fetches full step details from the API
- Maps zaps to documentation folders
- Generates comprehensive README files with:
  - Status and metadata
  - Apps used table
  - ASCII flow diagram
  - Step-by-step breakdown
  - Troubleshooting guide

## Zap-to-Folder Mapping

The script automatically maps zaps to documentation folders based on:

1. **Explicit ID mapping** - Direct zap ID → folder mapping
2. **Title pattern matching** - Regex patterns match zap titles

### Currently Mapped Zaps

| Zap ID | Folder | Description |
|--------|--------|-------------|
| 262386682 | `demo_requests` | Main demo request flow |
| 268969745 | `product_sign_ups` | Product signup tracking |
| 300616653 | `auto_set_lifecycle` | Auto-set lifecycle stage |
| 266596665 | `intercom_bot_reply` | Bot conversation alerts |
| 207157349 | `intercom_demo_email` | Demo requests via chat |
| 247549034 | `sales_target_update` | Sales target tracking |
| 240869492 | `contacts_deals_associations` | CRM associations |
| 236426171 | `deal_renewed` | Renewal notifications |

### Embedded Code Steps

Some folders represent Code by Zapier steps embedded in other zaps:

| Folder | Parent Zap | Purpose |
|--------|------------|---------|
| `deal_owner_assignment` | demo_requests | Deal owner assignment logic |

### Adding New Mappings

Edit `ZAP_FOLDER_MAP` in `zapier_api.py`:

```python
ZAP_FOLDER_MAP = {
    YOUR_ZAP_ID: "your_folder_name",
    ...
}
```

### Token Refresh

If your token expires:

```bash
python zapier_api.py --refresh --client-id YOUR_ID --client-secret YOUR_SECRET
```

### Option 2: Manual Export (Simpler)

If OAuth is too complex, you can manually export zap data:

1. **From Zapier Dashboard**
   - Go to https://zapier.com/app/zaps
   - Use browser DevTools (F12 → Network tab)
   - Refresh the page and look for API calls to `/v2/zaps`
   - Copy the response JSON

2. **Save to Data File**
   ```bash
   # Paste the JSON into this file
   vim data/zaps_export_manual.json
   ```

3. **Process with Script**
   ```bash
   python process_manual_export.py data/zaps_export_manual.json
   ```

### Option 3: Browser Console Export

1. Go to https://zapier.com/app/zaps while logged in
2. Open browser DevTools (F12) → Console
3. Run this script:

```javascript
// Fetch all zaps from the current session
(async () => {
    const response = await fetch('https://zapier.com/api/v4/zaps?status=on&limit=100', {
        credentials: 'include'
    });
    const data = await response.json();
    console.log(JSON.stringify(data, null, 2));
    
    // Create downloadable file
    const blob = new Blob([JSON.stringify(data, null, 2)], {type: 'application/json'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'zapier_zaps_export.json';
    a.click();
})();
```

## Environment Variables

Add to your `.env` file:

```bash
# For OAuth flow
ZAPIER_CLIENT_ID=your_client_id
ZAPIER_CLIENT_SECRET=your_client_secret
ZAPIER_ACCESS_TOKEN=your_access_token

# Optional: AI Actions API (different from Workflow API)
ZAPIER_AI_ACTIONS_KEY=your_ai_actions_key
```

## AI Actions API (Different Purpose)

The AI Actions API key from https://actions.zapier.com/credentials/ is for **executing** pre-configured Zapier actions through AI, not for listing your zaps. It's a different product.

## Troubleshooting

### "Your app needs to be published"
The `/v2/zaps` endpoint requires your OAuth app to be a public integration. For internal tools, use the browser export method.

### Rate Limiting
The API is rate limited. See: https://docs.zapier.com/powered-by-zapier/api-reference/rate-limiting

### Token Expired
OAuth tokens expire. You'll need to refresh them periodically using the refresh token.

## Links

- Zapier API Docs: https://docs.zapier.com/powered-by-zapier/introduction
- Get Zaps Endpoint: https://docs.zapier.com/powered-by-zapier/api-reference/zaps/get-zaps-[v2]
- Developer Platform: https://developer.zapier.com/
