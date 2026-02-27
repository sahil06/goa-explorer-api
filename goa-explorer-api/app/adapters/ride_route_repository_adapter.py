from typing import List
from app.domain.entities.ride_route import RideRoute
from app.ports.ride_route_repository_port import RideRouteRepositoryPort
from app.adapters.filters.ride_route_filter import RideRouteFilter
from app.domain.enums import (
    RouteDifficulty,
    RoadType,
    SurfaceType,
    TrafficLevel,
)
from app.datasources.ride_route_json_datasource import RideRouteJsonDatasource


class RideRouteRepositoryAdapter(RideRouteRepositoryPort):

    def __init__(self, datasource: RideRouteJsonDatasource):
        self.datasource = datasource

    def list_filtered(self, filters: RideRouteFilter) -> List[RideRoute]:
        raw_data = self.datasource.load()

        results: List[RideRoute] = []

        for item in raw_data:

            if filters.difficulty and item["difficulty"] != filters.difficulty.value:
                continue

            if filters.road_type and item["road_type"] != filters.road_type.value:
                continue

            if filters.surface and item["surface"] != filters.surface.value:
                continue

            if filters.traffic and item["traffic_level"] != filters.traffic.value:
                continue

            if filters.min_distance_km and item["distance_km"] < filters.min_distance_km:
                continue

            if filters.max_distance_km and item["distance_km"] > filters.max_distance_km:
                continue

            route = RideRoute(
                id=item["id"],
                name=item["name"],
                start_location=item["start_location"],
                end_location=item["end_location"],
                distance_km=item["distance_km"],
                difficulty=RouteDifficulty(item["difficulty"]),
                road_type=RoadType(item["road_type"]),
                surface=SurfaceType(item["surface"]),
                traffic_level=TrafficLevel(item["traffic_level"]),
                highlights=item["highlights"],
            )

            results.append(route)

        return results