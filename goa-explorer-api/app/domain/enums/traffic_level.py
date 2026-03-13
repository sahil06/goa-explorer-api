from enum import Enum



class TrafficLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"