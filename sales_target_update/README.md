# SALES TARGET UPDATE Automation

> **Status**: ✅ Active (ON)  
> **Location**: Internal Operations  
> **Last Modified**: Jan 20, 2026  
> **Owner**: Dominik Vacikar  

## Table of Contents
1. [What This Zap Does](#what-this-zap-does)
2. [Why This Exists](#why-this-exists)
3. [Flow Architecture](#flow-architecture)
4. [Update Logic](#update-logic)
5. [Target Tracking](#target-tracking)

---

## What This Zap Does

This Zap maintains **sales target progress** tracking by:

1. **Monitoring** HubSpot deal wins
2. **Calculating** progress toward monthly/quarterly targets
3. **Updating** Google Sheets sales dashboard
4. **Tracking** individual rep performance

---

## Why This Exists

### Business Problem Solved
- **Target Visibility**: Sales needed real-time target progress
- **Manual Updates**: Dashboard was always outdated
- **Motivation**: No gamification or progress tracking

### Value Delivered
- Real-time target progress percentages
- Individual rep tracking
- Monthly/quarterly roll-ups

---

## Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         TRIGGER                                  │
│  HubSpot → Deal Won (Sales Pipeline)                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DATA EXTRACTION                            │
│  1. Get deal amount                                             │
│  2. Get deal owner                                              │
│  3. Get close date (determines period)                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     CALCULATION                                  │
│  4. Add to rep's monthly total                                  │
│  5. Add to team monthly total                                   │
│  6. Calculate % of target                                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     GOOGLE SHEETS UPDATE                        │
│  7. Update individual rep progress                              │
│  8. Update team totals                                          │
│  9. Update target % cells                                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## Update Logic

### Monthly Target Calculation

```
Rep Progress = Sum(Deals Won This Month for Rep)
Team Progress = Sum(All Deals Won This Month)
% of Target = (Progress / Target) × 100
```

### Period Detection

Close date determines which period to credit:
- Close Date in January → January totals
- Close Date in Q1 → Q1 totals

---

## Target Tracking

### Google Sheets Structure

#### Individual Targets
| Rep | Monthly Target | MTD Won | % Progress |
|-----|---------------|---------|------------|
| Marco | €100,000 | €45,000 | 45% |
| Philipp | €75,000 | €60,000 | 80% |
| Isabella | €75,000 | €30,000 | 40% |

#### Team Summary
| Metric | Value |
|--------|-------|
| Team Monthly Target | €250,000 |
| Team MTD Won | €135,000 |
| Team % Progress | 54% |
| Days Left in Month | 15 |
| Required Run Rate | €7,667/day |

---

## Related Documentation

- [ARR UPDATE](../arr_update/README.md) - Overall revenue tracking
- [Deal Signed](../deal_signed/README.md) - Individual deal wins
