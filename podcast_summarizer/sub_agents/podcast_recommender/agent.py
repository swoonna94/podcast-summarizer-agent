"""recommendation agent for analyzing podcast transcript."""

from google.adk import Agent
from google.genai import types

from . import prompt

MODEL = "gemini-2.5-flash"

podcast_recommender_agent = Agent(
    model=MODEL,
    name="podcast_recommender_agent",
    instruction=prompt.PODCAST_RECOMMENDATION_PROMPT,
    generate_content_config=types.GenerateContentConfig(
        temperature=0.1,
    ),
    output_key="podcast_recommendations"
)