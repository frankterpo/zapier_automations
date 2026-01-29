# Intercom Request / Slack Automation

> **Status**: ✅ Active (ON)  
> **Location**: CS  
> **Last Modified**: Jan 16, 2026  
> **Owner**: Dominik Vacikar  

## Table of Contents
1. [What This Zap Does](#what-this-zap-does)
2. [Why This Exists](#why-this-exists)
3. [Flow Architecture](#flow-architecture)
4. [Filter Conditions](#filter-conditions)
5. [Slack Message Format](#slack-message-format)

---

## What This Zap Does

When a **customer support request** comes through Intercom (that isn't handled by the bot), this Zap:

1. **Captures** the Intercom conversation
2. **Filters** to exclude bot-handled conversations
3. **Posts** to Slack for team visibility
4. **Links** directly to the Intercom conversation

---

## Why This Exists

### Business Problem Solved
- **Response Time**: Support requests were missed
- **Visibility**: Team didn't know when help was needed
- **Prioritization**: No way to see urgent requests quickly

### Value Delivered
- Real-time support request alerts
- Reduced average response time
- Better customer experience

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
│  Only continue if:                                              │
│  • NOT initiated by bot                                         │
│  • NOT a demo request (handled by other Zap)                    │
│  • NOT a newsletter signup                                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      SLACK NOTIFICATION                         │
│  Post to #support-requests channel                              │
└─────────────────────────────────────────────────────────────────┘
```

---

## Filter Conditions

### Include
- Conversation type = "user"
- Source = "messenger" or "email"

### Exclude
- Bot-initiated conversations
- Conversations containing "demo" in first message
- Auto-reply conversations

---

## Slack Message Format

**Channel**: #support-requests

```
🆘 New Support Request

From: John Smith (john@acme.com)
Company: Acme Corp
Time: Jan 29, 2026, 2:30 PM

Message Preview:
"I'm having trouble exporting my data. When I click the export button..."

View in Intercom: [Link]
```

---

## Related Documentation

- [Intercom Demo Email / Slack](../intercom_demo_email/README.md) - Demo requests
- [Intercom Bot Reply / Slack](../intercom_bot_reply/README.md) - Bot interactions
