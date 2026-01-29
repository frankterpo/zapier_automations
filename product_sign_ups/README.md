# Product Sign Ups Automation

> **Status**: ✅ Active (ON)  
> **Location**: Leads  
> **Last Modified**: Jan 19, 2026  
> **Owner**: Dominik Vacikar  

## Table of Contents
1. [What This Zap Does](#what-this-zap-does)
2. [Why This Exists](#why-this-exists)
3. [Flow Architecture](#flow-architecture)
4. [Trigger Setup](#trigger-setup)
5. [HubSpot Actions](#hubspot-actions)
6. [Notifications](#notifications)

---

## What This Zap Does

When a user **signs up for Specter's product** (self-serve), this Zap:

1. **Receives** webhook from product backend
2. **Creates/Updates** contact in HubSpot
3. **Creates/Updates** company in HubSpot
4. **Creates** a deal in the Leads pipeline
5. **Logs** signup to Google Sheets
6. **Notifies** team via Slack

---

## Why This Exists

### Business Problem Solved
- **Lead Capture**: Product signups weren't tracked in CRM
- **Sales Awareness**: Team didn't know who was signing up
- **Follow-up**: No system to nurture self-serve leads

### Value Delivered
- Every product signup becomes a CRM lead
- Sales can prioritize high-potential signups
- Product-led growth (PLG) visibility

---

## Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         TRIGGER                                  │
│  Webhook from Specter Backend → New User Signup                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DATA PREPARATION                           │
│  1. Format date/time                                            │
│  2. Extract domain from email                                   │
│  3. Clean/format fields                                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    HUBSPOT ENRICHMENT                           │
│  4. Find or Create Company (by domain)                          │
│  5. Find or Create Contact (by email)                           │
│  6. Create Deal in Leads/Inbound pipeline                       │
│  7. Create associations (Company ↔ Contact ↔ Deal)              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      LOGGING & NOTIFICATIONS                    │
│  8. Google Sheets: Log signup                                   │
│  9. Slack: Notify #product-signups                              │
└─────────────────────────────────────────────────────────────────┘
```

---

## Trigger Setup

**Type**: Webhook (Catch Hook)  
**Source**: Specter product backend  
**Event**: User registration completed

### Expected Payload

```json
{
  "email": "john@acme.com",
  "first_name": "John",
  "last_name": "Smith",
  "company": "Acme Corp",
  "job_title": "Data Analyst",
  "signup_source": "self_serve",
  "plan": "free_trial",
  "timestamp": "2026-01-29T14:30:00Z"
}
```

---

## HubSpot Actions

### Contact Properties Set

| Property | Source | Notes |
|----------|--------|-------|
| `email` | Webhook | Primary identifier |
| `firstname` | Webhook | |
| `lastname` | Webhook | |
| `jobtitle` | Webhook | |
| `lifecyclestage` | Fixed | "lead" |
| `hs_lead_status` | Fixed | "NEW" |
| `signup_date` | Webhook timestamp | Custom property |
| `signup_source` | Fixed | "product_signup" |
| `plan_type` | Webhook | free_trial, paid, etc. |

### Company Properties Set

| Property | Source |
|----------|--------|
| `name` | Webhook company |
| `domain` | Extracted from email |

### Deal Properties Set

| Property | Value |
|----------|-------|
| `dealname` | `{Company} - Product Signup` |
| `pipeline` | Leads/Inbound (`701945664`) |
| `dealstage` | Inbound (`1025533703`) |
| `lead_source` | "product_signup" |
| `signup_plan` | From webhook |

---

## Notifications

### Slack Channel
`#product-signups`

### Message Format
```
📱 New Product Signup!

Email: john@acme.com
Company: Acme Corp
Job Title: Data Analyst
Plan: Free Trial
Time: Jan 29, 2026, 2:30 PM

View in HubSpot: [Link]
```

### Google Sheets Log
Spreadsheet: "Product Signups Tracker"

| Column | Value |
|--------|-------|
| Timestamp | Auto |
| Email | User email |
| Company | Company name |
| Job Title | User job title |
| Plan | Signup plan |
| HubSpot Contact ID | Created contact ID |

---

## Troubleshooting

### Signup Not Appearing in HubSpot

**Check**:
1. Webhook delivery in product backend logs
2. Zapier task history for errors
3. Email format is valid

### Duplicate Contacts

**Symptom**: Multiple contacts for same email

**Cause**: Race condition or find step not matching

**Fix**: HubSpot deduplicates by email automatically

---

## Related Documentation

- [Demo Requests](../demo_requests/README.md) - Form-based lead flow
- [Product Import Requests](../product_import_requests/README.md) - Data import leads
