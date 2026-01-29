# Auto-set: Previous Customer / Customer

> **Status**: ✅ Active (ON)  
> **Location**: CS  
> **Last Modified**: Jun 3, 2025  
> **Owner**: Dominik Vacikar  

## What This Zap Does

Automatically manages HubSpot contact **lifecycle stage** based on deal status:

1. When a deal is **Won** → Set contact lifecycle to "Customer"
2. When a deal is **Churned** → Set contact lifecycle to "Previous Customer"

---

## Why This Exists

### Business Problem Solved
- Manual lifecycle updates were inconsistent
- Contacts remained as "Customer" after churn
- Segmentation for marketing was inaccurate

### Value Delivered
- Accurate lifecycle tracking
- Better marketing segmentation
- Automated data hygiene

---

## Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         TRIGGER                                  │
│  HubSpot → Deal Stage Changed                                   │
└─────────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              │                               │
              ▼                               ▼
┌─────────────────────────┐     ┌─────────────────────────┐
│   Stage = "Won"         │     │   Stage = "Churned"     │
│   ↓                     │     │   ↓                     │
│   Set Lifecycle =       │     │   Set Lifecycle =       │
│   "Customer"            │     │   "Previous Customer"   │
└─────────────────────────┘     └─────────────────────────┘
```

---

## Trigger Conditions

| Event | Pipeline | Stage | Lifecycle Set To |
|-------|----------|-------|------------------|
| Deal Won | Sales | Won | Customer |
| Deal Churned | Renewals | Churned | Previous Customer |

---

## HubSpot Properties Modified

| Property | Object | Values |
|----------|--------|--------|
| `lifecyclestage` | Contact | "customer", "236741536" (Previous Customer) |

---

## Related Documentation

- [Demo Requests](../demo_requests/README.md) - Uses lifecycle for lead classification
- [Deal Signed](../deal_signed/README.md) - Triggers "Customer" lifecycle
