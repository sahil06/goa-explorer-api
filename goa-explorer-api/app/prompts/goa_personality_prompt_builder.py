from app.domain.requests.goa_personality_request import GoaPersonalityRequest


class GoaPersonalityPromptBuilder:

    @staticmethod
    def build_prompt(request: GoaPersonalityRequest) -> str:
        prefs = ", ".join(request.preferences)

        return f"""
You are a Goa travel expert.

Classify the user into a Goa traveler personality.

Preferences:
{prefs}

Possible personalities:
Party Explorer
Sunset Chaser
Hidden Beach Hunter
Luxury Escapist
Nature Seeker
Cafe Hopper

Return STRICT JSON:

personality
description
recommended_areas (array of Goa locations)
"""