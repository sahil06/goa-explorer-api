from functools import lru_cache
from fastapi import Depends
from app.services.health_service import HealthService
from app.adapters.in_memory_health_repository import InMemoryHealthRepository


def get_health_repository():
    return InMemoryHealthRepository()

def get_health_service() -> HealthService:
    repository = get_health_repository()
    return HealthService(repository)