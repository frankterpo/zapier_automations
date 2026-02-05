# Product Sign Ups Automation

> **Status**: ✅ Active (ON)  
> **Zap ID**: 268969745  
> **Steps**: 32  
> **Last Modified**: January 19, 2026  
> **Last Successful Run**: December 19, 2025 at 14:58 UTC  
> **Editor**: [Open in Zapier](https://zapier.com/editor/268969745)

## Table of Contents
1. [What This Zap Does](#what-this-zap-does)
2. [Apps Used](#apps-used)
3. [Flow Architecture](#flow-architecture)
4. [Step-by-Step Breakdown](#step-by-step-breakdown)
5. [Troubleshooting](#troubleshooting)
6. [How to Modify](#how-to-modify)

---

## What This Zap Does

This automation is triggered by **Slack** and performs 31 subsequent actions.

**Trigger**: Slack: Send Channel Message

**Main Actions**: Code by Zapier → HubSpot → Googlesheets → Slack

---

## Apps Used

| App | Usage in Zap |
|-----|-------------|
| Slack | 4 step(s): Slack: Send Channel Message, Slack: Send Channel Message, Slack: Send Channel Message +1 more |
| Code by Zapier | 4 step(s): Code by Zapier: Custom Code, Code by Zapier: Custom Code, Code by Zapier: Custom Code +1 more |
| HubSpot | 8 step(s): HubSpot: Create Associations, HubSpot: Update CRM Deal, HubSpot: Create Associations +5 more |
| Filter by Zapier | 3 step(s): Filter by Zapier: Filter, Filter by Zapier: Filter, Filter by Zapier: Filter |
| Googlesheets | 5 step(s): Googlesheets: Create Spreadsheet Row, Googlesheets: Create Spreadsheet Row, Googlesheets: Create Spreadsheet Row +2 more |
| Branching | 8 step(s): Branching: Filter, Branching: Filter, Branching: Filter +5 more |

---

## Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                             TRIGGER                             │
│  1. Slack: Send Channel Message                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  2. Code by Zapier: Custom Code                                 │
│  3. HubSpot: Create Associations                                │
│  4. HubSpot: Update CRM Deal                                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  5. Filter by Zapier: Filter                                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  6. Googlesheets: Create Spreadsheet Row                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  7. Branching: Filter                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  8. Googlesheets: Create Spreadsheet Row                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  9. Branching: Filter                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  10. Googlesheets: Create Spreadsheet Row                        │
│  11. Googlesheets: Create Spreadsheet Row                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  12. Branching: Filter                                           │
│  13. Branching: branch                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  14. Code by Zapier: Custom Code                                 │
│  15. Googlesheets: Create Spreadsheet Row                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  16. Filter by Zapier: Filter                                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  17. HubSpot: Create Associations                                │
│  18. HubSpot: Find Deal                                          │
│  19. Slack: Send Channel Message                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  20. Branching: Filter                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  21. Code by Zapier: Custom Code                                 │
│  22. HubSpot: Find Deal                                          │
│  23. HubSpot: find_associations                                  │
│  24. Slack: Send Channel Message                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  25. Branching: Filter                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  26. Slack: Send Channel Message                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  27. Branching: Filter                                           │
│  28. Branching: branch                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  29. HubSpot: upsert_contact                                     │
│  30. HubSpot: Find Company                                       │
│  31. Code by Zapier: Custom Code                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  32. Filter by Zapier: Filter                                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Step-by-Step Breakdown

### Step 1: Slack: Send Channel Message

| Property | Value |
|----------|-------|
| **Type** | ⚡ Trigger |
| **App** | Slack |
| **Action** | Send Channel Message |

### Step 2: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 3: HubSpot: Create Associations

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | Create Associations |

### Step 4: HubSpot: Update CRM Deal

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | Update CRM Deal |

### Step 5: Filter by Zapier: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Filter |
| **App** | Filter by Zapier |
| **Action** | Filter |

### Step 6: Googlesheets: Create Spreadsheet Row

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlesheets |
| **Action** | Create Spreadsheet Row |

### Step 7: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 8: Googlesheets: Create Spreadsheet Row

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlesheets |
| **Action** | Create Spreadsheet Row |

### Step 9: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 10: Googlesheets: Create Spreadsheet Row

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlesheets |
| **Action** | Create Spreadsheet Row |

### Step 11: Googlesheets: Create Spreadsheet Row

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlesheets |
| **Action** | Create Spreadsheet Row |

### Step 12: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 13: Branching: branch

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | branch |

### Step 14: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 15: Googlesheets: Create Spreadsheet Row

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlesheets |
| **Action** | Create Spreadsheet Row |

### Step 16: Filter by Zapier: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Filter |
| **App** | Filter by Zapier |
| **Action** | Filter |

### Step 17: HubSpot: Create Associations

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | Create Associations |

### Step 18: HubSpot: Find Deal

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search_Or_Create |
| **App** | HubSpot |
| **Action** | Find Deal |

### Step 19: Slack: Send Channel Message

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Slack |
| **Action** | Send Channel Message |

### Step 20: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 21: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 22: HubSpot: Find Deal

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search |
| **App** | HubSpot |
| **Action** | Find Deal |

### Step 23: HubSpot: find_associations

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search |
| **App** | HubSpot |
| **Action** | find_associations |

### Step 24: Slack: Send Channel Message

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Slack |
| **Action** | Send Channel Message |

### Step 25: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 26: Slack: Send Channel Message

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Slack |
| **Action** | Send Channel Message |

### Step 27: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 28: Branching: branch

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | branch |

### Step 29: HubSpot: upsert_contact

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | upsert_contact |

### Step 30: HubSpot: Find Company

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search |
| **App** | HubSpot |
| **Action** | Find Company |

### Step 31: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 32: Filter by Zapier: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Filter |
| **App** | Filter by Zapier |
| **Action** | Filter |

---

## Troubleshooting

### Common Issues

#### Zap Not Triggering

**Check**:
1. Verify the trigger app connection is active
2. Check if the trigger event actually occurred
3. Review Zap history for filtered out runs

#### Step Errors

**Check**:
1. Verify app authentication is current
2. Check if required fields have values
3. Review error message in Zap history

### Viewing Zap History

1. Open [Zap Editor](https://zapier.com/editor/268969745)
2. Click "Zap runs" in left sidebar
3. Review individual runs for errors

---

## How to Modify

### Editing Steps

1. Open the Zap in Zapier Editor
2. Click on the step you want to modify
3. Update the configuration
4. Test the step
5. Publish the changes

### Adding New Steps

1. Click the "+" button between steps
2. Search for the app you want to add
3. Configure the action
4. Map fields from previous steps
5. Test and publish

### Changing Trigger

⚠️ **Warning**: Changing the trigger may require re-mapping all subsequent steps.

1. Click on the trigger step
2. Select new trigger event
3. Reconfigure trigger settings
4. Review and update all field mappings
5. Test entire Zap before publishing

---

## Version History

| Date | Changes |
|------|---------|
| January 19, 2026 | Last modified |
| - | Documentation auto-generated |

---

*This documentation was auto-generated from Zapier API data.*
*Last updated: 2026-02-05 15:01*
