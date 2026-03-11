from app.api.schemas.requests.ask_goa_request_schema import AskGoaRequestSchema
from app.domain.requests.ask_goa_request import AskGoaRequest


class AskGoaMapper:

    @staticmethod
    def to_domain_request(schema: AskGoaRequestSchema) -> AskGoaRequest:
        return AskGoaRequest(question=schema.question)