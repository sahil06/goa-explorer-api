from pydantic import BaseModel
from typing import List
from app.domain.enums.road_type import RoadType
from app.domain.enums.route_difficulty import RouteDifficulty
from app.domain.enums.surface_type import SurfaceType
from app.domain.enums.traffic_level import TrafficLevel


class RideRouteResponse(BaseModel):
    id: str
    name: str
    start_location: str
    end_location: str
    distance_km: float
    difficulty: RouteDifficulty
    road_type: RoadType
    surface: SurfaceType
    traffic_level: TrafficLevel
    highlights: List[str]

    class Config:
        from_attributes = True


class RideRouteListResponse(BaseModel):
    total: int
    items: List[RideRouteResponse]