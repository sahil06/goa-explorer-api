from typing import List
from pydantic import BaseModel
from app.domain.enums.enums import RouteDifficulty, RoadType, SurfaceType, TrafficLevel


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