from pydantic import BaseModel, Field
from typing import List
from app.domain.enums import Vibe


class LocationResponse(BaseModel):
    id: str = Field(example="loc1")
    name: str = Field(example="Baga Beach")
    is_beach: bool = Field(example=True)
    vibe: Vibe = Field(example="party")
    has_parking: bool = Field(example=True)
    district: str = Field(example="North Goa")

    class Config:
        from_attributes = True


class LocationListResponse(BaseModel):
    total: int
    items: List[LocationResponse]