from app.api.schemas.requests.ask_goa_request_schema import AskGoaRequestSchema
from app.api.schemas.responses.ask_goa_response import AskGoaResponse
from app.domain.requests.ask_goa_request import AskGoaRequest
from app.domain.models.ask_goa_answer import AskGoaAnswer


class AskGoaMapper:

    @staticmethod
    def to_domain_request(schema: AskGoaRequestSchema) -> AskGoaRequest:
        return AskGoaRequest(question=schema.question)

    @staticmethod
    def to_response(domain: AskGoaAnswer) -> AskGoaResponse:
        return AskGoaResponse.model_validate(domain.model_dump())