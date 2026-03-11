from pydantic import BaseModel


class BestSunsetRequestSchema(BaseModel):
    current_location: str
    travel_time_minutes: int