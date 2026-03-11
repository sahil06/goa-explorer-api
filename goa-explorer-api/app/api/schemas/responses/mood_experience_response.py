from pydantic import BaseModel


class MoodExperienceResponse(BaseModel):
    experience: str
    location: str
    route: str
    best_time: str
    notes: str