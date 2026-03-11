import json
from app.domain.models.mood_experience import MoodExperience


class MoodExperienceParser:

    @staticmethod
    def parse(raw_response: str) -> MoodExperience:
        try:
            data = json.loads(raw_response)

            return MoodExperience(
                experience=data.get("experience", ""),
                location=data.get("location", ""),
                route=data.get("route", ""),
                best_time=data.get("best_time", ""),
                notes=data.get("notes", "")
            )

        except json.JSONDecodeError:
            return MoodExperience(
                experience="Unknown experience",
                location="",
                route="",
                best_time="",
                notes="LLM response was not valid JSON"
            )