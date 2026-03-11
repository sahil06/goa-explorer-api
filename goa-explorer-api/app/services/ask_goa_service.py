from typing import AsyncGenerator
from app.ports.llm_port import LLMPort
from app.domain.requests.ask_goa_request import AskGoaRequest
from app.prompts.ask_goa_prompt_builder import AskGoaPromptBuilder


class AskGoaService:

    def __init__(
        self,
        llm: LLMPort,
        prompt_builder: AskGoaPromptBuilder,
    ):
        self.llm = llm
        self.prompt_builder = prompt_builder

    async def stream_answer(self, request: AskGoaRequest) -> AsyncGenerator[str, None]:
        prompt = self.prompt_builder.build_prompt(request)

        async for chunk in self.llm.generate_stream(prompt):
            yield chunk