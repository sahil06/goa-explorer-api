from app.api.schemas.requests.context_request_schema import ContextRequestSchema
from app.domain.entities.context_info import ContextInfo
from app.api.schemas.responses.context_response import (
    ContextResponse,
    ContextInfoResponse,
)
from app.domain.requests.context_request import ContextRequest


class ContextMapper:

    @staticmethod
    def to_domain_request(schema: ContextRequestSchema) -> ContextRequest:
        return ContextRequest(
            location_id=schema.location_id,
            day_type=schema.day_type,
            time_of_day=schema.time_of_day,
        )

    @staticmethod
    def to_response(entity: ContextInfo) -> ContextInfoResponse:
        return ContextInfoResponse(
            data=ContextResponse.model_validate(entity)
        )