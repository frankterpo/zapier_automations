# Intercom Demo Email Automation

> **Status**: ✅ Active (ON)  
> **Zap ID**: 207157349  
> **Steps**: 12  
> **Last Modified**: October 07, 2025  
> **Last Successful Run**: July 19, 2024 at 14:11 UTC  
> **Editor**: [Open in Zapier](https://zapier.com/editor/207157349)

## Table of Contents
1. [What This Zap Does](#what-this-zap-does)
2. [Apps Used](#apps-used)
3. [Flow Architecture](#flow-architecture)
4. [Step-by-Step Breakdown](#step-by-step-breakdown)
5. [Troubleshooting](#troubleshooting)
6. [How to Modify](#how-to-modify)

---

## What This Zap Does

This automation is triggered by **Googlemail** and performs 11 subsequent actions.

**Trigger**: Googlemail: Send Email

**Main Actions**: HubSpot → Slack → Code by Zapier

---

## Apps Used

| App | Usage in Zap |
|-----|-------------|
| Googlemail | 1 step(s): Googlemail: Send Email |
| HubSpot | 8 step(s): HubSpot: _zap_raw_request, HubSpot: find_associations, HubSpot: find_associations +5 more |
| Slack | 1 step(s): Slack: Send Channel Message |
| Code by Zapier | 1 step(s): Code by Zapier: Custom Code |
| Filter by Zapier | 1 step(s): Filter by Zapier: Filter |

---

## Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                             TRIGGER                             │
│  1. Googlemail: Send Email                                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  2. HubSpot: _zap_raw_request                                   │
│  3. HubSpot: find_associations                                  │
│  4. HubSpot: find_associations                                  │
│  5. HubSpot: Create Associations                                │
│  6. HubSpot: Create Associations                                │
│  7. HubSpot: Find Deal                                          │
│  8. HubSpot: upsert_contact                                     │
│  9. HubSpot: Find Company                                       │
│  10. Slack: Send Channel Message                                 │
│  11. Code by Zapier: Custom Code                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  12. Filter by Zapier: Filter                                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Step-by-Step Breakdown

### Step 1: Googlemail: Send Email

| Property | Value |
|----------|-------|
| **Type** | ⚡ Trigger |
| **App** | Googlemail |
| **Action** | Send Email |

### Step 2: HubSpot: _zap_raw_request

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | _zap_raw_request |

### Step 3: HubSpot: find_associations

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search |
| **App** | HubSpot |
| **Action** | find_associations |

### Step 4: HubSpot: find_associations

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search |
| **App** | HubSpot |
| **Action** | find_associations |

### Step 5: HubSpot: Create Associations

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | Create Associations |

### Step 6: HubSpot: Create Associations

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | Create Associations |

### Step 7: HubSpot: Find Deal

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search_Or_Create |
| **App** | HubSpot |
| **Action** | Find Deal |

### Step 8: HubSpot: upsert_contact

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | upsert_contact |

### Step 9: HubSpot: Find Company

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search_Or_Create |
| **App** | HubSpot |
| **Action** | Find Company |

### Step 10: Slack: Send Channel Message

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Slack |
| **Action** | Send Channel Message |

### Step 11: Code by Zapier: Custom Code

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Code by Zapier |
| **Action** | Custom Code |

### Step 12: Filter by Zapier: Filter

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

1. Open [Zap Editor](https://zapier.com/editor/207157349)
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
| October 07, 2025 | Last modified |
| - | Documentation auto-generated |

---

*This documentation was auto-generated from Zapier API data.*
*Last updated: 2026-02-05 15:01*
