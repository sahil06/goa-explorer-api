from fastapi import FastAPI
from app.core.config import settings
from app.api.routes.health import router as health_router
from app.api.routes.locations import router as locations_router
from app.api.routes.ride_routes import router as ride_routes_router
from app.api.routes.context import router as context_router
from app.core.logger import setup_logger
from app.api.middleware.request_logging import RequestLoggingMiddleware
from app.api.exception_handlers import (
    domain_exception_handler,
    generic_exception_handler,
    validation_exception_handler,
    not_found_exception_handler
)
from app.core.exceptions import DomainException, NotFoundException, ValidationException

setup_logger()
app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,)

app.include_router(health_router, prefix=settings.api_v1_prefix)
app.include_router(locations_router, prefix=settings.api_v1_prefix)
app.include_router(ride_routes_router, prefix=settings.api_v1_prefix)
app.include_router(context_router, prefix=settings.api_v1_prefix)
app.add_middleware(RequestLoggingMiddleware)
app.add_exception_handler(ValidationException, validation_exception_handler)
app.add_exception_handler(NotFoundException, not_found_exception_handler)
app.add_exception_handler(DomainException, domain_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

@app.get("/")
def root():
    return {"message": "API is running"}
