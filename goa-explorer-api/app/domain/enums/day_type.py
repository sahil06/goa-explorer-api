from enum import Enum


class DayType(str, Enum):
    weekday = "weekday"
    weekend = "weekend"
    holiday = "holiday"