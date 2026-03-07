
from app.ports.location_repository_port import LocationRepositoryPort
from app.ports.ride_route_repository_port import RideRouteRepositoryPort
from app.ports.context_repository_port import ContextRepositoryPort
from app.domain.requests.location_filter import LocationFilter


class ExplorationService:

    def __init__(
        self,
        location_repo: LocationRepositoryPort,
        route_repo: RideRouteRepositoryPort,
        context_repo: ContextRepositoryPort,
    ):
        self.location_repo = location_repo
        self.route_repo = route_repo
        self.context_repo = context_repo

    def list_locations(self, filters: LocationFilter):
        return self.location_repo.list_filtered(filters)

    def list_ride_routes(self, filters):
        return self.route_repo.list_filtered(filters)

    def get_context_info(self, query):
        return self.context_repo.get_context(query)