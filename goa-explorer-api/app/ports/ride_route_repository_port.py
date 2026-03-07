from abc import ABC, abstractmethod
from typing import List
from app.domain.models.ride_route import RideRoute
from app.domain.requests.ride_route_filter import RideRouteFilter


class RideRouteRepositoryPort(ABC):

    @abstractmethod
    def list_filtered(self, filters: RideRouteFilter) -> List[RideRoute]:
        pass