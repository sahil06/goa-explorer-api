from pydantic import BaseModel
from typing import List


class GoaPersonalityResponse(BaseModel):
    personality: str
    description: str
    recommended_areas: List[str]