# Goa Explorer API (FastAPI + Ollama)

## 1. Project Title

**Goa Explorer API** — AI-powered travel and ride experiences for Goa (FastAPI + local LLM via Ollama).

## 2. Project Overview

Goa Explorer API is a Python FastAPI backend that combines **curated Goa exploration data** (locations, ride routes, contextual hints) with a **local LLM** (via **Ollama**) to generate personalized ride plans and travel experiences.

It solves the problem of “generic travel suggestions” by turning a user’s inputs (mood, start location, time constraints, ride duration, preferences) into **structured, developer-friendly JSON** responses that can be used by web/mobile clients.

## 3. Key Features

- **Explore Goa datasets**: filterable locations and ride routes from local JSON data sources.
- **Context lookup**: fetch contextual information for a location (day type / time of day).
- **AI ride planning**: generate a structured ride plan (stops, distance, timing, notes).
- **AI experiences**: generate mood-based experiences and best-sunset recommendations.
- **Streaming AI chat**: stream an answer to “Ask Goa” questions (plain text chunks).
- **Swagger/OpenAPI docs**: interactive API docs via FastAPI.

## 4. Tech Stack

- **Python**
- **FastAPI**
- **Ollama** (local LLM runtime)
- **LangChain** (`langchain`, `langchain-community`, `langchain-ollama`)
- **REST API**
- **OpenAPI / Swagger** (FastAPI `/docs`)

## 5. Architecture

This codebase follows a clean, layered architecture where the API layer is thin and delegates to services. AI requests follow a consistent pipeline: **Request → Prompt Builder → LLM Client (Ollama) → Parser → Response**.

- **API / Routes**: FastAPI routers under `app/api/routes/` define endpoints and bind request/response schemas.
- **Services**: business orchestration under `app/services/` (exploration, ride planning, experiences, personality, chat).
- **Prompt Builder**: prompt templates under `app/prompts/` produce strict JSON instructions for the LLM (except streaming chat).
- **LLM Client**: `app/adapters/ollama_llm_adapter.py` wraps LangChain’s `OllamaLLM` for JSON responses and streaming.
- **Model Integration**:
  - **Domain models** in `app/domain/models/`
  - **Ports (interfaces)** in `app/ports/`
  - **Adapters** in `app/adapters/` (repositories + LLM adapter)
  - **Parsers** in `app/parsers/` convert raw LLM output to typed domain models

Architecture diagram (high-level):

```text
Client (Web/Mobile)
        |
        v
 FastAPI Routes (app/api/routes)
        |
        v
   Services (app/services)
     |         \
     |          \  (AI flows)
     |           v
 (Data flows)  Prompt Builders (app/prompts)
     |           |
     v           v
Adapters/Repos   LLM Port (app/ports/llm_port.py)
     |           |
     v           v
JSON Datasources Ollama Adapter (langchain_ollama.OllamaLLM)
     |           |
     v           v
 Domain Models  Parsers (app/parsers) -> Domain Models
        \______________________/ 
                 |
                 v
        API Response Schemas
```

## 6. Project Structure

Repository layout (key paths):

```text
.
├── README.md
└── goa-explorer-api/
    ├── main.py
    ├── requirements.txt
    └── app/
        ├── api/
        │   ├── routes/
        │   ├── schemas/
        │   ├── middleware/
        │   └── exception_handlers.py
        ├── services/
        ├── prompts/
        ├── parsers/
        ├── adapters/
        ├── ports/
        ├── datasources/
        ├── domain/
        ├── mappers/
        └── core/
```

What each folder does:

- **`goa-explorer-api/main.py`**: FastAPI app entrypoint; registers routers under `/api/v1`.
- **`app/api/routes/`**: HTTP endpoints grouped by feature (`Explore`, `Plan`, `Experience`, `Chat`, `Personality`, `Health`).
- **`app/api/schemas/`**: Pydantic request/response schemas used by the API layer.
- **`app/services/`**: orchestration and business logic; calls repositories and/or the LLM.
- **`app/prompts/`**: prompt builders that enforce “STRICT JSON” outputs for parseable AI responses.
- **`app/parsers/`**: resilient parsing from raw LLM text/JSON into typed domain models.
- **`app/adapters/`**: implementation of ports (e.g., JSON repositories, in-memory health repo, Ollama LLM adapter).
- **`app/ports/`**: “interfaces” the services depend on (LLM port, repository ports).
- **`app/datasources/`**: local JSON data files and datasource helpers (`locations.json`, `ride_routes.json`, `context.json`).
- **`app/domain/`**: domain models, enums, and request objects independent of the web framework.
- **`app/mappers/`**: translation between API schemas and domain models.
- **`app/core/`**: config, logging, and shared exceptions/settings.

## 7. API Endpoints

Base URL: `http://localhost:8000`  
API prefix: `/api/v1`

### Health

- **GET** `/api/v1/health` — service health status.

### Explore

- **GET** `/api/v1/explore/locations` — list/filter locations.
  - Query params: `region`, `type`, `vibe` (all optional; enum-backed)

Example:

```bash
curl "http://localhost:8000/api/v1/explore/locations?region=NORTH&type=BEACH"
```

- **GET** `/api/v1/explore/ride-routes` — list/filter ride routes.
  - Query params (optional): `difficulty`, `road_type`, `surface`, `traffic`, `min_distance_km`, `max_distance_km`

Example:

```bash
curl "http://localhost:8000/api/v1/explore/ride-routes?difficulty=EASY&max_distance_km=60"
```

- **POST** `/api/v1/explore/context` — get context info for a location and time.

Example:

```bash
curl -X POST "http://localhost:8000/api/v1/explore/context" \
  -H "Content-Type: application/json" \
  -d '{
    "location_id": "candolim-beach",
    "day_type": "WEEKEND",
    "time_of_day": "SUNSET"
  }'
```

### Plan (AI)

- **POST** `/api/v1/plan/plan-ride` — generate an AI ride plan (STRICT JSON from LLM).

Request:

```bash
curl -X POST "http://localhost:8000/api/v1/plan/plan-ride" \
  -H "Content-Type: application/json" \
  -d '{
    "start_location": "Panjim",
    "ride_duration_hours": 4,
    "time_of_day": "MORNING"
  }'
```

Response shape:

```json
{
  "data": {
    "stops": ["..."],
    "total_distance": 0,
    "estimated_time": "...",
    "notes": "..."
  }
}
```

### Experience (AI)

- **POST** `/api/v1/experience/experience-from-mood` — mood → experience recommendation.

```bash
curl -X POST "http://localhost:8000/api/v1/experience/experience-from-mood" \
  -H "Content-Type: application/json" \
  -d '{
    "mood": "relaxed",
    "start_location": "Anjuna"
  }'
```

- **POST** `/api/v1/experience/best-sunset` — best sunset location within travel time.

```bash
curl -X POST "http://localhost:8000/api/v1/experience/best-sunset" \
  -H "Content-Type: application/json" \
  -d '{
    "current_location": "Baga",
    "travel_time_minutes": 35
  }'
```

### Chat (AI, streaming)

- **POST** `/api/v1/chat/ask-goa/stream` — stream an answer as plain text.

```bash
curl -N -X POST "http://localhost:8000/api/v1/chat/ask-goa/stream" \
  -H "Content-Type: application/json" \
  -d '{ "question": "What is a good sunrise spot near Panjim?" }'
```

### Personality (AI)

- **POST** `/api/v1/personality/goa-personality` — classify traveler personality from preferences.

```bash
curl -X POST "http://localhost:8000/api/v1/personality/goa-personality" \
  -H "Content-Type: application/json" \
  -d '{
    "preferences": ["quiet beaches", "sunsets", "cafes", "short rides"]
  }'
```

## 8. Running the Project Locally

### Prerequisites

- Python 3.10+ (recommended)
- Ollama installed and running locally

### Clone the repo

```bash
git clone <your-repo-url>
cd goa-explorer-api
```

### Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r goa-explorer-api/requirements.txt
```

### Run Ollama

1) Start Ollama (it listens on `http://localhost:11434` by default).

```bash
ollama serve
```

2) Pull the model used by this project (defaults to `llama3` in code):

```bash
ollama pull llama3
```

### Start the FastAPI server

Run from the `goa-explorer-api/` directory (the one containing `main.py`):

```bash
cd goa-explorer-api
uvicorn main:app --reload
```

## 9. API Documentation

Swagger UI is available at:

`http://localhost:8000/docs`

## 10. Example Output

Example response from **POST** `/api/v1/plan/plan-ride`:

```json
{
  "data": {
    "stops": [
      "Panjim Promenade",
      "Miramar Beach",
      "Dona Paula View Point",
      "Old Goa"
    ],
    "total_distance": 42.5,
    "estimated_time": "3h 45m",
    "notes": "A relaxed morning ride with scenic coastal stops and a heritage finish. Avoid peak traffic near Panjim around school hours."
  }
}
```

## 11. Learning Goals

This project was built as a learning exercise to explore:

- **Python backend development**
- **FastAPI architecture** (routers, schemas, dependency injection, middleware)
- **AI API integration with local LLMs** (Ollama + LangChain, structured JSON prompting, streaming responses)
