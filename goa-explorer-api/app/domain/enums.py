from enum import Enum


class Region(str, Enum):
    north = "north"
    south = "south"


class LocationType(str, Enum):
    beach = "beach"
    fort = "fort"
    scenic = "scenic"
    village = "village"


class Vibe(str, Enum):
    party = "party"
    quiet = "quiet"
    romantic = "romantic"
    mixed = "mixed"


class TimeOfDay(str, Enum):
    morning = "morning"
    afternoon = "afternoon"
    sunset = "sunset"
    night = "night"


class CrowdLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

    from enum import Enum


class RouteDifficulty(str, Enum):
    easy = "easy"
    moderate = "moderate"
    hard = "hard"
    extreme = "extreme"


class RoadType(str, Enum):
    highway = "highway"
    coastal = "coastal"
    village = "village"
    ghat = "ghat"
    city = "city"


class SurfaceType(str, Enum):
    asphalt = "asphalt"
    gravel = "gravel"
    mud = "mud"
    mixed = "mixed"


class TrafficLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class DayType(str, Enum):
    weekday = "weekday"
    weekend = "weekend"
    holiday = "holiday"