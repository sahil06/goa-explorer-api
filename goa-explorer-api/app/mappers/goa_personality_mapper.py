from app.api.schemas.requests.goa_personality_request_schema import GoaPersonalityRequestSchema
from app.api.schemas.responses.goa_personality_response import GoaPersonalityResponse
from app.domain.requests.goa_personality_request import GoaPersonalityRequest
from app.domain.models.goa_personality import GoaPersonality


class GoaPersonalityMapper:

    @staticmethod
    def to_domain_request(schema: GoaPersonalityRequestSchema) -> GoaPersonalityRequest:
        return GoaPersonalityRequest(preferences=schema.preferences)

    @staticmethod
    def to_response(domain: GoaPersonality) -> GoaPersonalityResponse:
        return GoaPersonalityResponse.model_validate(domain.model_dump())