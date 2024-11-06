from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from src.core.models import WebhookPayload
from src.core.payload_processor import PayloadDataProcessor


class WebhookRouter:

    def __init__(self, prefix: str = ''):
        self.prefix = prefix
        self.router = APIRouter()

    @staticmethod
    def _generic_handler(processor: PayloadDataProcessor):
        def wrapper(request: Request, payload: dict):
            try:
                payload = WebhookPayload.from_payload(payload)

                processor.process_payload_data(request, payload)
                processor.dispatch_to_service(request, payload)

                return JSONResponse(
                    content={'message': "request processed successfully"},
                    status_code=status.HTTP_200_OK
                )
            except Exception as err:
                # TODO: do proper error handling
                return JSONResponse(
                    content={
                        'message': 'request failed with error',
                        'error': str(err)
                    },
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        return wrapper

    def add_router(self, path: str, processor: PayloadDataProcessor):
        self.router.post(path)(self._generic_handler(processor))

    def get_router(self):
        return self.router
