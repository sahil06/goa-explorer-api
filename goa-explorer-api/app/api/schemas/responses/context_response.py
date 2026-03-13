from pydantic import BaseModel
from app.domain.enums.day_type import DayType
from app.domain.enums.crowd_level import CrowdLevel
from app.domain.enums.time_of_day import TimeOfDay


class ContextResponse(BaseModel):
    location_id: str
    day_type: DayType
    time_of_day: TimeOfDay
    crowd_level: CrowdLevel
    recommendation: str

    class Config:
        from_attributes = True


class ContextInfoResponse(BaseModel):
    data: ContextResponse