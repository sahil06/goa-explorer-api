from pydantic import BaseModel
from app.domain.enums.day_type import DayType
from app.domain.enums.time_of_day import TimeOfDay


class ContextRequest(BaseModel):
    location_id: str
    day_type: DayType
    time_of_day: TimeOfDay