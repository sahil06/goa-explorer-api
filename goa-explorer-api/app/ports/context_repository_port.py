from abc import ABC, abstractmethod
from app.domain.entities.context_info import ContextInfo
from app.queries.context_query import ContextQuery


class ContextRepositoryPort(ABC):

    @abstractmethod
    def get_context(self, query: ContextQuery) -> ContextInfo:
        pass