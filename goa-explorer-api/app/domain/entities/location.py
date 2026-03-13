from typing import List
from pydantic import BaseModel
from app.domain.enums.crowd_level import CrowdLevel
from app.domain.enums.location_type import LocationType
from app.domain.enums.region import Region
from app.domain.enums.time_of_day import TimeOfDay
from app.domain.enums.vibe import Vibe


class Location(BaseModel):
    id: str
    name: str
    region: Region
    type: LocationType
    vibe: List[Vibe]
    best_time_of_day: List[TimeOfDay]
    crowd_level_weekday: CrowdLevel
    crowd_level_weekend: CrowdLevel
    short_description: str