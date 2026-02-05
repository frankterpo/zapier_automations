# Deal Renewed Automation

> **Status**: ✅ Active (ON)  
> **Zap ID**: 236426171  
> **Steps**: 7  
> **Last Modified**: December 08, 2025  
> **Last Successful Run**: September 01, 2025 at 14:32 UTC  
> **Editor**: [Open in Zapier](https://zapier.com/editor/236426171)

## Table of Contents
1. [What This Zap Does](#what-this-zap-does)
2. [Apps Used](#apps-used)
3. [Flow Architecture](#flow-architecture)
4. [Step-by-Step Breakdown](#step-by-step-breakdown)
5. [Troubleshooting](#troubleshooting)
6. [How to Modify](#how-to-modify)

---

## What This Zap Does

This automation is triggered by **HubSpot** and performs 6 subsequent actions.

**Trigger**: HubSpot: updated_deal_stage

**Main Actions**: Zapierformatter → Ai → Code by Zapier → Slack → Googlesheets

---

## Apps Used

| App | Usage in Zap |
|-----|-------------|
| HubSpot | 1 step(s): HubSpot: updated_deal_stage |
| Zapierformatter | 1 step(s): Zapierformatter: text_line_item |
| Ai | 1 step(s): Ai: get_completion |
| Code by Zapier | 2 step(s): Code by Zapier: Custom Code, Code by Zapier: Custom Code |
| Slack | 1 step(s): Slack: Send Channel Message |
| Googlesheets | 1 step(s): Googlesheets: Create Spreadsheet Row |

---

## Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                             TRIGGER                             │
│  1. HubSpot: updated_deal_stage                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  2. Zapierformatter: text_line_item                             │
│  3. Ai: get_completion                                          │
│  4. Code by Zapier: Custom Code                                 │
│  5. Code by Zapier: Custom Code                                 │
│  6. Slack: Send Channel Message                                 │
│  7. Googlesheets: Create Spreadsheet Row                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Step-by-Step Breakdown

### Step 1: HubSpot: updated_deal_stage

| Property | Value |
|----------|-------|
| **Type** | ⚡ Trigger |
| **App** | HubSpot |
| **Action** | updated_deal_stage |

### Step 2: Zapierformatter: text_line_item

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Zapierformatter |
| **Action** | text_line_item |

### Step 3: Ai: get_completion

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Ai |
| **Action** | get_completion |

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

### Step 6: Slack: Send Channel Message

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Slack |
| **Action** | Send Channel Message |

### Step 7: Googlesheets: Create Spreadsheet Row

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlesheets |
| **Action** | Create Spreadsheet Row |

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

1. Open [Zap Editor](https://zapier.com/editor/236426171)
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
| December 08, 2025 | Last modified |
| - | Documentation auto-generated |

---

*This documentation was auto-generated from Zapier API data.*
*Last updated: 2026-02-05 15:01*
