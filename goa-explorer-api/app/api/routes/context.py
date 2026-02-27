from fastapi import APIRouter, Depends, Query
from app.api.dependencies import get_exploration_service
from app.api.schemas.context_request import ContextRequest
from app.api.schemas.context_response import ContextInfoResponse
from app.mappers.context_mapper import ContextMapper
from app.queries.context_query import ContextQuery
from app.services.exploration_service import ExplorationService

router = APIRouter(prefix="/explore", tags=["Explore"])


@router.post("/context", response_model=ContextInfoResponse)
def get_context(
    request: ContextRequest,
    service: ExplorationService = Depends(get_exploration_service),
):
    query = ContextQuery(
        location_id=request.location_id,
        day_type=request.day_type,
        time_of_day=request.time_of_day,
    )

    context = service.get_context_info(query)
    return ContextMapper.to_response(context)