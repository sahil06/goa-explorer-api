from functools import lru_cache
from fastapi import Depends
from app.adapters.ollama_llm_adapter import OllamaLLMAdapter
from app.datasources.context_json_datasource import ContextJsonDataSource
from app.datasources.ride_route_json_datasource import RideRouteJsonDatasource
from app.parsers.ask_goa_parser import AskGoaParser
from app.parsers.mood_experience_parser import MoodExperienceParser
from app.parsers.ride_plan_parser import RidePlanParser
from app.parsers.sunset_recommendation_parser import SunsetRecommendationParser
from app.ports.context_repository_port import ContextRepositoryPort
from app.ports.llm_port import LLMPort
from app.ports.location_repository_port import LocationRepositoryPort
from app.ports.ride_route_repository_port import RideRouteRepositoryPort
from app.prompts.ask_goa_prompt_builder import AskGoaPromptBuilder
from app.prompts.best_sunset_prompt_builder import BestSunsetPromptBuilder
from app.prompts.mood_experience_prompt_builder import MoodExperiencePromptBuilder
from app.prompts.ride_planning_prompt_builder import RidePlanningPromptBuilder
from app.services.ask_goa_service import AskGoaService
from app.services.experience_service import ExperienceService
from app.services.exploration_service import ExplorationService
from app.services.health_service import HealthService
from app.adapters.in_memory_health_repository import InMemoryHealthRepository
from app.adapters.ride_route_repository_adapter import RideRouteRepositoryAdapter
from app.adapters.context_repository_adapter import ContextRepositoryAdapter
from app.adapters.location_repository_adapter import LocationRepositoryAdapter
from app.datasources.location_json_datasource import LocationJsonDatasource
from app.services.ride_planning_service import RidePlanningService


def get_health_repository():
    return InMemoryHealthRepository()

def get_health_service() -> HealthService:
    repository = get_health_repository()
    return HealthService(repository)

@lru_cache
def get_location_datasource():
    return LocationJsonDatasource(file_path="app/datasources/locations.json")

def get_location_repository(
    datasource: LocationJsonDatasource = Depends(get_location_datasource),
) -> LocationRepositoryPort:
    return LocationRepositoryAdapter(datasource)

@lru_cache
def get_ride_route_datasource():
    return RideRouteJsonDatasource(file_path="app/datasources/ride_routes.json")

def get_ride_route_repository(
    datasource: RideRouteJsonDatasource = Depends(get_ride_route_datasource),
) -> RideRouteRepositoryPort:
    return RideRouteRepositoryAdapter(datasource)

@lru_cache
def get_context_datasource():
    return ContextJsonDataSource(file_path="app/datasources/context.json")

def get_context_repository(
    datasource: ContextJsonDataSource = Depends(get_context_datasource),
) -> ContextRepositoryPort:
    return ContextRepositoryAdapter(datasource)

def get_exploration_service(
    location_repository: LocationRepositoryPort = Depends(get_location_repository),
    ride_route_repository: RideRouteRepositoryPort = Depends(get_ride_route_repository),
    context_repository: ContextRepositoryPort = Depends(get_context_repository),
):
    return ExplorationService(
        location_repo=location_repository,
        route_repo=ride_route_repository,
        context_repo=context_repository,
    )

@lru_cache()
def get_llm() -> LLMPort:
    return OllamaLLMAdapter(model="llama3")

def get_ride_planning_service(
    llm: LLMPort = Depends(get_llm),
) -> RidePlanningService:
    prompt_builder = RidePlanningPromptBuilder()
    parser = RidePlanParser()
    return RidePlanningService(llm, prompt_builder, parser)

def get_experience_service(
    llm: LLMPort = Depends(get_llm),
) -> ExperienceService:

    mood_prompt = MoodExperiencePromptBuilder()
    mood_parser = MoodExperienceParser()

    sunset_prompt = BestSunsetPromptBuilder()
    sunset_parser = SunsetRecommendationParser()

    return ExperienceService(
        llm=llm,
        mood_prompt_builder=mood_prompt,
        mood_parser=mood_parser,
        sunset_prompt_builder=sunset_prompt,
        sunset_parser=sunset_parser,
    )

def get_ask_goa_service(
    llm: LLMPort = Depends(get_llm),
) -> AskGoaService:
    return AskGoaService(
        llm,
        AskGoaPromptBuilder(),
        AskGoaParser(),
    )

