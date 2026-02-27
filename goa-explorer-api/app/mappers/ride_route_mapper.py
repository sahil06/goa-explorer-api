from app.domain.entities.ride_route import RideRoute
from app.api.schemas.ride_route_response import RideRouteListResponse, RideRouteResponse


class RideRouteMapper:

    @staticmethod
    def to_response(entity: RideRoute) -> RideRouteResponse:
        return RideRouteResponse.model_validate(entity)

    @staticmethod
    def to_list_response(entities: list[RideRoute]) -> RideRouteListResponse:
        return RideRouteListResponse(
            total=len(entities),
            items=[
                RideRouteResponse.model_validate(e)
                for e in entities
            ]
        )