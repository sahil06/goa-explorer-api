import json
from app.domain.models.ask_goa_answer import AskGoaAnswer


class AskGoaParser:

    @staticmethod
    def parse(raw_response: str) -> AskGoaAnswer:
        try:
            data = json.loads(raw_response)
            return AskGoaAnswer(answer=data.get("answer", ""))
        except json.JSONDecodeError:
            return AskGoaAnswer(answer=raw_response)