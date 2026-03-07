from pydantic import BaseModel


class AskGoaAnswer(BaseModel):
    answer: str