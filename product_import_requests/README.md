# Product Import Requests Automation

> **Status**: ⏸️ Paused (OFF)  
> **Zap ID**: 203988472  
> **Steps**: 13  
> **Last Modified**: December 26, 2025  
> **Last Successful Run**: January 20, 2025 at 12:37 UTC  
> **Editor**: [Open in Zapier](https://zapier.com/editor/203988472)

## Table of Contents
1. [What This Zap Does](#what-this-zap-does)
2. [Apps Used](#apps-used)
3. [Flow Architecture](#flow-architecture)
4. [Step-by-Step Breakdown](#step-by-step-breakdown)
5. [Troubleshooting](#troubleshooting)
6. [How to Modify](#how-to-modify)

---

## What This Zap Does

This automation is triggered by **Slack** and performs 12 subsequent actions.

**Trigger**: Slack: Send Channel Message

**Main Actions**: Googlesheets → Notion → Code by Zapier → Zapierformatter

---

## Apps Used

| App | Usage in Zap |
|-----|-------------|
| Slack | 1 step(s): Slack: Send Channel Message |
| Googlesheets | 2 step(s): Googlesheets: Create Spreadsheet Row, Googlesheets: Create Spreadsheet Row |
| Notion | 2 step(s): Notion: create_database_item, Notion: create_database_item |
| Code by Zapier | 2 step(s): Code by Zapier: Custom Code, Code by Zapier: Custom Code |
| Zapierformatter | 2 step(s): Zapierformatter: text_line_item, Zapierformatter: text_line_item |
| Branching | 3 step(s): Branching: Filter, Branching: Filter, Branching: branch |
| Filter by Zapier | 1 step(s): Filter by Zapier: Filter |

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
│  2. Googlesheets: Create Spreadsheet Row                        │
│  3. Googlesheets: Create Spreadsheet Row                        │
│  4. Notion: create_database_item                                │
│  5. Code by Zapier: Custom Code                                 │
│  6. Zapierformatter: text_line_item                             │
│  7. Zapierformatter: text_line_item                             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  8. Branching: Filter                                           │
│  9. Branching: Filter                                           │
│  10. Branching: branch                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  11. Notion: create_database_item                                │
│  12. Code by Zapier: Custom Code                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  13. Filter by Zapier: Filter                                    │
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

### Step 2: Googlesheets: Create Spreadsheet Row

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlesheets |
| **Action** | Create Spreadsheet Row |

### Step 3: Googlesheets: Create Spreadsheet Row

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Googlesheets |
| **Action** | Create Spreadsheet Row |

### Step 4: Notion: create_database_item

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Notion |
| **Action** | create_database_item |

### Step 5: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 6: Zapierformatter: text_line_item

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Zapierformatter |
| **Action** | text_line_item |

### Step 7: Zapierformatter: text_line_item

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Zapierformatter |
| **Action** | text_line_item |

### Step 8: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 9: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 10: Branching: branch

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | branch |

### Step 11: Notion: create_database_item

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Notion |
| **Action** | create_database_item |

### Step 12: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 13: Filter by Zapier: Filter

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

1. Open [Zap Editor](https://zapier.com/editor/203988472)
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
| December 26, 2025 | Last modified |
| - | Documentation auto-generated |

---

*This documentation was auto-generated from Zapier API data.*
*Last updated: 2026-02-05 14:32*
