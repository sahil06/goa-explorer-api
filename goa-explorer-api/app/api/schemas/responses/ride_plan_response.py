from pydantic import BaseModel
from typing import List

class RideResponse(BaseModel):
    stops: List[str]
    total_distance: float
    estimated_time: str
    notes: str


class RidePlanResponse(BaseModel):
    data: RideResponse