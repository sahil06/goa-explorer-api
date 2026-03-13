from typing import Dict
from pydantic import BaseModel


class HealthStatus(BaseModel):
    service: str
    status: str
    details: Dict[str, str]
