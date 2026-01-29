# Product Import Data Requests

> **Status**: ✅ Active (ON)  
> **Location**: Leads  
> **Last Modified**: Sep 1, 2025  
> **Owner**: Dominik Vacikar  

## What This Zap Does

Handles **data import requests** from the Specter product:

1. **Receives** webhook when user requests data import
2. **Creates/Updates** HubSpot contact and deal
3. **Logs** request to Google Sheets
4. **Notifies** team via Slack

---

## Why This Exists

### Business Problem Solved
- Data import requests weren't tracked as leads
- Sales missed upsell opportunities
- No visibility into product usage signals

### Value Delivered
- Every import request becomes a sales signal
- Upsell opportunity identification
- Product usage tracking

---

## Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         TRIGGER                                  │
│  Webhook → Data Import Request from Product                     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DATA PREPARATION                           │
│  1. Parse webhook payload                                       │
│  2. Extract user info and import details                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    HUBSPOT ENRICHMENT                           │
│  3. Find/Create Contact                                         │
│  4. Find/Create Company                                         │
│  5. Create/Update Deal with import flag                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      LOGGING & NOTIFICATIONS                    │
│  6. Google Sheets: Log import request                           │
│  7. Slack: Notify #product-activity                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Trigger

**Type**: Webhook (Catch Hook)  
**Source**: Specter product backend  
**Event**: User requests data import

### Expected Payload

```json
{
  "email": "john@acme.com",
  "user_id": "usr_123",
  "import_type": "company_data",
  "record_count": 500,
  "timestamp": "2026-01-29T14:30:00Z"
}
```

---

## HubSpot Properties Set

| Property | Value |
|----------|-------|
| `data_import_requested` | true |
| `import_type` | From webhook |
| `import_record_count` | From webhook |
| `last_import_request_date` | Timestamp |

---

## Slack Notification

**Channel**: #product-activity

```
📊 Data Import Request

User: john@acme.com
Import Type: Company Data
Records: 500

View in HubSpot: [Link]
```

---

## Related Documentation

- [Product Sign Ups](../product_sign_ups/README.md) - Initial sign-up flow
- [Demo Requests](../demo_requests/README.md) - Form-based leads
