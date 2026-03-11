from pydantic import BaseModel


class MoodExperienceRequestSchema(BaseModel):
    mood: str
    start_location: str