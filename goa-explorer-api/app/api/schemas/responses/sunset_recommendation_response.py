from pydantic import BaseModel


class SunsetRecommendationResponse(BaseModel):
    location: str
    distance_km: float
    best_arrival_time: str
    crowd_level: str
    notes: str