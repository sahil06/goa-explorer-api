from typing import Dict
from app.ports.health_repository_port import HealthRepositoryPort


class InMemoryHealthRepository(HealthRepositoryPort):

    async def get_components_status(self) -> Dict[str, str]:
        # Simulating infrastructure checks
        return {
            "database": "ok",
            "redis": "ok"
        }
