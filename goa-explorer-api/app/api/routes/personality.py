from fastapi import APIRouter, Depends
from app.api.schemas.requests.goa_personality_request_schema import GoaPersonalityRequestSchema
from app.api.schemas.responses.goa_personality_response import GoaPersonalityResponse
from app.mappers.goa_personality_mapper import GoaPersonalityMapper
from app.services.personality_service import PersonalityService
from app.api.dependencies import get_personality_service


router = APIRouter(prefix="/personality", tags=["Personality"])


@router.post("/goa-personality", response_model=GoaPersonalityResponse, summary="Classify the user's personality type based on their preferences using AI.")
def goa_personality(
    request: GoaPersonalityRequestSchema,
    service: PersonalityService = Depends(get_personality_service),
):
    domain_request = GoaPersonalityMapper.to_domain_request(request)
    result = service.classify(domain_request)
    return GoaPersonalityMapper.to_response(result)