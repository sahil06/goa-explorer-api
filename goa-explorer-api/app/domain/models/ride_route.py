from typing import List
from pydantic import BaseModel
from app.domain.enums.road_type import RoadType
from app.domain.enums.route_difficulty import RouteDifficulty
from app.domain.enums.surface_type import SurfaceType
from app.domain.enums.traffic_level import TrafficLevel


class RideRoute(BaseModel):
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