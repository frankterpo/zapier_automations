# ARR UPDATE Automation

> **Status**: ✅ Active (ON)  
> **Location**: Dominik Vacikar (Personal)  
> **Last Modified**: Dec 19, 2025  
> **Owner**: Dominik Vacikar  

## Table of Contents
1. [What This Zap Does](#what-this-zap-does)
2. [Why This Exists](#why-this-exists)
3. [Flow Architecture](#flow-architecture)
4. [Trigger Conditions](#trigger-conditions)
5. [ARR Calculation](#arr-calculation)

---

## What This Zap Does

This Zap maintains real-time **ARR (Annual Recurring Revenue)** tracking by:

1. **Monitoring** HubSpot deal changes (won, lost, renewed, churned)
2. **Calculating** impact on ARR
3. **Updating** Google Sheets finance tracker
4. **Maintaining** historical ARR data

---

## Why This Exists

### Business Problem Solved
- **Real-time ARR**: Finance needed live ARR numbers
- **Manual Tracking**: Spreadsheets were outdated
- **Investor Reporting**: Quick access to key metrics

### Value Delivered
- Always-current ARR in Google Sheets
- Automatic calculation on deal changes
- Historical trend data for reporting

---

## Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         TRIGGERS                                 │
│  HubSpot Deal Changes:                                          │
│  • Deal Won → Add to ARR                                        │
│  • Deal Lost → No change (wasn't revenue)                       │
│  • Deal Renewed → Maintain ARR                                  │
│  • Deal Churned → Subtract from ARR                             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      ARR CALCULATION                            │
│  1. Get deal amount (annual value)                              │
│  2. Determine action (add/subtract/maintain)                    │
│  3. Apply to running total                                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     GOOGLE SHEETS UPDATE                        │
│  4. Update ARR total cell                                       │
│  5. Log change with timestamp                                   │
│  6. Record deal details                                         │
└─────────────────────────────────────────────────────────────────┘
```

---

## Trigger Conditions

### ARR Increase Events
- Deal stage → "Won" (Sales pipeline)
- Deal stage → "Renewed" (Renewals pipeline)
- Upsell deal closed

### ARR Decrease Events
- Deal stage → "Churned" (Renewals pipeline)
- Partial churn (contract reduction)

### No ARR Change
- Deal stage → "Lost" (never was customer)
- Deal moved between non-closed stages

---

## ARR Calculation

### Formula
```
New ARR = Current ARR + Deal Amount (if won/renewed)
New ARR = Current ARR - Deal Amount (if churned)
```

### Monthly Breakdown
For deals with monthly payment terms:
```
ARR Contribution = Monthly Amount × 12
```

### Multi-year Deals
```
ARR Contribution = Total Deal Value / Contract Years
```

---

## Google Sheets Structure

### ARR Summary Sheet

| Cell | Content |
|------|---------|
| B1 | Current ARR |
| B2 | MTD New ARR |
| B3 | MTD Churned ARR |
| B4 | Net ARR Change |

### ARR Log Sheet

| Column | Description |
|--------|-------------|
| A | Timestamp |
| B | Deal Name |
| C | Company |
| D | Action (New/Renewed/Churned) |
| E | Amount |
| F | Running ARR Total |

---

## Related Documentation

- [Deal Signed](../deal_signed/README.md) - New ARR
- [Deal Renewed](../deal_renewed/README.md) - Renewal ARR
- [SALES TARGET UPDATE](../sales_target_update/README.md) - Target tracking
