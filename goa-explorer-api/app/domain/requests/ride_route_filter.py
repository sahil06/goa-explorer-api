from pydantic import BaseModel
from typing import Optional

from app.domain.enums.enums import RoadType, RouteDifficulty, SurfaceType, TrafficLevel

class RideRouteFilter(BaseModel):
    difficulty: Optional[RouteDifficulty] = None
    road_type: Optional[RoadType] = None
    surface: Optional[SurfaceType] = None
    traffic: Optional[TrafficLevel] = None
    min_distance_km: Optional[int] = None
    max_distance_km: Optional[int] = None