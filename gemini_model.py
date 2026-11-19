import os

from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel, set_tracing_disabled

load_dotenv(override=True)

# Tracing uploads to OpenAI, so it is turned off when running on Gemini
set_tracing_disabled(True)

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
# Gemini often returns 503 (overloaded) / 429 (rate limit); retry with exponential backoff
gemini_client = AsyncOpenAI(
    base_url=GEMINI_BASE_URL,
    api_key=os.getenv("GOOGLE_API_KEY"),
    max_retries=6,
    timeout=120,
)

# One free model shared by all agents
MODEL = OpenAIChatCompletionsModel(
    model=os.getenv("DEFAULT_MODEL_NAME", "gemini-3.1-flash-lite"),
    openai_client=gemini_client,
)
