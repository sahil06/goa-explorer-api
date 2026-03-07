from abc import ABC, abstractmethod
from app.domain.models.context_info import ContextInfo
from app.domain.requests.context_request import ContextRequest


class ContextRepositoryPort(ABC):

    @abstractmethod
    def get_context(self, query: ContextRequest) -> ContextInfo:
        pass