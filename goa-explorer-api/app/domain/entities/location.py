from dataclasses import dataclass
from typing import List
from app.domain.enums import Region, LocationType, Vibe, TimeOfDay, CrowdLevel


@dataclass
class Location:
    id: str
    name: str
    region: Region
    type: LocationType
    vibe: List[Vibe]
    best_time_of_day: List[TimeOfDay]
    crowd_level_weekday: CrowdLevel
    crowd_level_weekend: CrowdLevel
    short_description: str