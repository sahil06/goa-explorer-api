from dataclasses import dataclass
from app.domain.enums import DayType, TimeOfDay


@dataclass
class ContextQuery:
    location_id: str
    day_type: DayType
    time_of_day: TimeOfDay