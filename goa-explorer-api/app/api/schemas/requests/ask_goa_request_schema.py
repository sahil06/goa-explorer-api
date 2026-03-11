from pydantic import BaseModel


class AskGoaRequestSchema(BaseModel):
    question: str