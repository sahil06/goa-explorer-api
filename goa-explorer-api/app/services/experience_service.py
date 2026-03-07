from app.parsers.mood_experience_parser import MoodExperienceParser
from app.ports.llm_port import LLMPort
from app.domain.requests.mood_experience_request import MoodExperienceRequest
from app.domain.models.mood_experience import MoodExperience
from app.prompts.mood_experience_prompt_builder import MoodExperiencePromptBuilder


class ExperienceService:

    def __init__(
        self,
        llm: LLMPort,
        prompt_builder: MoodExperiencePromptBuilder,
        parser: MoodExperienceParser,
    ):
        self.llm = llm
        self.prompt_builder = prompt_builder
        self.parser = parser

    def experience_from_mood(self, request: MoodExperienceRequest) -> MoodExperience:
        prompt = self.prompt_builder.build_prompt(request)
        raw_response = self.llm.generate(prompt)
        return self.parser.parse(raw_response)