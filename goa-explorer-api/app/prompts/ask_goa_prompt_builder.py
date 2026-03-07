from app.domain.requests.ask_goa_request import AskGoaRequest


class AskGoaPromptBuilder:

    @staticmethod
    def build_prompt(request: AskGoaRequest) -> str:
        return f"""
User question: {request.question}

Answer naturally.
"""