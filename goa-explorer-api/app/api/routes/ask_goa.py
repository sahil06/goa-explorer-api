from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from app.api.dependencies import get_ask_goa_service
from app.api.schemas.requests.ask_goa_request_schema import AskGoaRequestSchema
from app.mappers.ask_goa_mapper import AskGoaMapper
from app.services.ask_goa_service import AskGoaService


router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/ask-goa/stream", summary="Ask any question about Goa and get an AI-powered answer based on the latest information and insights.")
async def ask_goa(
    request: AskGoaRequestSchema,
    service: AskGoaService = Depends(get_ask_goa_service),
):

    domain_request = AskGoaMapper.to_domain_request(request)

    async def generator():
        async for chunk in service.stream_answer(domain_request):
            yield chunk

    return StreamingResponse(generator(), media_type="text/plain")


