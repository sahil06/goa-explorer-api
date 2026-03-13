from typing import List
from pydantic import BaseModel


class RidePlan(BaseModel):
    stops: List[str]
    total_distance: float
    estimated_time: str
    notes: str