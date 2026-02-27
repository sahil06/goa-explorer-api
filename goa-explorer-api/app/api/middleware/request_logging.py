import time
import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.logger import get_logger

logger = get_logger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        start_time = time.time()

        logger.info(
            f"Request started | id={request_id} | "
            f"method={request.method} | path={request.url.path}"
        )

        response = await call_next(request)

        duration = round((time.time() - start_time) * 1000, 2)

        logger.info(
            f"Request completed | id={request_id} | "
            f"status={response.status_code} | duration={duration}ms"
        )

        response.headers["X-Request-ID"] = request_id
        return response
