# Zapier Automations Documentation

> **Last Updated**: February 5, 2026  
> **Account**: Dominik Vacikar Individual (Professional Plan)  
> **Total Active Zaps**: 32  
> **Key Business Zaps**: 9  

## Overview

This documentation covers all **active** Zapier automations for Specter. Automations are auto-documented from the Zapier API with full step details.

---

## Quick Stats

| Metric | Value |
|--------|-------|
| Active Zaps | 32 |
| Key Business Automations | 9 |
| Landscape/Download Handlers | 23 |
| Total Steps (all zaps) | ~200 |
| Most Complex Zap | Demo Requests (76 steps) |

---

## Key Business Automations

### Sales & Lead Processing

| Zap | Steps | Apps | Last Active | Documentation |
|-----|-------|------|-------------|---------------|
| **Demo Requests** | 76 | GetForm → HubSpot → Slack → Gmail | Aug 2025 | [README](demo_requests/README.md) |
| **Product Sign Ups** | 32 | Webhook → HubSpot → Slack → Sheets | Dec 2025 | [README](product_sign_ups/README.md) |
| **Deal Signed** | 8 | HubSpot → AI → Sheets → Slack | Sep 2025 | [README](deal_signed/README.md) |
| **Deal Renewed** | 7 | HubSpot → AI → Sheets → Slack | Sep 2025 | [README](deal_renewed/README.md) |

### Finance & Reporting

| Zap | Steps | Apps | Last Active | Documentation |
|-----|-------|------|-------------|---------------|
| **ARR UPDATE** | 2 | Google Sheets → Slack | Feb 2025 | [README](arr_update/README.md) |
| **SALES TARGET UPDATE** | 4 | Google Sheets → Slack | Dec 2024 | [README](sales_target_update/README.md) |

### Communication & Support

| Zap | Steps | Apps | Last Active | Documentation |
|-----|-------|------|-------------|---------------|
| **Intercom Demo Email / Slack** | 12 | Intercom → HubSpot → Gmail → Slack | Jul 2024 | [README](intercom_demo_email/README.md) |
| **Intercom Request / Slack** | 5 | Intercom → AI → Slack | Oct 2024 | [README](intercom_request_slack/README.md) |

### HubSpot Data Management

| Zap | Steps | Apps | Last Active | Documentation |
|-----|-------|------|-------------|---------------|
| **Auto-set: Previous Customer / Customer** | 8 | HubSpot (lifecycle management) | May 2025 | [README](auto_set_lifecycle/README.md) |

---

## Automation Flow Architecture

```
                         ┌─────────────────────────────────────┐
                         │            TRIGGERS                 │
                         └─────────────────────────────────────┘
                                         │
         ┌───────────────┬───────────────┼───────────────┬───────────────┐
         │               │               │               │               │
         ▼               ▼               ▼               ▼               ▼
    ┌─────────┐    ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
    │ GetForm │    │  Webhook │   │ HubSpot  │   │ Intercom │   │  Sheets  │
    │  Forms  │    │ (Product)│   │  Events  │   │  Chats   │   │ Changes  │
    └────┬────┘    └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬─────┘
         │               │               │               │               │
         └───────────────┴───────────────┴───────────────┴───────────────┘
                                         │
                                         ▼
                         ┌─────────────────────────────────────┐
                         │         PROCESSING LAYER            │
                         │  • Code by Zapier (Python)          │
                         │  • Formatter by Zapier              │
                         │  • Filters & Paths                  │
                         │  • AI by Zapier                     │
                         └─────────────────────────────────────┘
                                         │
         ┌───────────────┬───────────────┼───────────────┬───────────────┐
         │               │               │               │               │
         ▼               ▼               ▼               ▼               ▼
    ┌─────────┐    ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
    │ HubSpot │    │  Slack   │   │  Gmail   │   │  Sheets  │   │ Intercom │
    │   CRM   │    │  Alerts  │   │  Emails  │   │  Logs    │   │  Replies │
    └─────────┘    └──────────┘   └──────────┘   └──────────┘   └──────────┘
```

---

## Detailed Zap Breakdown

### 1. Demo Requests (76 Steps)
**The most critical automation** - Processes all inbound demo requests.

| Component | Details |
|-----------|---------|
| **Trigger** | GetForm → New Form Submission |
| **Apps** | GetForm, Google Sheets, HubSpot, Gmail, Slack, Code by Zapier |
| **Key Functions** | Lead classification, deal creation, owner assignment, notifications |
| **Code Scripts** | `zapier_classify_lead_type.py`, `zapier_deal_owner.py` |

**Flow**:
1. Form submitted on tryspecter.com
2. Data formatted and logged to Sheets
3. HubSpot: Find/Create Company, Contact, Deal
4. Code: Classify lead type (New/Returning/Churned)
5. Code: Assign deal owner based on rules
6. Slack: Notify #sales-inbound
7. Gmail: Send internal summary

[Full Documentation →](demo_requests/README.md)

---

### 2. Product Sign Ups (32 Steps)
Tracks self-serve product signups.

| Component | Details |
|-----------|---------|
| **Trigger** | Webhook from Product Backend |
| **Apps** | HubSpot, Google Sheets, Slack, Code by Zapier |
| **Key Functions** | Contact/company creation, deal tracking, notifications |

[Full Documentation →](product_sign_ups/README.md)

---

### 3. Deal Signed (8 Steps)
Celebrates and logs won deals.

| Component | Details |
|-----------|---------|
| **Trigger** | HubSpot Deal → Stage = Won |
| **Apps** | HubSpot, AI by Zapier, Google Sheets, Slack |
| **Key Functions** | Product mapping, finance logging, Slack celebration |

[Full Documentation →](deal_signed/README.md)

---

### 4. Deal Renewed (7 Steps)
Tracks customer renewals.

| Component | Details |
|-----------|---------|
| **Trigger** | HubSpot Deal → Stage = Renewed |
| **Apps** | HubSpot, AI by Zapier, Google Sheets, Slack |
| **Key Functions** | Renewal tracking, ARR maintenance, celebration |

[Full Documentation →](deal_renewed/README.md)

---

### 5. Intercom Demo Email / Slack (12 Steps)
Routes demo requests from Intercom chat.

| Component | Details |
|-----------|---------|
| **Trigger** | Intercom Conversation (demo keywords) |
| **Apps** | Intercom, HubSpot, Gmail, Slack, Code by Zapier |
| **Key Functions** | Keyword detection, HubSpot enrichment, routing |

[Full Documentation →](intercom_demo_email/README.md)

---

### 6. Auto-set Lifecycle (8 Steps)
Manages HubSpot lifecycle stages automatically.

| Component | Details |
|-----------|---------|
| **Trigger** | HubSpot Deal Stage Changes |
| **Apps** | HubSpot, Filter by Zapier |
| **Key Functions** | Set Previous Customer / Customer lifecycle |

[Full Documentation →](auto_set_lifecycle/README.md)

---

### 7. Intercom Request / Slack (5 Steps)
Alerts support team of Intercom requests.

| Component | Details |
|-----------|---------|
| **Trigger** | Intercom New Conversation |
| **Apps** | Intercom, AI by Zapier, Slack |
| **Key Functions** | Request classification, Slack routing |

[Full Documentation →](intercom_request_slack/README.md)

---

### 8. SALES TARGET UPDATE (4 Steps)
Tracks progress against sales targets.

| Component | Details |
|-----------|---------|
| **Trigger** | Google Sheets Row Updated |
| **Apps** | Google Sheets, Slack, Code by Zapier |
| **Key Functions** | Target calculation, progress alerts |

[Full Documentation →](sales_target_update/README.md)

---

### 9. ARR UPDATE (2 Steps)
Real-time ARR tracking.

| Component | Details |
|-----------|---------|
| **Trigger** | Google Sheets Row Updated |
| **Apps** | Google Sheets, Slack |
| **Key Functions** | ARR change notifications |

[Full Documentation →](arr_update/README.md)

---

## Landscape Download Zaps (23 Active)

These are simple 3-step form handlers for landscape report downloads:

| Category | Count | Example |
|----------|-------|---------|
| AI/Tech Landscapes | 12 | AI x GTM, AI Voice Agents, AI Agents Ecosystem |
| Industry Landscapes | 8 | Biotech, Legal AI, Restaurant Tech |
| Regional Landscapes | 3 | LATAM AI, French AI, EU Defence |

Each follows the pattern: GetForm → Google Sheets → Slack notification

---

## Code by Zapier Scripts

All Python scripts are maintained in version control:

```
hubspot_automations/scripts/hs_zapier_code/
├── assign_deal_owner/
│   ├── zapier_deal_owner.py           # Deal owner assignment logic
│   ├── zapier_returning_lead_owner.py # Returning lead handling
│   └── test_deal_owner.py             # Unit tests
├── demo_request/
│   ├── zapier_classify_lead_type.py   # Lead classification (800+ lines)
│   ├── zapier_deal_reuse_or_create.py
│   └── ZAPIER_MAPPING_GUIDE.md
└── deal_signed/
    └── zapier_deal_signed_map.md
```

---

## Disabled/Legacy Zaps

| Zap | Status | Reason |
|-----|--------|--------|
| Intercom Bot Reply / Slack | OFF | Replaced/Consolidated |
| Contacts to Deals Associations | OFF | Manual process now |
| (Copy) Product Sign Ups | OFF | Duplicate |
| (Copy) Demo Requests | OFF | Duplicate |
| [OLD] Closed Lost Notes | OFF | Deprecated |

---

## Documentation Tools

### Auto-Generate Documentation

```bash
cd zapier_automations/scripts

# 1. Export from browser (at zapier.com/app/zaps, F12 → Console):
# [paste browser export script from SETUP.md]

# 2. Move downloaded file:
mv ~/Downloads/zaps_full_details.json data/

# 3. Generate READMEs for active zaps:
python3 zapier_api.py --document --from-file data/zaps_full_details.json --active-only

# 4. Check status:
python3 zapier_api.py --status
```

### Available Commands

```bash
python3 zapier_api.py --document --active-only    # Generate docs for active zaps
python3 zapier_api.py --status                    # Show documentation status
python3 zapier_api.py --list-mapped               # Show zap-to-folder mappings
```

---

## Account Details

| Property | Value |
|----------|-------|
| Account | Dominik Vacikar Individual |
| Plan | Professional |
| Monthly Task Limit | 2,000 |
| Active Zaps | 32 |
| Folders | Leads, CS, Hubspot Automations, Landscapes |

---

## Quick Links

- [Zapier Dashboard](https://zapier.com/app/zaps)
- [Demo Requests Editor](https://zapier.com/editor/262386682)
- [Product Sign Ups Editor](https://zapier.com/editor/268969745)
- [Deal Signed Editor](https://zapier.com/editor/164077234)

---

## Changelog

| Date | Changes |
|------|---------|
| Feb 5, 2026 | Full documentation refresh from API export |
| Jan 29, 2026 | Added auto-documentation scripts |
| Jan 2026 | Demo Requests v117 - fixed returning lead classification |

---

*Documentation auto-generated from Zapier API. Last sync: February 5, 2026*
