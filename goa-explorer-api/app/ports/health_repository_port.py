from abc import ABC, abstractmethod
from typing import Dict


class HealthRepositoryPort(ABC):

    @abstractmethod
    async def get_components_status(self) -> Dict[str, str]:
        pass
