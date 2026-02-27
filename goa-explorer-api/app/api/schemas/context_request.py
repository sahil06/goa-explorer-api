from pydantic import BaseModel
from app.domain.enums import DayType, TimeOfDay


class ContextRequest(BaseModel):
    location_id: str
    day_type: DayType
    time_of_day: TimeOfDay