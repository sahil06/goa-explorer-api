from pydantic import BaseModel
from typing import List
from app.domain.enums.enums import RouteDifficulty, RoadType, SurfaceType, TrafficLevel


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