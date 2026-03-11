from app.domain.requests.best_sunset_request import BestSunsetRequest


class BestSunsetPromptBuilder:

    @staticmethod
    def build_prompt(request: BestSunsetRequest) -> str:
        return f"""
You are a Goa travel assistant.

Recommend the best sunset location.

User current location: {request.current_location}
Available travel time (minutes): {request.travel_time_minutes}

Return STRICT JSON with fields:
location
distance_km
best_arrival_time
crowd_level
notes

Return ONLY valid JSON.
"""