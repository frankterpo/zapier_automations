# Deal Renewed Automation

> **Status**: ✅ Active (ON)  
> **Location**: Internal Operations  
> **Last Modified**: Oct 20, 2025  
> **Owner**: Dominik Vacikar  

## Table of Contents
1. [What This Zap Does](#what-this-zap-does)
2. [Why This Exists](#why-this-exists)
3. [Flow Architecture](#flow-architecture)
4. [Trigger Conditions](#trigger-conditions)
5. [Notifications](#notifications)

---

## What This Zap Does

When an existing customer **renews** their contract (deal stage = "Renewed" in Renewals pipeline), this Zap:

1. **Captures** the renewal deal data
2. **Logs** renewal to Google Sheets (finance tracking)
3. **Celebrates** with Slack notification
4. **Updates** company lifecycle properties

---

## Why This Exists

### Business Problem Solved
- **Visibility**: Team wasn't tracking renewal wins
- **Finance**: Manual ARR tracking for renewals
- **Churn Prevention**: No systematic renewal process

### Value Delivered
- Real-time renewal tracking
- Automated ARR adjustments
- Team visibility on customer success

---

## Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         TRIGGER                                  │
│  HubSpot → Deal in Renewals Pipeline → "Renewed" Stage          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DATA EXTRACTION                            │
│  1. Get deal properties (amount, products, owner)               │
│  2. Get associated company                                      │
│  3. Calculate renewal year (Y2, Y3, etc.)                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     LOGGING & NOTIFICATIONS                     │
│  4. Google Sheets: Log to Renewals tracker                      │
│  5. Slack: Post renewal celebration                             │
│  6. Update company: renewal_date, customer status               │
└─────────────────────────────────────────────────────────────────┘
```

---

## Trigger Conditions

**App**: HubSpot  
**Event**: Deal property changed  
**Pipeline**: Renewals (`88620615`)  
**Stage**: Renewed

### Renewals Pipeline Stages

| Stage | Description |
|-------|-------------|
| New Client | Just signed, in onboarding |
| 11-9M to Renewal | 11-9 months before renewal |
| 9-6M to Renewal | 9-6 months before renewal |
| 6-3M to Renewal | 6-3 months before renewal |
| 3-2M to Renewal | 3-2 months before renewal |
| 1M to Renewal | 1 month before renewal |
| Renewal Action | Active renewal negotiation |
| **Renewed** | ✅ Deal renewed (triggers this Zap) |
| Churned | ❌ Customer did not renew |

---

## Notifications

### Slack Message Format

```
🔄 RENEWAL COMPLETE! 🔄

Company: Acme Corp
Renewal Year: Y2
Amount: €50,000
Products: Company Database, People Database
CS Owner: Isabella Garcia Foster

View Deal: [HubSpot Link]
```

### Google Sheets Logging

| Column | Value |
|--------|-------|
| Date | Auto-timestamp |
| Company | Company name |
| Deal Name | Company - Y2 |
| Amount | Deal amount |
| Products | Product list |
| Owner | Deal owner name |
| Year | Renewal year number |

---

## Differences from Deal Signed

| Aspect | Deal Signed | Deal Renewed |
|--------|-------------|--------------|
| Pipeline | Sales | Renewals |
| Stage | Won | Renewed |
| Slack Channel | #sales-wins | #cs-renewals |
| Purpose | New customer | Existing customer |

---

## Related Documentation

- [Deal Signed](../deal_signed/README.md) - New customer wins
- [ARR UPDATE](../arr_update/README.md) - Financial tracking
