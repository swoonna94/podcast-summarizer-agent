"""sentiment analyzer agent for analyzing podcast transcript."""

from google.adk import Agent
from google.genai import types

from . import prompt

MODEL = "gemini-2.5-flash"

sentiment_analyzer_agent = Agent(
    model=MODEL,
    name="sentiment_analyzer_agent",
    instruction=prompt.SENTIMENT_ANALYSIS_PROMPT,
    generate_content_config=types.GenerateContentConfig(
        temperature=0.1,
        safety_settings=[
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            )
        ]
    ),
    output_key="sentiment_analysis"
)