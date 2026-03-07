from pydantic import BaseModel
from app.domain.enums.time_of_day import TimeOfDay


class PlanRideRequestSchema(BaseModel):
    start_location: str
    ride_duration_hours: int
    time_of_day: TimeOfDay