from __future__ import annotations

from src.core.models import WebhookPayload
from abc import abstractmethod, ABC

from fastapi import Request


class PayloadDataProcessor(ABC):

    @abstractmethod
    def process_payload_data(self, request: Request, payload: WebhookPayload):
        raise NotImplemented

    @abstractmethod
    def dispatch_to_service(self, request: Request, processed_payload: WebhookPayload):
        raise NotImplemented



