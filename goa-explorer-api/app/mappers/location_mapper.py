from app.api.schemas.requests.location_request_schema import LocationRequestSchema
from app.domain.entities.location import Location
from app.api.schemas.responses.location_response import (
    LocationResponse,
    LocationListResponse,
)
from app.domain.requests.location_filter import LocationFilter


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