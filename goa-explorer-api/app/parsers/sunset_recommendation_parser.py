import json
from app.domain.entities.sunset_recommendation import SunsetRecommendation


class SunsetRecommendationParser:

    @staticmethod
    def parse(raw_response: str) -> SunsetRecommendation:
        try:
            data = json.loads(raw_response)

            return SunsetRecommendation(
                location=data.get("location", ""),
                distance_km=data.get("distance_km", 0),
                best_arrival_time=data.get("best_arrival_time", ""),
                crowd_level=data.get("crowd_level", ""),
                notes=data.get("notes", ""),
            )

        except json.JSONDecodeError:
            return SunsetRecommendation(
                location="",
                distance_km=0,
                best_arrival_time="",
                crowd_level="unknown",
                notes="LLM response was not valid JSON",
            )