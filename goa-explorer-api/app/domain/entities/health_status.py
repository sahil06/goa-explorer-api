from dataclasses import dataclass
from typing import Dict


@dataclass
class HealthStatus:
    service: str
    status: str
    details: Dict[str, str]
