from fastapi import APIRouter, Depends
from typing import Optional
from app.api.schemas.responses.location_response import LocationListResponse
from app.domain.enums.enums import Region, LocationType, Vibe
from app.domain.requests.location_filter import LocationFilter
from app.mappers.location_mapper import LocationMapper
from app.services.exploration_service import ExplorationService
from app.api.dependencies import get_exploration_service

router = APIRouter(prefix="/explore", tags=["Explore"])


@router.get("/locations", response_model=LocationListResponse)
def get_locations(
    region: Optional[Region] = None,
    type: Optional[LocationType] = None,
    vibe: Optional[Vibe] = None,
    service: ExplorationService = Depends(get_exploration_service),
):
    filters = LocationFilter(region=region, type=type, vibe=vibe)
    locations = service.list_locations(filters)
    return LocationMapper.to_list_response(locations)