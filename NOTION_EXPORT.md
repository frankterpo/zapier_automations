# Zapier Automations

> Last Updated: February 5, 2026
> Account: Dominik Vacikar (Professional Plan)
> Active Zaps: 32 | Key Business Zaps: 9

---

## Overview

Specter uses Zapier for workflow automation across sales, finance, and customer success. All automations are documented with full step details.

---

## Key Business Automations

### Sales & Lead Processing

| Automation | Steps | Flow | Status |
|------------|-------|------|--------|
| **Demo Requests** | 76 | GetForm → HubSpot → Slack → Gmail | ✅ Active |
| **Product Sign Ups** | 32 | Webhook → HubSpot → Slack → Sheets | ✅ Active |
| **Deal Signed** | 8 | HubSpot → AI → Sheets → Slack | ✅ Active |
| **Deal Renewed** | 7 | HubSpot → AI → Sheets → Slack | ✅ Active |

### Finance & Reporting

| Automation | Steps | Flow | Status |
|------------|-------|------|--------|
| **ARR UPDATE** | 2 | Google Sheets → Slack | ✅ Active |
| **SALES TARGET UPDATE** | 4 | Google Sheets → Slack | ✅ Active |

### Communication & Support

| Automation | Steps | Flow | Status |
|------------|-------|------|--------|
| **Intercom Demo Email / Slack** | 12 | Intercom → HubSpot → Gmail → Slack | ✅ Active |
| **Intercom Request / Slack** | 5 | Intercom → AI → Slack | ✅ Active |

### HubSpot Data Management

| Automation | Steps | Flow | Status |
|------------|-------|------|--------|
| **Auto-set Lifecycle** | 8 | HubSpot lifecycle management | ✅ Active |

---

## Detailed Breakdown

### 1. Demo Requests (76 Steps) ⭐ Most Critical

**Purpose**: Process all inbound demo requests from tryspecter.com

**Trigger**: GetForm form submission

**What It Does**:
1. Captures form data from tryspecter.com
2. Logs submission to Google Sheets (backup)
3. Finds or creates Company in HubSpot (by domain)
4. Finds or creates Contact in HubSpot (by email)
5. Classifies lead type:
   - **New Lead**: First-time inquiry
   - **Returning Lead**: Has existing deal
   - **Returning Churned**: Was customer, then churned
6. Assigns deal owner based on rules:
   - AUM < 200m → Philipp Berhoerster
   - New Business → Marco Squarci
   - Returning → Keep original owner (unless departed)
7. Posts to #sales-inbound Slack channel
8. Sends internal email summary

**Apps Used**: GetForm, Google Sheets, HubSpot, Gmail, Slack, Code by Zapier

**Code Scripts**:
- `zapier_classify_lead_type.py` - Lead classification logic
- `zapier_deal_owner.py` - Owner assignment rules

---

### 2. Product Sign Ups (32 Steps)

**Purpose**: Track self-serve product signups

**Trigger**: Webhook from Specter product backend

**What It Does**:
1. Receives signup webhook
2. Creates/updates HubSpot Contact
3. Creates/updates HubSpot Company
4. Creates Deal in Leads pipeline
5. Logs to Google Sheets
6. Notifies #product-signups Slack

---

### 3. Deal Signed (8 Steps)

**Purpose**: Celebrate and log won deals

**Trigger**: HubSpot Deal stage → Won

**What It Does**:
1. Detects deal won
2. Uses AI to extract product mapping
3. Logs to Finance Google Sheet
4. Posts celebration to Slack

---

### 4. Deal Renewed (7 Steps)

**Purpose**: Track customer renewals

**Trigger**: HubSpot Deal stage → Renewed

**What It Does**:
1. Detects renewal
2. Updates ARR tracking
3. Logs to Finance Sheet
4. Posts celebration to Slack

---

### 5. Intercom Demo Email / Slack (12 Steps)

**Purpose**: Route demo requests from Intercom chat

**Trigger**: Intercom conversation with demo keywords

**What It Does**:
1. Detects demo-related keywords in chat
2. Enriches contact in HubSpot
3. Sends email notification
4. Posts to Slack

---

### 6. Auto-set Lifecycle (8 Steps)

**Purpose**: Manage HubSpot lifecycle stages

**Trigger**: HubSpot deal stage changes

**What It Does**:
1. Monitors deal stage changes
2. Sets Contact lifecycle to "Customer" when deal won
3. Sets lifecycle to "Previous Customer" when churned

---

### 7. Intercom Request / Slack (5 Steps)

**Purpose**: Alert support team of requests

**Trigger**: New Intercom conversation

**What It Does**:
1. Receives new conversation
2. Uses AI to classify request type
3. Routes to appropriate Slack channel

---

### 8. SALES TARGET UPDATE (4 Steps)

**Purpose**: Track sales target progress

**Trigger**: Google Sheets target row updated

**What It Does**:
1. Monitors target tracking sheet
2. Calculates progress percentage
3. Sends Slack update

---

### 9. ARR UPDATE (2 Steps)

**Purpose**: Real-time ARR tracking

**Trigger**: Google Sheets ARR row updated

**What It Does**:
1. Monitors ARR tracking sheet
2. Sends Slack notification on changes

---

## Landscape Download Zaps (23 Active)

Simple 3-step form handlers for landscape report downloads.

**Pattern**: GetForm → Google Sheets → Slack

**Examples**:
- AI x GTM Landscape 2025
- AI Voice Agents 2025
- AI Agents Ecosystem 2025
- 500+ Startups in Biotechnology 2025
- 400+ Legal AI Landscape
- EU Defence Startups 2025
- French AI Startups 2025
- LATAM AI Startups 2025

---

## Code Scripts Location

All Python scripts maintained in GitHub:

```
hubspot_automations/scripts/hs_zapier_code/
├── assign_deal_owner/
│   └── zapier_deal_owner.py
├── demo_request/
│   └── zapier_classify_lead_type.py
└── deal_signed/
    └── zapier_deal_signed_map.md
```

---

## Owner Assignment Rules

| Condition | Assigned To |
|-----------|-------------|
| AUM < 200m | Philipp Berhoerster |
| New Business (default) | Marco Squarci |
| Returning (departed owner) | Marco Squarci |
| Returning (active owner) | Keep original |
| Upsell | Keep current owner |

**Owner IDs**:
- Marco Squarci: 35673999
- Philipp Berhoerster: 77583320
- Dominik Vacikar: 49928941

---

## Lead Classification Logic

| Type | Definition | Action |
|------|------------|--------|
| **New Lead** | First-time inquiry | Create new deal |
| **Returning Lead** | Has existing deal | Reuse existing deal |
| **Returning Churned** | Was customer, churned | High priority re-engagement |

---

## Account Info

| Property | Value |
|----------|-------|
| Account | Dominik Vacikar Individual |
| Plan | Professional |
| Task Limit | 2,000/month |
| Active Zaps | 32 |

---

## Quick Links

- [Zapier Dashboard](https://zapier.com/app/zaps)
- [Demo Requests](https://zapier.com/editor/262386682)
- [Product Sign Ups](https://zapier.com/editor/268969745)
- [Deal Signed](https://zapier.com/editor/164077234)
- [Deal Renewed](https://zapier.com/editor/236426171)

---

## Disabled Zaps

| Zap | Reason |
|-----|--------|
| Intercom Bot Reply / Slack | Consolidated |
| Contacts to Deals Associations | Manual process |
| (Copy) Product Sign Ups | Duplicate |
| (Copy) Demo Requests | Duplicate |

---

*Last sync: February 5, 2026*
