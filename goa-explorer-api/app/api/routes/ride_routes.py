from fastapi import APIRouter, Depends, Query
from typing import List, Optional

from app.api.schemas.responses.ride_route_response import RideRouteListResponse
from app.mappers.ride_route_mapper import RideRouteMapper
from app.services.exploration_service import ExplorationService
from app.domain.requests.ride_route_filter import RideRouteFilter
from app.domain.enums.enums import (
    RouteDifficulty,
    RoadType,
    SurfaceType,
    TrafficLevel,
)
from app.api.dependencies import get_exploration_service

router = APIRouter(prefix="/explore", tags=["Explore"])


@router.get("/ride-routes", response_model=RideRouteListResponse)
def list_ride_routes(
    difficulty: Optional[RouteDifficulty] = Query(None),
    road_type: Optional[RoadType] = Query(None),
    surface: Optional[SurfaceType] = Query(None),
    traffic: Optional[TrafficLevel] = Query(None),
    min_distance_km: Optional[int] = Query(None),
    max_distance_km: Optional[int] = Query(None),
    service: ExplorationService = Depends(get_exploration_service),
):
    filters = RideRouteFilter(
        difficulty=difficulty,
        road_type=road_type,
        surface=surface,
        traffic=traffic,
        min_distance_km=min_distance_km,
        max_distance_km=max_distance_km,
    )

    routes = service.list_ride_routes(filters)
    return RideRouteMapper.to_list_response(routes)