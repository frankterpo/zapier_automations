# Arr Update Automation

> **Status**: ✅ Active (ON)  
> **Zap ID**: 186806230  
> **Steps**: 2  
> **Last Modified**: December 19, 2025  
> **Last Successful Run**: February 06, 2025 at 03:06 UTC  
> **Editor**: [Open in Zapier](https://zapier.com/editor/186806230)

## Table of Contents
1. [What This Zap Does](#what-this-zap-does)
2. [Apps Used](#apps-used)
3. [Flow Architecture](#flow-architecture)
4. [Step-by-Step Breakdown](#step-by-step-breakdown)
5. [Troubleshooting](#troubleshooting)
6. [How to Modify](#how-to-modify)

---

## What This Zap Does

This automation is triggered by **Googlesheets** and performs 1 subsequent actions.

**Trigger**: Googlesheets: updated_row

**Main Actions**: Slack

---

## Apps Used

| App | Usage in Zap |
|-----|-------------|
| Googlesheets | 1 step(s): Googlesheets: updated_row |
| Slack | 1 step(s): Slack: Send Direct Message |

---

## Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                             TRIGGER                             │
│  1. Googlesheets: updated_row                                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  2. Slack: Send Direct Message                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Step-by-Step Breakdown

### Step 1: Googlesheets: updated_row

| Property | Value |
|----------|-------|
| **Type** | ⚡ Trigger |
| **App** | Googlesheets |
| **Action** | updated_row |

### Step 2: Slack: Send Direct Message

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Slack |
| **Action** | Send Direct Message |

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

1. Open [Zap Editor](https://zapier.com/editor/186806230)
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
| December 19, 2025 | Last modified |
| - | Documentation auto-generated |

---

*This documentation was auto-generated from Zapier API data.*
*Last updated: 2026-02-05 15:01*
