from pydantic import BaseModel


class AskGoaRequest(BaseModel):
    question: str