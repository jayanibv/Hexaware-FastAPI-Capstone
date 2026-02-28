from fastapi import Request, HTTPException
import time

REQUEST_LIMIT = 100
WINDOW_TIME = 60

request_counts = {}


async def rate_limiter(request: Request):
    ip = request.client.host
    current_time = time.time()

    if ip not in request_counts:
        request_counts[ip] = []

    request_counts[ip] = [
        timestamp for timestamp in request_counts[ip]
        if current_time - timestamp < WINDOW_TIME
    ]

    if len(request_counts[ip]) >= REQUEST_LIMIT:
        raise HTTPException(status_code=429, detail="Too many requests")

    request_counts[ip].append(current_time)