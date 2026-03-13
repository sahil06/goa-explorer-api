from typing import List
from app.domain.enums.crowd_level import CrowdLevel
from app.domain.enums.location_type import LocationType
from app.domain.enums.region import Region
from app.domain.enums.time_of_day import TimeOfDay
from app.domain.enums.vibe import Vibe
from app.ports.location_repository_port import LocationRepositoryPort
from app.domain.entities.location import Location
from app.domain.requests.location_filter import LocationFilter
from app.datasources.location_json_datasource import LocationJsonDatasource


class LocationRepositoryAdapter(LocationRepositoryPort):

    def __init__(self, datasource: LocationJsonDatasource):
        self.datasource = datasource

    def _to_domain(self, raw: dict) -> Location:
        return Location(
            id=raw["id"],
            name=raw["name"],
            region=Region(raw["region"]),
            type=LocationType(raw["type"]),
            vibe=[Vibe(v) for v in raw["vibe"]],
            best_time_of_day=[TimeOfDay(t) for t in raw["best_time_of_day"]],
            crowd_level_weekday=CrowdLevel(raw["crowd_level_weekday"]),
            crowd_level_weekend=CrowdLevel(raw["crowd_level_weekend"]),
            short_description=raw["short_description"],
        )

    def list_filtered(self, filters: LocationFilter) -> List[Location]:
        raw_data = self.datasource.load()
        locations = [self._to_domain(item) for item in raw_data]

        if filters.region:
            locations = [l for l in locations if l.region == filters.region]

        if filters.type:
            locations = [l for l in locations if l.type == filters.type]

        if filters.vibe:
            locations = [l for l in locations if filters.vibe in l.vibe]

        return locations