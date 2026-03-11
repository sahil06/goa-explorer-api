from pydantic import BaseModel
from typing import Optional
from app.domain.enums.enums import Region, LocationType, Vibe


class LocationFilter(BaseModel):
    region: Optional[Region] = None
    type: Optional[LocationType] = None
    vibe: Optional[Vibe] = None