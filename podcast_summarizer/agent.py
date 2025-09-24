from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from . import prompt
from .sub_agents.sentiment_analyzer import sentiment_analyzer_agent
from .sub_agents.podcast_recommender import podcast_recommender_agent


# Initialize the language model with the API key from environment variables
MODEL = "gemini-2.5-flash"

podcast_coordinator = LlmAgent(
    name="podcast_coordinator",
    model=MODEL,
    description="A podcast summarization coordinator agent that uses " \
    "specialized tools to generate a comprehensive summary and sentiment analysis of podcast episode transcripts"
    "and suggest similar podcasts.",
    instruction=prompt.PODCAST_ANALYSIS_PROMPT,
    output_key="podcast_analysis",
    tools=[AgentTool(agent=sentiment_analyzer_agent), AgentTool(agent=podcast_recommender_agent)]
)

root_agent = podcast_coordinator



