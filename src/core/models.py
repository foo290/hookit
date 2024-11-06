from typing import List, Dict, Any

from src.core.base import WebhookEventBase, EventPriority, WebhookPayloadBase


class WebhookEvent(WebhookEventBase):
    def __init__(
            self, event_name: str,
            event_type: str = 'default',
            event_priority: str = EventPriority.NORMAL
    ):
        self.event_name = event_name
        self.event_type = event_type
        self.event_priority = event_priority


class WebhookPayload(WebhookPayloadBase):
    def __init__(self):
        super().__init__()

