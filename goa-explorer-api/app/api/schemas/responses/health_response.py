from pydantic import BaseModel
from typing import Dict


class HealthResponse(BaseModel):
    service: str
    status: str
    details: Dict[str, str]
