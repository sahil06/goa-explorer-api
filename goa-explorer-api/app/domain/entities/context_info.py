from pydantic import BaseModel
from app.domain.enums.day_type import DayType
from app.domain.enums.time_of_day import TimeOfDay

class ContextInfo(BaseModel):
    location_id: str
    day_type: DayType
    time_of_day: TimeOfDay
    crowd_level: str
    recommendation: str