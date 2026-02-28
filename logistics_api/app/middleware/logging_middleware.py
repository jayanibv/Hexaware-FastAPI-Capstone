import time
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):
        start_time = time.time()

        response = await call_next(request)

        process_time = time.time() - start_time
        print(
            f"{request.method} {request.url.path} "
            f"completed in {process_time:.4f}s "
            f"status={response.status_code}"
        )

        return response