from app.domain.entities.context_info import ContextInfo
from app.api.schemas.context_response import (
    ContextResponse,
    ContextInfoResponse,
)


class ContextMapper:

    @staticmethod
    def to_response(entity: ContextInfo) -> ContextInfoResponse:
        return ContextInfoResponse(
            data=ContextResponse.model_validate(entity)
        )