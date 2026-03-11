from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Goa Explorer API"
    debug: bool = False
    api_v1_prefix: str = "/api/v1"
    service_name: str = "ai-backend"
    ollama_base_url: str = "http://localhost:11434"

    class Config:
        env_file = ".env"


settings = Settings()

