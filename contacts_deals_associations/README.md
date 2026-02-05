# Contacts Deals Associations Automation

> **Status**: ⏸️ Paused (OFF)  
> **Zap ID**: 240869492  
> **Steps**: 5  
> **Last Modified**: December 08, 2025  
> **Last Successful Run**: July 04, 2024 at 08:15 UTC  
> **Editor**: [Open in Zapier](https://zapier.com/editor/240869492)

## Table of Contents
1. [What This Zap Does](#what-this-zap-does)
2. [Apps Used](#apps-used)
3. [Flow Architecture](#flow-architecture)
4. [Step-by-Step Breakdown](#step-by-step-breakdown)
5. [Troubleshooting](#troubleshooting)
6. [How to Modify](#how-to-modify)

---

## What This Zap Does

This automation is triggered by **HubSpot** and performs 4 subsequent actions.

**Trigger**: HubSpot: contactList

**Main Actions**: HubSpot → Zapierformatter

---

## Apps Used

| App | Usage in Zap |
|-----|-------------|
| HubSpot | 4 step(s): HubSpot: contactList, HubSpot: Create Associations, HubSpot: find_associations +1 more |
| Zapierformatter | 1 step(s): Zapierformatter: text_line_item |

---

## Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                             TRIGGER                             │
│  1. HubSpot: contactList                                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  2. HubSpot: Create Associations                                │
│  3. HubSpot: find_associations                                  │
│  4. HubSpot: Find Company                                       │
│  5. Zapierformatter: text_line_item                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Step-by-Step Breakdown

### Step 1: HubSpot: contactList

| Property | Value |
|----------|-------|
| **Type** | ⚡ Trigger |
| **App** | HubSpot |
| **Action** | contactList |

### Step 2: HubSpot: Create Associations

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | Create Associations |

### Step 3: HubSpot: find_associations

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search |
| **App** | HubSpot |
| **Action** | find_associations |

### Step 4: HubSpot: Find Company

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search |
| **App** | HubSpot |
| **Action** | Find Company |

### Step 5: Zapierformatter: text_line_item

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | Zapierformatter |
| **Action** | text_line_item |

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

1. Open [Zap Editor](https://zapier.com/editor/240869492)
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
*Last updated: 2026-02-05 14:32*
