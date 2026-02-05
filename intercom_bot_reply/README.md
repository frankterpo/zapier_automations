# Intercom Bot Reply Automation

> **Status**: ⏸️ Paused (OFF)  
> **Zap ID**: 266596665  
> **Steps**: 6  
> **Last Modified**: January 20, 2026  
> **Last Successful Run**: November 05, 2025 at 19:34 UTC  
> **Editor**: [Open in Zapier](https://zapier.com/editor/266596665)

## Table of Contents
1. [What This Zap Does](#what-this-zap-does)
2. [Apps Used](#apps-used)
3. [Flow Architecture](#flow-architecture)
4. [Step-by-Step Breakdown](#step-by-step-breakdown)
5. [Troubleshooting](#troubleshooting)
6. [How to Modify](#how-to-modify)

---

## What This Zap Does

This automation is triggered by **Intercom** and performs 5 subsequent actions.

**Trigger**: Intercom: contact_replied

**Main Actions**: Ai → Code by Zapier → Slack

---

## Apps Used

| App | Usage in Zap |
|-----|-------------|
| Intercom | 1 step(s): Intercom: contact_replied |
| Ai | 1 step(s): Ai: get_completion |
| Filter by Zapier | 2 step(s): Filter by Zapier: Filter, Filter by Zapier: Filter |
| Code by Zapier | 1 step(s): Code by Zapier: Custom Code |
| Slack | 1 step(s): Slack: Send Channel Message |

---

## Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                             TRIGGER                             │
│  1. Intercom: contact_replied                                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  2. Ai: get_completion                                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  3. Filter by Zapier: Filter                                    │
│  4. Filter by Zapier: Filter                                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  5. Code by Zapier: Custom Code                                 │
│  6. Slack: Send Channel Message                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Step-by-Step Breakdown

### Step 1: Intercom: contact_replied

| Property | Value |
|----------|-------|
| **Type** | ⚡ Trigger |
| **App** | Intercom |
| **Action** | contact_replied |

### Step 2: Ai: get_completion

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Ai |
| **Action** | get_completion |

### Step 3: Filter by Zapier: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Filter |
| **App** | Filter by Zapier |
| **Action** | Filter |

### Step 4: Filter by Zapier: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Filter |
| **App** | Filter by Zapier |
| **Action** | Filter |

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

1. Open [Zap Editor](https://zapier.com/editor/266596665)
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
| January 20, 2026 | Last modified |
| - | Documentation auto-generated |

---

*This documentation was auto-generated from Zapier API data.*
*Last updated: 2026-02-05 14:32*
