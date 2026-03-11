from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.logger import get_logger
from app.core.exceptions import DomainException, NotFoundException, ValidationException

logger = get_logger(__name__)


async def domain_exception_handler(request: Request, exc: DomainException):
    logger.warning(
        f"Domain exception occurred | path={request.url.path} | error={str(exc)}"
    )

    return JSONResponse(
        status_code=400,
        content={
            "error": str(exc),
            "type": exc.__class__.__name__,
        },
    )


async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(
        f"Unhandled exception | path={request.url.path} | error={str(exc)}",
        exc_info=True,
    )

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "type": "ServerError",
        },
    )

async def validation_exception_handler(request: Request, exc: ValidationException):
    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "error": str(exc),
        },
    )

async def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "error": str(exc),
        },
    )
