from app.domain.entities.ride_plan import RidePlan
from app.domain.requests.plan_ride_request import PlanRideRequest
from app.parsers.ride_plan_parser import RidePlanParser
from app.ports.llm_port import LLMPort
from app.prompts.ride_planning_prompt_builder import RidePlanningPromptBuilder


class RidePlanningService:

    def __init__(
        self,
        llm: LLMPort,
        prompt_builder: RidePlanningPromptBuilder,
        parser: RidePlanParser
    ):
        self.llm = llm
        self.prompt_builder = prompt_builder
        self.parser = parser

    def plan_ride(self, request: PlanRideRequest) -> RidePlan:
        prompt = self.prompt_builder.build_plan_prompt(request)
        raw_response = self.llm.generate(prompt)
        return self.parser.parse(raw_response)