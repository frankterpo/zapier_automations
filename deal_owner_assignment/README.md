# Deal Owner Assignment

## Overview

| Property | Value |
|----------|-------|
| **Status** | Active (embedded in Demo Requests Zap) |
| **Type** | Code by Zapier action |
| **Last Modified** | Jan 2026 |

## Purpose

Automatically assigns HubSpot deal owners based on:
- Deal type (New Business, Re-attempting, Upsell)
- AUM (Assets Under Management) value
- Current owner status

## Business Rules

### 1. New Lead (Lead Type = "New Business")

| Condition | Assigned Owner |
|-----------|----------------|
| Default | Marco Squarci (35673999) |
| AUM < 200m | Philipp Berhoerster (77583320) |

### 2. Returning Lead (Lead Type = "Re-attempting")

| Condition | Assigned Owner |
|-----------|----------------|
| Default | Keep Former Deal Owner |
| Current owner in special list | Marco Squarci (35673999) |
| AUM < 200m | Philipp Berhoerster (77583320) |

**Special Owner IDs** (reassigned to Marco):
- 63630364
- 80911411
- 74169263
- 61798434

### 3. Existing Customer (Lead Type = "Upsell")

| Condition | Assigned Owner |
|-----------|----------------|
| Default | Keep Current Deal Owner |

## Code Implementation

**File**: [`zapier_deal_owner.py`](../../hubspot_automations/scripts/hs_zapier_code/assign_deal_owner/zapier_deal_owner.py)

```python
# Key constants
MARCO_SQUARCI = "35673999"
PHILIPP_BERHOERSTER = "77583320"
SPECIAL_OWNER_IDS = {"63630364", "80911411", "74169263", "61798434"}
SMALL_AUM_VALUES = {"<50m", "50m-200m"}

def assign_deal_owner(deal_type, current_owner_id, aum):
    # AUM-first logic: prioritize small AUM regardless of deal type
    if aum in SMALL_AUM_VALUES:
        return PHILIPP_BERHOERSTER
    
    if deal_type == "New Business":
        return MARCO_SQUARCI
    
    if deal_type == "Re-attempting":
        if current_owner_id in SPECIAL_OWNER_IDS:
            return MARCO_SQUARCI
        return current_owner_id or MARCO_SQUARCI
    
    if deal_type == "Upsell":
        return current_owner_id or MARCO_SQUARCI
    
    return MARCO_SQUARCI  # Default
```

## Input Variables

| Variable | Type | Description |
|----------|------|-------------|
| `deal_type` | String | "New Business", "Re-attempting", or "Upsell" |
| `current_owner_id` | String | HubSpot owner ID of current deal |
| `aum` | String | AUM value: "<50m", "50m-200m", "200m-500m", "500m+", "n/a" |
| `current_owner_name` | String | Optional: Current owner name for output |
| `deal_id` | String | HubSpot deal ID to update |
| `api_key` | String | HubSpot API key |

## Output Variables

| Variable | Type | Description |
|----------|------|-------------|
| `owner_id` | String | Assigned HubSpot owner ID |
| `owner_name` | String | Human-readable owner name |
| `assignment_reason` | String | Explanation for the assignment |
| `update_success` | Boolean | Whether HubSpot update succeeded |
| `update_message` | String | Success/error message |

## Zapier Setup

### Step 1: Add Code by Zapier Action
1. Select "Run Python"
2. Paste contents of `zapier_deal_owner.py`

### Step 2: Map Input Data

```json
{
  "deal_type": "{{lead_type}}",
  "current_owner_id": "{{hubspot_owner_id}}",
  "aum": "{{aum}}",
  "deal_id": "{{deal_id}}",
  "api_key": "{{env.HUBSPOT_API_KEY}}"
}
```

### Step 3: Use Output

In subsequent HubSpot actions:
```
Deal Owner ID: {{Code.owner_id}}
```

## Testing

Run the test script to verify logic:

```bash
cd hubspot_automations/scripts/hs_zapier_code/assign_deal_owner
python3 test_deal_owner.py
```

## Related Files

- [`zapier_deal_owner.py`](../../hubspot_automations/scripts/hs_zapier_code/assign_deal_owner/zapier_deal_owner.py) - Main script
- [`zapier_returning_lead_owner.py`](../../hubspot_automations/scripts/hs_zapier_code/assign_deal_owner/zapier_returning_lead_owner.py) - Extended version
- [`test_deal_owner.py`](../../hubspot_automations/scripts/hs_zapier_code/assign_deal_owner/test_deal_owner.py) - Test cases
- [`README.md`](../../hubspot_automations/scripts/hs_zapier_code/assign_deal_owner/README.md) - Original documentation
