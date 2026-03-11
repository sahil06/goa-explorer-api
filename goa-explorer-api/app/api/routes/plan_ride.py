from fastapi import APIRouter, Depends
from app.api.dependencies import get_ride_planning_service
from app.api.schemas.requests.plan_ride_request_schema import PlanRideRequestSchema
from app.api.schemas.responses.ride_plan_response import RidePlanResponse
from app.mappers.ride_plan_mapper import RidePlanMapper
from app.services.ride_planning_service import RidePlanningService

router = APIRouter(prefix="/plan", tags=["Plan"])


@router.post("/plan-ride", response_model=RidePlanResponse, summary="Plan a ride based on user preferences and AI-generated suggestions.")
def plan_ride(
    request: PlanRideRequestSchema,
    service: RidePlanningService = Depends(get_ride_planning_service),
):
    domain_request = RidePlanMapper.to_domain_request(request)
    ride_plan = service.plan_ride(domain_request)
    return RidePlanMapper.to_response(ride_plan)