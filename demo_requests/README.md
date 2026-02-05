# Demo Requests Automation

> **Status**: ✅ Active (ON)  
> **Zap ID**: 262386682  
> **Steps**: 76  
> **Last Modified**: February 04, 2026  
> **Last Successful Run**: August 06, 2025 at 19:24 UTC  
> **Editor**: [Open in Zapier](https://zapier.com/editor/262386682)

## Table of Contents
1. [What This Zap Does](#what-this-zap-does)
2. [Apps Used](#apps-used)
3. [Flow Architecture](#flow-architecture)
4. [Step-by-Step Breakdown](#step-by-step-breakdown)
5. [Troubleshooting](#troubleshooting)
6. [How to Modify](#how-to-modify)

---

## What This Zap Does

This automation is triggered by **GetForm** and performs 75 subsequent actions.

**Trigger**: GetForm: New Form Submission

**Main Actions**: Code by Zapier → Googlesheets → HubSpot → Zapierformatter → Googlemail → Slack

---

## Apps Used

| App | Usage in Zap |
|-----|-------------|
| GetForm | 1 step(s): GetForm: New Form Submission |
| Code by Zapier | 12 step(s): Code by Zapier: Custom Code, Code by Zapier: Custom Code, Code by Zapier: Custom Code +9 more |
| Googlesheets | 2 step(s): Googlesheets: Create Spreadsheet Row, Googlesheets: Create Spreadsheet Row |
| HubSpot | 21 step(s): HubSpot: Update CRM Deal, HubSpot: Update CRM Deal, HubSpot: Update CRM Deal +18 more |
| Filter by Zapier | 2 step(s): Filter by Zapier: Filter, Filter by Zapier: Filter |
| Zapierformatter | 2 step(s): Zapierformatter: datetime_line_item, Zapierformatter: text_line_item |
| Googlemail | 9 step(s): Googlemail: Send Email, Googlemail: Send Email, Googlemail: Send Email +6 more |
| Slack | 9 step(s): Slack: Send Channel Message, Slack: Send Channel Message, Slack: Send Channel Message +6 more |
| Branching | 18 step(s): Branching: Filter, Branching: Filter, Branching: Filter +15 more |

---

## Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                             TRIGGER                             │
│  1. GetForm: New Form Submission                                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  2. Code by Zapier: Custom Code                                 │
│  3. Code by Zapier: Custom Code                                 │
│  4. Code by Zapier: Custom Code                                 │
│  5. Code by Zapier: Custom Code                                 │
│  6. Code by Zapier: Custom Code                                 │
│  7. Code by Zapier: Custom Code                                 │
│  8. Code by Zapier: Custom Code                                 │
│  9. Code by Zapier: Custom Code                                 │
│  10. Code by Zapier: Custom Code                                 │
│  11. Googlesheets: Create Spreadsheet Row                        │
│  12. Code by Zapier: Custom Code                                 │
│  13. HubSpot: Update CRM Deal                                    │
│  14. HubSpot: Update CRM Deal                                    │
│  15. HubSpot: Update CRM Deal                                    │
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
│  17. Zapierformatter: datetime_line_item                         │
│  18. Googlemail: Send Email                                      │
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
│  21. Googlemail: Send Email                                      │
│  22. Slack: Send Channel Message                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  23. Branching: Filter                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  24. Googlemail: Send Email                                      │
│  25. Slack: Send Channel Message                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  26. Branching: Filter                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  27. Googlemail: Send Email                                      │
│  28. Slack: Send Channel Message                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  29. Branching: Filter                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  30. Googlemail: Send Email                                      │
│  31. Slack: Send Channel Message                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  32. Branching: Filter                                           │
│  33. Branching: branch                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  34. Code by Zapier: Custom Code                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  35. Branching: Filter                                           │
│  36. Branching: branch                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  37. HubSpot: _zap_raw_request                                   │
│  38. HubSpot: find_associations                                  │
│  39. HubSpot: find_associations                                  │
│  40. HubSpot: find_associations                                  │
│  41. HubSpot: Create Associations                                │
│  42. HubSpot: Create Associations                                │
│  43. HubSpot: Find Deal                                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  44. Branching: Filter                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  45. Googlemail: Send Email                                      │
│  46. Slack: Send Channel Message                                 │
│  47. HubSpot: Create Associations                                │
│  48. HubSpot: Find Deal                                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  49. Branching: Filter                                           │
│  50. Branching: Filter                                           │
│  51. Branching: branch                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  52. HubSpot: Create Associations                                │
│  53. Googlemail: Send Email                                      │
│  54. HubSpot: _zap_raw_request                                   │
│  55. HubSpot: find_associations                                  │
│  56. HubSpot: find_associations                                  │
│  57. HubSpot: find_associations                                  │
│  58. HubSpot: Create Associations                                │
│  59. HubSpot: Find Deal                                          │
│  60. HubSpot: upsert_contact                                     │
│  61. Slack: Send Channel Message                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  62. Branching: Filter                                           │
│  63. Branching: Filter                                           │
│  64. Branching: branch                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  65. HubSpot: Find Company                                       │
│  66. Googlemail: Send Email                                      │
│  67. Slack: Send Channel Message                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  68. Branching: Filter                                           │
│  69. Branching: Filter                                           │
│  70. Branching: branch                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  71. Code by Zapier: Custom Code                                 │
│  72. Googlemail: Send Email                                      │
│  73. Zapierformatter: text_line_item                             │
│  74. Slack: Send Channel Message                                 │
│  75. Googlesheets: Create Spreadsheet Row                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  76. Filter by Zapier: Filter                                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Step-by-Step Breakdown

### Step 1: GetForm: New Form Submission

| Property | Value |
|----------|-------|
| **Type** | ⚡ Trigger |
| **App** | GetForm |
| **Action** | New Form Submission |

### Step 2: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 3: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 4: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 5: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 6: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 7: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 8: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 9: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 10: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 11: Googlesheets: Create Spreadsheet Row

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlesheets |
| **Action** | Create Spreadsheet Row |

### Step 12: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 13: HubSpot: Update CRM Deal

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | Update CRM Deal |

### Step 14: HubSpot: Update CRM Deal

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | Update CRM Deal |

### Step 15: HubSpot: Update CRM Deal

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | Update CRM Deal |

### Step 16: Filter by Zapier: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Filter |
| **App** | Filter by Zapier |
| **Action** | Filter |

### Step 17: Zapierformatter: datetime_line_item

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Zapierformatter |
| **Action** | datetime_line_item |

### Step 18: Googlemail: Send Email

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlemail |
| **Action** | Send Email |

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

### Step 21: Googlemail: Send Email

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlemail |
| **Action** | Send Email |

### Step 22: Slack: Send Channel Message

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Slack |
| **Action** | Send Channel Message |

### Step 23: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 24: Googlemail: Send Email

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlemail |
| **Action** | Send Email |

### Step 25: Slack: Send Channel Message

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Slack |
| **Action** | Send Channel Message |

### Step 26: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 27: Googlemail: Send Email

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlemail |
| **Action** | Send Email |

### Step 28: Slack: Send Channel Message

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Slack |
| **Action** | Send Channel Message |

### Step 29: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 30: Googlemail: Send Email

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlemail |
| **Action** | Send Email |

### Step 31: Slack: Send Channel Message

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Slack |
| **Action** | Send Channel Message |

### Step 32: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 33: Branching: branch

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | branch |

### Step 34: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 35: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 36: Branching: branch

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | branch |

### Step 37: HubSpot: _zap_raw_request

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | _zap_raw_request |

### Step 38: HubSpot: find_associations

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search |
| **App** | HubSpot |
| **Action** | find_associations |

### Step 39: HubSpot: find_associations

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search |
| **App** | HubSpot |
| **Action** | find_associations |

### Step 40: HubSpot: find_associations

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search |
| **App** | HubSpot |
| **Action** | find_associations |

### Step 41: HubSpot: Create Associations

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | Create Associations |

### Step 42: HubSpot: Create Associations

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | Create Associations |

### Step 43: HubSpot: Find Deal

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search_Or_Create |
| **App** | HubSpot |
| **Action** | Find Deal |

### Step 44: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 45: Googlemail: Send Email

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlemail |
| **Action** | Send Email |

### Step 46: Slack: Send Channel Message

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Slack |
| **Action** | Send Channel Message |

### Step 47: HubSpot: Create Associations

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | Create Associations |

### Step 48: HubSpot: Find Deal

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search_Or_Create |
| **App** | HubSpot |
| **Action** | Find Deal |

### Step 49: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 50: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 51: Branching: branch

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | branch |

### Step 52: HubSpot: Create Associations

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | Create Associations |

### Step 53: Googlemail: Send Email

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlemail |
| **Action** | Send Email |

### Step 54: HubSpot: _zap_raw_request

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | _zap_raw_request |

### Step 55: HubSpot: find_associations

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search |
| **App** | HubSpot |
| **Action** | find_associations |

### Step 56: HubSpot: find_associations

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search |
| **App** | HubSpot |
| **Action** | find_associations |

### Step 57: HubSpot: find_associations

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search |
| **App** | HubSpot |
| **Action** | find_associations |

### Step 58: HubSpot: Create Associations

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | Create Associations |

### Step 59: HubSpot: Find Deal

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search_Or_Create |
| **App** | HubSpot |
| **Action** | Find Deal |

### Step 60: HubSpot: upsert_contact

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | upsert_contact |

### Step 61: Slack: Send Channel Message

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Slack |
| **Action** | Send Channel Message |

### Step 62: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 63: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 64: Branching: branch

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | branch |

### Step 65: HubSpot: Find Company

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search_Or_Create |
| **App** | HubSpot |
| **Action** | Find Company |

### Step 66: Googlemail: Send Email

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlemail |
| **Action** | Send Email |

### Step 67: Slack: Send Channel Message

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Slack |
| **Action** | Send Channel Message |

### Step 68: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 69: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 70: Branching: branch

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | branch |

### Step 71: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 72: Googlemail: Send Email

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlemail |
| **Action** | Send Email |

### Step 73: Zapierformatter: text_line_item

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Zapierformatter |
| **Action** | text_line_item |

### Step 74: Slack: Send Channel Message

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Slack |
| **Action** | Send Channel Message |

### Step 75: Googlesheets: Create Spreadsheet Row

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlesheets |
| **Action** | Create Spreadsheet Row |

### Step 76: Filter by Zapier: Filter

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

1. Open [Zap Editor](https://zapier.com/editor/262386682)
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
| February 04, 2026 | Last modified |
| - | Documentation auto-generated |

---

*This documentation was auto-generated from Zapier API data.*
*Last updated: 2026-02-05 15:01*
