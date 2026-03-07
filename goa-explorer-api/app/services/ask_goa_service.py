from app.parsers.ask_goa_parser import AskGoaParser
from app.ports.llm_port import LLMPort
from app.domain.requests.ask_goa_request import AskGoaRequest
from app.domain.models.ask_goa_answer import AskGoaAnswer
from app.prompts.ask_goa_prompt_builder import AskGoaPromptBuilder


class AskGoaService:

    def __init__(
        self,
        llm: LLMPort,
        prompt_builder: AskGoaPromptBuilder,
        parser: AskGoaParser,
    ):
        self.llm = llm
        self.prompt_builder = prompt_builder
        self.parser = parser

    def ask(self, request: AskGoaRequest) -> AskGoaAnswer:
        prompt = self.prompt_builder.build_prompt(request)
        raw_response = self.llm.generate(prompt)
        return self.parser.parse(raw_response)