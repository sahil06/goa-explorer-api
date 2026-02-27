from app.core.config import settings
from app.domain.entities.health_status import HealthStatus
from app.ports.health_repository_port import HealthRepositoryPort
from app.core.logger import get_logger

logger = get_logger(__name__)

class HealthService:

    def __init__(self, repository: HealthRepositoryPort):
        self.repository = repository

    async def get_health(self) -> HealthStatus:
        logger.info("Checking system health")
        components = await self.repository.get_components_status()

        if not components:
            overall_status = "down"
        else:
            overall_status = (
                "down"
                if any(status != "ok" for status in components.values())
                else "ok"
            )

        return HealthStatus(
            service=settings.service_name,
            status=overall_status,
            details=components
        )
