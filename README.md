# Zapier Automations Documentation

> Last Updated: January 29, 2026  
> Account: Dominik Vacikar Individual (Professional Plan)

## Overview

This documentation covers all **active** Zapier automations for Specter. Only active (ON) Zaps are documented here. Legacy and disabled Zaps are listed separately.

---

## Quick Navigation

### Critical Business Automations

| Zap | Purpose | Documentation |
|-----|---------|---------------|
| **Demo Requests** | Primary inbound lead processing | [README](demo_requests/README.md) |
| **Deal Signed** | Won deal notifications & finance logging | [README](deal_signed/README.md) |
| **Deal Renewed** | Renewal tracking & celebration | [README](deal_renewed/README.md) |
| **Product Sign Ups** | Self-serve signup tracking | [README](product_sign_ups/README.md) |
| **ARR UPDATE** | Real-time ARR tracking | [README](arr_update/README.md) |
| **SALES TARGET UPDATE** | Target progress tracking | [README](sales_target_update/README.md) |

### Communication Automations

| Zap | Purpose | Documentation |
|-----|---------|---------------|
| **Intercom Request / Slack** | Support request alerts | [README](intercom_request_slack/README.md) |
| **Intercom Demo Email / Slack** | Intercom demo request routing | [README](intercom_demo_email/README.md) |
| **Intercom Bot Reply / Slack** | Bot conversation alerts | [README](intercom_bot_reply/README.md) |

### HubSpot Data Automations

| Zap | Purpose | Documentation |
|-----|---------|---------------|
| **Auto-set: Previous Customer / Customer** | Lifecycle stage management | [README](auto_set_lifecycle/README.md) |
| **Contacts to Deals Associations** | Association creation | [README](contacts_deals_associations/README.md) |
| **Product Import Data Requests** | Import request tracking | [README](product_import_requests/README.md) |

---

## Architecture Overview

```
                    ┌──────────────┐
                    │   TRIGGERS   │
                    └──────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
   ┌─────────┐      ┌──────────┐     ┌──────────┐
   │ GetForm │      │ HubSpot  │     │ Intercom │
   │ Webhook │      │ Webhooks │     │ Messages │
   └────┬────┘      └────┬─────┘     └────┬─────┘
        │                │                 │
        └────────────────┼─────────────────┘
                         │
                         ▼
              ┌────────────────────┐
              │   PROCESSING       │
              │  • Formatter       │
              │  • Code by Zapier  │
              │  • Filters         │
              └────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
   ┌─────────┐     ┌──────────┐    ┌──────────┐
   │ HubSpot │     │  Slack   │    │  Sheets  │
   │   CRM   │     │  Alerts  │    │  Logging │
   └─────────┘     └──────────┘    └──────────┘
```

---

## Zap Categories

### Sales & CRM
Automations that process leads and manage the sales pipeline.

- **[Demo Requests](demo_requests/README.md)** - 76 steps, v117
  - Trigger: GetForm submission
  - Actions: HubSpot enrichment, lead classification, owner assignment
  - Notifications: Slack, Gmail

- **[Deal Signed](deal_signed/README.md)** - Active
  - Trigger: HubSpot deal → Won
  - Actions: Product mapping, finance logging
  - Notifications: Slack celebration

- **[Deal Renewed](deal_renewed/README.md)** - Active
  - Trigger: HubSpot deal → Renewed
  - Actions: Finance logging, renewal tracking
  - Notifications: Slack celebration

- **[Product Sign Ups](product_sign_ups/README.md)** - Active
  - Trigger: Webhook from product backend
  - Actions: HubSpot contact/company/deal creation
  - Notifications: Slack, Sheets logging

### Finance & Reporting
Automations that maintain financial tracking.

- **[ARR UPDATE](arr_update/README.md)** - Active
  - Trigger: HubSpot deal changes
  - Actions: ARR calculation, Sheets update

- **[SALES TARGET UPDATE](sales_target_update/README.md)** - Active
  - Trigger: HubSpot deal won
  - Actions: Target progress calculation

### Communication
Automations that route messages and alerts.

- **[Intercom Request / Slack](intercom_request_slack/README.md)** - Active
  - Trigger: Intercom conversation (support)
  - Actions: Slack notification

- **[Intercom Demo Email / Slack](intercom_demo_email/README.md)** - Active
  - Trigger: Intercom conversation (demo keywords)
  - Actions: Email + Slack notification

- **[Intercom Bot Reply / Slack](intercom_bot_reply/README.md)** - Active
  - Trigger: Intercom bot conversation
  - Actions: Slack notification

### Client Delivery Monitoring
Automations that monitor S3 bucket deliveries.

- Log Assure Delivery
- Log Underscore Delivery
- Log Expa Delivery
- Log Moonfire (S3) Delivery
- Log Omers Delivery
- Log STS Delivery
- Notify about missing delivery

### Landscape Downloads
23 Zaps handling landscape report download requests.

---

## Code by Zapier Scripts

All Python scripts used in Zapier are maintained in:

```
hubspot_automations/scripts/hs_zapier_code/
├── assign_deal_owner/
│   ├── zapier_deal_owner.py      # Deal owner assignment
│   └── zapier_returning_lead_owner.py
├── demo_request/
│   ├── zapier_classify_lead_type.py  # Lead classification
│   ├── zapier_deal_reuse_or_create.py
│   └── zapier_prepare_deal_properties.py
├── deal_signed/
│   └── zapier_deal_signed_map.md  # Product mapping
├── domain_redirects/
│   └── find_companies_by_domain.py
├── get_deal_owner_name/
│   └── zapier_get_owner_name.py
└── latest_company_deal/
    └── get_latest_company_deal.py
```

---

## Disabled/Legacy Zaps

These Zaps are OFF and should not be used:

| Zap | Reason |
|-----|--------|
| (Copy) Product Sign Ups | Duplicate - use original |
| (Copy) Demo Requests | Duplicate - use original |
| New Inbound | Legacy - replaced by Demo Requests |
| New Deal Signed | Legacy - replaced by Deal Signed |
| arr update | Legacy - replaced by ARR UPDATE |
| [OLD] Closed Lost Notes | Deprecated |

---

## How to Modify Zaps

### Making Changes
1. Go to [Zapier Editor](https://zapier.com/app/zaps)
2. Click on the Zap to edit
3. Make changes
4. Test with sample data
5. Publish new version
6. Update this documentation

### Adding Code Scripts
1. Write/modify script in `hs_zapier_code/` folder
2. Test locally
3. Copy to Zapier Code step
4. Update documentation

---

## Zapier Account Details

| Property | Value |
|----------|-------|
| Account | Dominik Vacikar Individual |
| Plan | Professional |
| Task Limit | 2,000/month |
| Active Zaps | ~50 |
| Held Runs | 250 max |

---

## Screenshots

Visual references are stored in each Zap's `screenshots/` folder:
- `demo_requests/screenshots/demo_requests_zap_overview.png`
