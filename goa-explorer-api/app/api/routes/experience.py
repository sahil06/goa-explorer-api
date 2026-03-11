from fastapi import APIRouter, Depends
from app.api.dependencies import get_experience_service
from app.api.schemas.requests.best_sunset_request_schema import BestSunsetRequestSchema
from app.api.schemas.requests.mood_experience_request_schema import MoodExperienceRequestSchema
from app.api.schemas.responses.mood_experience_response import MoodExperienceResponse
from app.api.schemas.responses.sunset_recommendation_response import SunsetRecommendationResponse
from app.mappers.mood_experience_mapper import MoodExperienceMapper
from app.mappers.sunset_recommendation_mapper import SunsetRecommendationMapper
from app.services.experience_service import ExperienceService


router = APIRouter(prefix="/experience", tags=["Experience"])


@router.post("/experience-from-mood", response_model=MoodExperienceResponse, summary="Get a personalized experience recommendation based on the user's current mood and preferences with AI.")
def experience_from_mood(
    request: MoodExperienceRequestSchema,
    service: ExperienceService = Depends(get_experience_service),
):
    domain_request = MoodExperienceMapper.to_domain_request(request)
    result = service.experience_from_mood(domain_request)
    return MoodExperienceMapper.to_response(result)


@router.post("/best-sunset", response_model=SunsetRecommendationResponse, summary="Get the best sunset viewing locations and times in Goa based on user preferences and AI analysis.")
def best_sunset(
    request: BestSunsetRequestSchema,
    service: ExperienceService = Depends(get_experience_service),
):
    domain_request = SunsetRecommendationMapper.to_domain_request(request)
    result = service.best_sunset(domain_request)
    return SunsetRecommendationMapper.to_response(result)