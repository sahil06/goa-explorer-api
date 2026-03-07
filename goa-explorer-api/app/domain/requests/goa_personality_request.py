from pydantic import BaseModel
from typing import List


class GoaPersonalityRequest(BaseModel):
    preferences: List[str]