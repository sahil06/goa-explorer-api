from pydantic import BaseModel
from app.domain.enums import DayType, TimeOfDay, CrowdLevel


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