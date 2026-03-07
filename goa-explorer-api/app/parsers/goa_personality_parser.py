import json
from app.domain.models.goa_personality import GoaPersonality


class GoaPersonalityParser:

    @staticmethod
    def parse(raw_response: str) -> GoaPersonality:

        try:
            data = json.loads(raw_response)

            return GoaPersonality(
                personality=data.get("personality", ""),
                description=data.get("description", ""),
                recommended_areas=data.get("recommended_areas", []),
            )

        except json.JSONDecodeError:

            return GoaPersonality(
                personality="Unknown",
                description="Could not determine personality",
                recommended_areas=[],
            )