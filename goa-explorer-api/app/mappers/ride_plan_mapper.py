from app.api.schemas.requests.plan_ride_request_schema import PlanRideRequestSchema
from app.api.schemas.responses.ride_plan_response import RidePlanResponse, RideResponse
from app.domain.requests.plan_ride_request import PlanRideRequest
from app.domain.entities.ride_plan import RidePlan


class RidePlanMapper:

    @staticmethod
    def to_domain_request(schema: PlanRideRequestSchema) -> PlanRideRequest:
        return PlanRideRequest(
            start_location=schema.start_location,
            ride_duration_hours=schema.ride_duration_hours,
            time_of_day=schema.time_of_day,
        )

    @staticmethod
    def to_response(domain: RidePlan) -> RidePlanResponse:
        ride_response = RideResponse.model_validate(domain.model_dump())
        return RidePlanResponse(data=ride_response)