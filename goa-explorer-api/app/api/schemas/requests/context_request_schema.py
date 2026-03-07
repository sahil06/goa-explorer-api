from pydantic import BaseModel
from app.domain.enums.enums import DayType
from app.domain.enums.time_of_day import TimeOfDay


class ContextRequestSchema(BaseModel):
    location_id: str
    day_type: DayType
    time_of_day: TimeOfDay