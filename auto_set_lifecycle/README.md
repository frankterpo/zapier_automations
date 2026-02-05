# Auto Set Lifecycle Automation

> **Status**: ✅ Active (ON)  
> **Zap ID**: 300616653  
> **Steps**: 8  
> **Last Modified**: December 08, 2025  
> **Last Successful Run**: May 29, 2025 at 16:06 UTC  
> **Editor**: [Open in Zapier](https://zapier.com/editor/300616653)

## Table of Contents
1. [What This Zap Does](#what-this-zap-does)
2. [Apps Used](#apps-used)
3. [Flow Architecture](#flow-architecture)
4. [Step-by-Step Breakdown](#step-by-step-breakdown)
5. [Troubleshooting](#troubleshooting)
6. [How to Modify](#how-to-modify)

---

## What This Zap Does

This automation is triggered by **HubSpot** and performs 7 subsequent actions.

**Trigger**: HubSpot: deal_property_change_resthook

**Main Actions**: HubSpot

---

## Apps Used

| App | Usage in Zap |
|-----|-------------|
| HubSpot | 4 step(s): HubSpot: deal_property_change_resthook, HubSpot: update_crm_company, HubSpot: update_crm_company +1 more |
| Filter by Zapier | 1 step(s): Filter by Zapier: Filter |
| Branching | 3 step(s): Branching: Filter, Branching: Filter, Branching: branch |

---

## Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                             TRIGGER                             │
│  1. HubSpot: deal_property_change_resthook                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  2. Filter by Zapier: Filter                                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  3. HubSpot: update_crm_company                                 │
│  4. HubSpot: update_crm_company                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                              LOGIC                              │
│  5. Branching: Filter                                           │
│  6. Branching: Filter                                           │
│  7. Branching: branch                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                             ACTIONS                             │
│  8. HubSpot: Find Company                                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## Step-by-Step Breakdown

### Step 1: HubSpot: deal_property_change_resthook

| Property | Value |
|----------|-------|
| **Type** | ⚡ Trigger |
| **App** | HubSpot |
| **Action** | deal_property_change_resthook |

### Step 2: Filter by Zapier: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Filter |
| **App** | Filter by Zapier |
| **Action** | Filter |

### Step 3: HubSpot: update_crm_company

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | update_crm_company |

### Step 4: HubSpot: update_crm_company

| Property | Value |
|----------|-------|
| **Type** | ▶️ Action |
| **App** | HubSpot |
| **Action** | update_crm_company |

### Step 5: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 6: Branching: Filter

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | Filter |

### Step 7: Branching: branch

| Property | Value |
|----------|-------|
| **Type** | 🔀 Path |
| **App** | Branching |
| **Action** | branch |

### Step 8: HubSpot: Find Company

| Property | Value |
|----------|-------|
| **Type** | 🔍 Search |
| **App** | HubSpot |
| **Action** | Find Company |

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

1. Open [Zap Editor](https://zapier.com/editor/300616653)
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
