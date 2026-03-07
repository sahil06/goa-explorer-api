from pydantic import BaseModel


class MoodExperienceRequest(BaseModel):
    mood: str
    start_location: str