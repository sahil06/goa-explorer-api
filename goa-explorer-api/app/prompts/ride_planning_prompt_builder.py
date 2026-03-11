from app.domain.requests.plan_ride_request import PlanRideRequest


class RidePlanningPromptBuilder:

    @staticmethod
    def build_plan_prompt(request: PlanRideRequest) -> str:
        return f"""
You are a Goa ride planning assistant.

Create a ride plan in STRICT JSON format with the following fields:
- stops: list of location names
- total_distance: number (in km)
- estimated_time: string
- notes: short description

User request:
Start location: {request.start_location}
Ride duration (hours): {request.ride_duration_hours}
Time of day: {request.time_of_day}

Return ONLY valid JSON.
"""