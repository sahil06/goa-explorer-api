from pydantic import BaseModel


class BestSunsetRequest(BaseModel):
    current_location: str
    travel_time_minutes: int