from app.domain.requests.ask_goa_request import AskGoaRequest


class AskGoaPromptBuilder:

    @staticmethod
    def build_prompt(request: AskGoaRequest) -> str:
        return f"""
You are a helpful Goa travel assistant.

Answer the user's question about Goa travel, beaches, food, nightlife, nature, or activities.

Question:
{request.question}

Return STRICT JSON with this field:
answer
"""