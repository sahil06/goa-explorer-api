from pydantic import BaseModel
from typing import List


class GoaPersonalityRequestSchema(BaseModel):
    preferences: List[str]