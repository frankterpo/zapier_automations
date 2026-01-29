# Intercom Demo Email / Slack Automation

> **Status**: ✅ Active (ON)  
> **Location**: Leads  
> **Last Modified**: Apr 30, 2025  
> **Owner**: Dominik Vacikar  

## What This Zap Does

When someone requests a **demo through Intercom** (instead of the website form), this Zap:

1. **Captures** the Intercom conversation
2. **Identifies** it as a demo request
3. **Sends** email notification to sales
4. **Posts** to Slack for team visibility

---

## Why This Exists

Some visitors prefer using Intercom chat to request demos rather than filling out the form. This Zap ensures these leads aren't lost.

---

## Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         TRIGGER                                  │
│  Intercom → New Conversation Started                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         FILTER                                   │
│  Only continue if message contains:                             │
│  • "demo", "meeting", "call", "trial"                           │
│  • Excludes support-type keywords                               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      NOTIFICATIONS                              │
│  1. Email: Send to sales@specter.com                            │
│  2. Slack: Post to #sales-inbound                               │
└─────────────────────────────────────────────────────────────────┘
```

---

## Filter Keywords

### Include (demo request signals)
- "demo"
- "trial"
- "call"
- "meeting"
- "pricing"
- "schedule"

### Exclude (support signals)
- "help"
- "issue"
- "bug"
- "error"
- "broken"

---

## Notifications

### Email
**To**: sales@specter.com  
**Subject**: 🎯 Demo Request via Intercom

### Slack
**Channel**: #sales-inbound
```
💬 Demo Request via Intercom

From: John Smith (john@acme.com)
Company: Acme Corp

Message:
"Hi, I'd like to schedule a demo of your platform..."

Respond in Intercom: [Link]
```

---

## Related Documentation

- [Demo Requests](../demo_requests/README.md) - Main demo flow
- [Intercom Request / Slack](../intercom_request_slack/README.md) - Support requests
