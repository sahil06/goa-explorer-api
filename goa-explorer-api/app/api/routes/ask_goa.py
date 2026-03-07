from fastapi import APIRouter, Depends
from app.api.dependencies import get_ask_goa_service
from app.api.schemas.requests.ask_goa_request_schema import AskGoaRequestSchema
from app.api.schemas.responses.ask_goa_response import AskGoaResponse
from app.mappers.ask_goa_mapper import AskGoaMapper
from app.services.ask_goa_service import AskGoaService


router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/ask-goa", response_model=AskGoaResponse, summary="Ask any question about Goa and get an AI-powered answer based on the latest information and insights.")
def ask_goa(
    request: AskGoaRequestSchema,
    service: AskGoaService = Depends(get_ask_goa_service),
):
    domain_request = AskGoaMapper.to_domain_request(request)
    result = service.ask(domain_request)
    return AskGoaMapper.to_response(result)