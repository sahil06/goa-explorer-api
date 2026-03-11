import json
import re
from app.domain.models.ride_plan import RidePlan


class RidePlanParser:

    @staticmethod
    def parse(raw_response: str) -> RidePlan:
        try:
            # Try to parse as direct JSON
            data = json.loads(raw_response)
        except json.JSONDecodeError:
            # Try to extract JSON from the response
            json_match = re.search(r'\{.*\}', raw_response, re.DOTALL)
            if json_match:
                try:
                    data = json.loads(json_match.group())
                except json.JSONDecodeError:
                    data = {}
            else:
                data = {}

        # Ensure required fields with defaults
        return RidePlan(
            stops=data.get("stops", []),
            total_distance=data.get("total_distance", 0),
            estimated_time=data.get("estimated_time", ""),
            notes=data.get("notes", "")
        )