from abc import ABC, abstractmethod
from typing import AsyncGenerator


class LLMPort(ABC):

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Synchronous full response generation"""
        pass

    @abstractmethod
    async def generate_stream(self, prompt: str) -> AsyncGenerator[str, None]:
        """Async generator for streaming response"""
        pass