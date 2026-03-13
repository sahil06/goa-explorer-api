from pydantic import BaseModel, Field
from typing import List
from app.domain.enums.crowd_level import CrowdLevel
from app.domain.enums.location_type import LocationType
from app.domain.enums.region import Region
from app.domain.enums.time_of_day import TimeOfDay
from app.domain.enums.vibe import Vibe


class LocationResponse(BaseModel):
    id: str = Field(example="loc_001")
    name: str = Field(example="Baga Beach")
    region: Region = Field(example="north")
    type: LocationType = Field(example="beach")
    vibe: List[Vibe] = Field(example=["party", "mixed"])
    best_time_of_day: List[TimeOfDay] = Field(example=["afternoon", "sunset"])
    crowd_level_weekday: CrowdLevel = Field(example="medium")
    crowd_level_weekend: CrowdLevel = Field(example="high")
    short_description: str = Field(
        example="Energetic beach known for nightlife and water sports."
    )

    class Config:
        from_attributes = True


class LocationListResponse(BaseModel):
    total: int
    items: List[LocationResponse]