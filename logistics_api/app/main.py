from fastapi import FastAPI
from app.core.database import engine
from app.core.database import Base
from app.api.router import api_router
from app.middleware.cors import setup_cors
from app.middleware.logging_middleware import LoggingMiddleware
from app.exceptions.exception_handlers import register_exception_handlers

app = FastAPI(title="Logistics API")

Base.metadata.create_all(bind=engine)
# Routers
app.include_router(api_router)

# Middleware
setup_cors(app)
app.add_middleware(LoggingMiddleware)

# Exception Handlers
register_exception_handlers(app)