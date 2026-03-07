import asyncio
from app.ports.llm_port import LLMPort
from langchain_ollama import OllamaLLM
from typing import AsyncGenerator


class OllamaLLMAdapter(LLMPort):

    def __init__(self, model: str = "llama3"):
        self.llm_json = OllamaLLM(
            model=model,
            format="json"
        )
        self.llm_stream = OllamaLLM(
            model=model,
            streaming=True
        )

    def generate(self, prompt: str) -> str:
        response = self.llm_json.invoke(prompt)
        return response
    
    async def generate_stream(self, prompt: str) -> AsyncGenerator[str, None]:
        for chunk in self.llm_stream.stream(prompt):
            if chunk:
                yield chunk
                await asyncio.sleep(0)  # flush event loop