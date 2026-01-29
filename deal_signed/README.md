# Deal Signed Automation

> **Status**: ✅ Active (ON)  
> **Location**: Internal Operations  
> **Last Modified**: Oct 1, 2025  
> **Owner**: Dominik Vacikar  

## Table of Contents
1. [What This Zap Does](#what-this-zap-does)
2. [Why This Exists](#why-this-exists)
3. [Flow Architecture](#flow-architecture)
4. [Step-by-Step Breakdown](#step-by-step-breakdown)
5. [Code Action: Product Mapping](#code-action-product-mapping)
6. [Troubleshooting](#troubleshooting)

---

## What This Zap Does

When a deal is marked as **"Won"** in HubSpot, this Zap:

1. **Extracts** deal data (products, amount, owner)
2. **Maps** product IDs to human-readable names
3. **Logs** the win to Google Sheets (finance tracking)
4. **Celebrates** with a Slack notification to the team
5. **Prepares** renewal data (increments deal name: "Y1" → "Y2")

---

## Why This Exists

### Business Problem Solved
- **Visibility**: Team wasn't aware when deals closed
- **Tracking**: Finance needed real-time ARR updates
- **Renewal Prep**: Manual work to set up renewal deals
- **Reporting**: Data scattered across systems

### Value Delivered
- Real-time Slack celebrations (team morale)
- Automated finance logging (no manual entry)
- Renewal setup automation (saves 10 min/deal)
- Consistent data across HubSpot and Sheets

---

## Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         TRIGGER                                  │
│  HubSpot → Deal Stage Changed to "Won"                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DATA EXTRACTION                            │
│  1. Get deal properties (amount, products, owner)               │
│  2. Get associated company                                      │
│  3. Get deal owner info                                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     CODE: PRODUCT MAPPING                       │
│  4. Map product IDs to names                                    │
│  5. Map owner IDs to names                                      │
│  6. Increment deal name for renewal (Y1 → Y2)                   │
│  7. Clean company name (remove " - Y1")                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      LOGGING & NOTIFICATIONS                    │
│  8. Google Sheets: Log to Finance tracker                       │
│  9. Slack: Post win celebration                                 │
│  10. (Optional) Update HubSpot with renewal prep                │
└─────────────────────────────────────────────────────────────────┘
```

---

## Step-by-Step Breakdown

### Trigger: Deal Stage = Won
**App**: HubSpot  
**Event**: Deal property changed  
**Condition**: `dealstage` = `closedwon`  
**Pipeline**: Sales (default)

### Step 2: Get Deal Properties
**App**: HubSpot  
**Action**: Get Deal  
**Properties Retrieved**:
- `dealname`
- `amount`
- `hubspot_owner_id`
- `products_frontend`
- `products_programmatic`
- `closedate`

### Step 3: Get Associated Company
**App**: HubSpot  
**Action**: Find Associated Company  
**Purpose**: Get company name for notifications

### Step 4: Code Action - Product Mapping
**File**: [`zapier_deal_signed_map.md`](../../hubspot_automations/scripts/hs_zapier_code/deal_signed/zapier_deal_signed_map.md)

See [Code Action: Product Mapping](#code-action-product-mapping) for details.

### Step 5: Google Sheets Logging
**App**: Google Sheets  
**Action**: Create Spreadsheet Row  
**Spreadsheet**: Finance tracker  
**Data Logged**:
- Company name
- Deal amount
- Products purchased
- Contract date
- Deal owner

### Step 6: Slack Notification
**App**: Slack  
**Channel**: #sales-wins  
**Message Format**:
```
🎉 DEAL WON! 🎉

Company: Acme Corp
Amount: €50,000
Products: Company Database, People Database, API
Owner: Marco Squarci

View Deal: [HubSpot Link]
```

---

## Code Action: Product Mapping

This code action transforms HubSpot internal IDs into human-readable values.

### Input Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `products_frontend` | Frontend product IDs | `web_app,bulk_data` |
| `products_programmatic` | Data product IDs | `company_database,people_database` |
| `deal_name` | Current deal name | `Acme Corp - Y1` |
| `company_name` | Associated company | `Acme Corp - Y1` |
| `deal_owner` | Owner HubSpot ID | `35673999` |

### Output Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `Owner_deal` | Human-readable owner | `Marco Squarci` |
| `web_app` | "Web App" if selected | `Web App` |
| `bulk_data` | "Bulk Data" if selected | `Bulk Data` |
| `api` | "API" if selected | `API` |
| `company_database` | "Company Database" if selected | `Company Database` |
| `people_database` | "People Database" if selected | `People Database` |
| `investor_database` | "Investor Database" if selected | |
| `talent_signals` | "Talent Signals" if selected | |
| `interest_signals` | "Interest Signals" if selected | |
| `revenue_signals` | "Revenue Signals" if selected | |
| `linkedin_company_profiles` | "LinkedIn - Company Profiles" if selected | |
| `linkedin_people_profiles` | "LinkedIn - People Profiles" if selected | |
| `g2.com` | "G2.com" if selected | |
| `trustpilot` | "Trustpilot" if selected | |
| `capterra` | "Capterra" if selected | |
| `chrome_extensions` | "Chrome Extensions" if selected | |
| `clickstream` | "Clickstream" if selected | |
| `company_data` | Cleaned company name | `Acme Corp` |
| `company_data_url` | URL-encoded company | `Acme%20Corp` |
| `incremented_deal_name` | Deal name for renewal | `Acme Corp - Y2` |

### Owner ID Mapping

```python
OWNER_MAPPING = {
    '35673999': 'Marco Squarci',
    '49928941': 'Dominik Vacikar',
    '77583320': 'Philipp Berhoerster',
    '200411144': 'Francisco Terpolilli',
    '713358197': 'Isabella Garcia Foster',
    '1509688330': 'David Looby'
}
```

### Deal Name Incrementing

Automatically prepares the deal name for renewal:

```python
import re

def increment_deal_name(deal_name):
    # "Company - Y1" → "Company - Y2"
    match = re.search(r"(.* - Y)(\d+)", deal_name)
    if match:
        prefix, number = match.groups()
        return f"{prefix}{int(number) + 1}"
    return deal_name
```

**Examples**:
- `Acme Corp - Y1` → `Acme Corp - Y2`
- `BigCo - Y3` → `BigCo - Y4`
- `No Year Deal` → `No Year Deal` (unchanged)

---

## Troubleshooting

### Products Not Mapped Correctly

**Symptom**: Product shows as blank in Slack/Sheets

**Check**:
1. Verify product ID in `products_frontend` or `products_programmatic`
2. Ensure ID matches exactly (case-sensitive)

**Known Product IDs**:
```
Frontend: web_app, bulk_data, api, n_a
Programmatic: company_database, people_database, investor_database,
              talent_signals, interest_signals, revenue_signals,
              linkedin_company_profiles, linkedin_people_profiles,
              g2.com, trustpilot, capterra, chrome_extensions,
              clickstream, legacy_clickstream_shopify, n_a
```

### Owner Not Recognized

**Symptom**: `Owner_deal` is blank

**Check**: Verify owner ID is in the mapping. Add new owners as needed.

### Deal Name Not Incrementing

**Symptom**: `incremented_deal_name` same as original

**Check**: Ensure deal name follows pattern `Company Name - Y{number}`

---

## Related Documentation

- [Deal Renewed](../deal_renewed/README.md) - Similar flow for renewals
- [ARR UPDATE](../arr_update/README.md) - Financial tracking
- [Demo Requests](../demo_requests/README.md) - Upstream lead flow
