from enum import Enum


class SurfaceType(str, Enum):
    asphalt = "asphalt"
    gravel = "gravel"
    mud = "mud"
    mixed = "mixed"