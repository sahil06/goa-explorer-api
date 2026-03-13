from pydantic import BaseModel
from typing import Optional
from app.domain.enums.road_type import RoadType
from app.domain.enums.route_difficulty import RouteDifficulty
from app.domain.enums.surface_type import SurfaceType
from app.domain.enums.traffic_level import TrafficLevel


class RideRouteFilter(BaseModel):
    difficulty: Optional[RouteDifficulty] = None
    road_type: Optional[RoadType] = None
    surface: Optional[SurfaceType] = None
    traffic: Optional[TrafficLevel] = None
    min_distance_km: Optional[int] = None
    max_distance_km: Optional[int] = None