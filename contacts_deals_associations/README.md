# Contacts to Deals Associations

> **Status**: ✅ Active (ON)  
> **Location**: CS  
> **Last Modified**: Dec 11, 2024  
> **Owner**: Dominik Vacikar  

## What This Zap Does

Ensures proper **HubSpot associations** between contacts and deals when they're missing:

1. **Monitors** deal creation/updates in HubSpot
2. **Checks** if deal has associated contacts
3. **Creates** missing associations based on company contacts

---

## Why This Exists

### Business Problem Solved
- Deals created via API sometimes lacked contact associations
- Manual association was time-consuming
- Reporting was incomplete without proper links

### Value Delivered
- Complete deal-contact relationships
- Accurate reporting on contacts per deal
- Better communication tracking

---

## Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         TRIGGER                                  │
│  HubSpot → Deal Created/Updated                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     CHECK ASSOCIATIONS                          │
│  Does deal have associated contacts?                            │
└─────────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              │ No                            │ Yes
              ▼                               ▼
┌─────────────────────────┐     ┌─────────────────────────┐
│  Get Company Contacts   │     │   Do Nothing            │
│  ↓                      │     │   (Already linked)      │
│  Associate to Deal      │     └─────────────────────────┘
└─────────────────────────┘
```

---

## Trigger

**App**: HubSpot  
**Event**: Deal Created or Updated  
**Filter**: Deal has associated company but no contacts

---

## Actions

1. **Find Associated Company** - Get company linked to deal
2. **Find Company Contacts** - Get all contacts for that company
3. **Associate Contacts** - Link contacts to the deal

---

## Association Types Created

| Association | Type ID | Description |
|-------------|---------|-------------|
| Deal → Contact | 3 | Standard deal-to-contact |
| Contact → Deal | 4 | Reverse association |

---

## Related Documentation

- [Demo Requests](../demo_requests/README.md) - Creates associations during lead processing
