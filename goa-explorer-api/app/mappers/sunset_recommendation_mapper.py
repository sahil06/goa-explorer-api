from app.api.schemas.requests.best_sunset_request_schema import BestSunsetRequestSchema
from app.api.schemas.responses.sunset_recommendation_response import SunsetRecommendationResponse
from app.domain.requests.best_sunset_request import BestSunsetRequest
from app.domain.models.sunset_recommendation import SunsetRecommendation


class SunsetRecommendationMapper:

    @staticmethod
    def to_domain_request(schema: BestSunsetRequestSchema) -> BestSunsetRequest:
        return BestSunsetRequest(
            current_location=schema.current_location,
            travel_time_minutes=schema.travel_time_minutes,
        )

    @staticmethod
    def to_response(domain: SunsetRecommendation) -> SunsetRecommendationResponse:
        return SunsetRecommendationResponse.model_validate(domain.model_dump())