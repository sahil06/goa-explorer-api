from fastapi import APIRouter, Depends
from app.services.health_service import HealthService
from app.api.dependencies import get_health_service
from app.api.schemas.responses.health_response import HealthResponse

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("", response_model=HealthResponse)
async def health_check(
    service: HealthService = Depends(get_health_service)
):
    result = await service.get_health()

    return HealthResponse(
        service=result.service,
        status=result.status,
        details=result.details
    )
