from pydantic import BaseModel


class AskGoaResponse(BaseModel):
    answer: str