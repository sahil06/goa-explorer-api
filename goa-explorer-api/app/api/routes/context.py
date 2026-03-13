from fastapi import APIRouter, Depends
from app.api.dependencies import get_exploration_service
from app.api.schemas.requests.context_request_schema import ContextRequestSchema
from app.api.schemas.responses.context_response import ContextInfoResponse
from app.domain.requests.context_request import ContextRequest
from app.mappers.context_mapper import ContextMapper
from app.services.exploration_service import ExplorationService

router = APIRouter(prefix="/explore", tags=["Explore"])


@router.post("/context", response_model=ContextInfoResponse)
def get_context(
    request: ContextRequestSchema,
    service: ExplorationService = Depends(get_exploration_service),
):
    domain_request = ContextMapper.to_domain_request(request)
    context = service.get_context_info(domain_request)
    return ContextMapper.to_response(context)