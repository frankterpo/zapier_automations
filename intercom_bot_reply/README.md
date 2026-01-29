# Intercom Bot Reply / Slack

> **Status**: ✅ Active (ON)  
> **Location**: CS  
> **Last Modified**: Nov 10, 2025  
> **Owner**: Dominik Vacikar  

## What This Zap Does

Monitors Intercom bot conversations and alerts the team when:

1. **Bot conversation** starts with a user
2. **User responds** to bot message
3. **Bot can't handle** the request (needs human)

---

## Why This Exists

### Business Problem Solved
- Bot conversations went unmonitored
- Users sometimes got stuck with bot
- No visibility into bot effectiveness

### Value Delivered
- Human takeover when bot fails
- Visibility into bot interactions
- Faster escalation to support team

---

## Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         TRIGGER                                  │
│  Intercom → Conversation with Bot Participant                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         FILTER                                   │
│  • Bot is participant                                           │
│  • User has replied                                             │
│  • Conversation is open                                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      SLACK NOTIFICATION                         │
│  Post to #support-bot-alerts                                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Trigger

**App**: Intercom  
**Event**: Conversation Updated  
**Filter**: Bot is a participant AND user has replied

---

## Slack Message

**Channel**: #support-bot-alerts

```
🤖 Bot Conversation Activity

User: John Smith (john@acme.com)
Company: Acme Corp
Status: User replied to bot

Preview: "Actually, I need help with something else..."

Take over: [Intercom Link]
```

---

## Related Documentation

- [Intercom Request / Slack](../intercom_request_slack/README.md) - Direct support requests
- [Intercom Demo Email / Slack](../intercom_demo_email/README.md) - Demo requests via chat
