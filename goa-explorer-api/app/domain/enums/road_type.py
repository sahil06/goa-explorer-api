from enum import Enum


class RoadType(str, Enum):
    highway = "highway"
    coastal = "coastal"
    village = "village"
    ghat = "ghat"
    city = "city"