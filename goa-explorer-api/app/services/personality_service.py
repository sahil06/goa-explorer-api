from app.parsers.goa_personality_parser import GoaPersonalityParser
from app.ports.llm_port import LLMPort
from app.domain.requests.goa_personality_request import GoaPersonalityRequest
from app.domain.models.goa_personality import GoaPersonality
from app.prompts.goa_personality_prompt_builder import GoaPersonalityPromptBuilder


class PersonalityService:

    def __init__(
        self,
        llm: LLMPort,
        prompt_builder: GoaPersonalityPromptBuilder,
        parser: GoaPersonalityParser,
    ):
        self.llm = llm
        self.prompt_builder = prompt_builder
        self.parser = parser

    def classify(self, request: GoaPersonalityRequest) -> GoaPersonality:
        prompt = self.prompt_builder.build_prompt(request)
        raw_response = self.llm.generate(prompt)
        return self.parser.parse(raw_response)