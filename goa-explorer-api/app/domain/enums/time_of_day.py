from enum import Enum


class TimeOfDay(str, Enum):
    morning = "morning"
    afternoon = "afternoon"
    sunset = "sunset"
    night = "night"