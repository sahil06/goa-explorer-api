from app.domain.entities.location import Location
from app.api.schemas.location_response import (
    LocationResponse,
    LocationListResponse,
)


class LocationMapper:

    @staticmethod
    def to_response(entity: Location) -> LocationResponse:
        return LocationResponse.model_validate(entity)

    @staticmethod
    def to_list_response(entities: list[Location]) -> LocationListResponse:
        return LocationListResponse(
            total=len(entities),
            items=[
                LocationResponse.model_validate(e)
                for e in entities
            ]
        )