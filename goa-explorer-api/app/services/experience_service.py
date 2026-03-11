from app.domain.models.sunset_recommendation import SunsetRecommendation
from app.domain.requests.best_sunset_request import BestSunsetRequest
from app.parsers.mood_experience_parser import MoodExperienceParser
from app.parsers.sunset_recommendation_parser import SunsetRecommendationParser
from app.ports.llm_port import LLMPort
from app.domain.requests.mood_experience_request import MoodExperienceRequest
from app.domain.models.mood_experience import MoodExperience
from app.prompts.best_sunset_prompt_builder import BestSunsetPromptBuilder
from app.prompts.mood_experience_prompt_builder import MoodExperiencePromptBuilder


class ExperienceService:

    def __init__(
        self,
        llm: LLMPort,
        mood_prompt_builder: MoodExperiencePromptBuilder,
        mood_parser: MoodExperienceParser,
        sunset_prompt_builder: BestSunsetPromptBuilder,
        sunset_parser: SunsetRecommendationParser,
    ):
        self.llm = llm
        self.mood_prompt_builder = mood_prompt_builder
        self.mood_parser = mood_parser
        self.sunset_prompt_builder = sunset_prompt_builder
        self.sunset_parser = sunset_parser

    def experience_from_mood(self, request: MoodExperienceRequest) -> MoodExperience:
        prompt = self.mood_prompt_builder.build_prompt(request)
        raw_response = self.llm.generate(prompt)
        return self.mood_parser.parse(raw_response)

    def best_sunset(self, request: BestSunsetRequest) -> SunsetRecommendation:
        prompt = self.sunset_prompt_builder.build_prompt(request)
        raw_response = self.llm.generate(prompt)
        return self.sunset_parser.parse(raw_response)