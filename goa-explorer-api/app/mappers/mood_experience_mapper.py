from app.api.schemas.requests.mood_experience_request_schema import MoodExperienceRequestSchema
from app.api.schemas.responses.mood_experience_response import MoodExperienceResponse
from app.domain.requests.mood_experience_request import MoodExperienceRequest
from app.domain.entities.mood_experience import MoodExperience


class MoodExperienceMapper:

    @staticmethod
    def to_domain_request(schema: MoodExperienceRequestSchema) -> MoodExperienceRequest:
        return MoodExperienceRequest(
            mood=schema.mood,
            start_location=schema.start_location,
        )

    @staticmethod
    def to_response(domain: MoodExperience) -> MoodExperienceResponse:
        return MoodExperienceResponse.model_validate(domain.model_dump())