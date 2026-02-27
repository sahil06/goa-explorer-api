from dataclasses import dataclass
from typing import List
from app.domain.enums import RouteDifficulty, RoadType, SurfaceType, TrafficLevel


@dataclass
class RideRoute:
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