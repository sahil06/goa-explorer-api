from typing import Optional

from pydantic import BaseModel
from app.domain.enums.location_type import LocationType
from app.domain.enums.region import Region
from app.domain.enums.vibe import Vibe


class LocationRequestSchema(BaseModel):
    region: Optional[Region] = None,
    type: Optional[LocationType] = None,
    vibe: Optional[Vibe] = None,