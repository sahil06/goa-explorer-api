from app.domain.requests.mood_experience_request import MoodExperienceRequest


class MoodExperiencePromptBuilder:

    @staticmethod
    def build_prompt(request: MoodExperienceRequest) -> str:
        return f"""
You are a Goa travel assistant.

A user wants a ride experience based on their mood.

User mood: {request.mood}
Starting location: {request.start_location}

Recommend a suitable ride experience in Goa.

Return the response in STRICT JSON format with the following fields:
- experience
- location
- route
- best_time
- notes

Return ONLY valid JSON.
"""