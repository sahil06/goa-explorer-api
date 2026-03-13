from enum import Enum


class CrowdLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"