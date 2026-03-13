from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.location import Location
from app.domain.requests.location_filter import LocationFilter


class LocationRepositoryPort(ABC):

    @abstractmethod
    def list_filtered(self, filters: LocationFilter) -> List[Location]:
        pass