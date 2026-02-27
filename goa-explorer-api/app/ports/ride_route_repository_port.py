from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.ride_route import RideRoute
from app.adapters.filters.ride_route_filter import RideRouteFilter


class RideRouteRepositoryPort(ABC):

    @abstractmethod
    def list_filtered(self, filters: RideRouteFilter) -> List[RideRoute]:
        pass