from app.core.exceptions import NotFoundException
from app.domain.entities.context_info import ContextInfo
from app.ports.context_repository_port import ContextRepositoryPort
from app.queries.context_query import ContextQuery
from app.datasources.context_json_datasource import ContextJsonDataSource
from app.domain.enums import (
    TimeOfDay,
    DayType,        
)


class ContextRepositoryAdapter(ContextRepositoryPort):

    def __init__(self, datasource: ContextJsonDataSource):
        self.datasource = datasource

    def get_context(self, query: ContextQuery) -> ContextInfo:
        raw_data = self.datasource.fetch_all()

        for item in raw_data:
            if (
                item["location_id"] == query.location_id
                and item["day_type"] == query.day_type.value
                and item["time_of_day"] == query.time_of_day.value
            ):
                return ContextInfo(
                    location_id=item["location_id"],
                    day_type=DayType(item["day_type"]),
                    time_of_day=TimeOfDay(item["time_of_day"]),
                    crowd_level=item["crowd_level"],
                    recommendation=item["recommendation"],
                )

        raise NotFoundException("Context not found")