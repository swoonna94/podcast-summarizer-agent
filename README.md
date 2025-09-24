# Podcast Summarizer


## Overview

AI-driven agent designed to transform lengthy podcast transcripts into comprehensive, digestible summaries with sentiment analysis. Recognizing the challenge listeners face in extracting key insights from hour-long episodes, this agent offers a quick approach to podcast content consumption.

1. It accepts podcast transcripts as text input and analyzes the content to extract key takeaways, notable quotes, topics, and resources mentioned.
2. It leverages a specialized sentiment analysis sub-agent to evaluate emotional tones and speaker sentiments throughout the episode.
3. It uses a podcast recommendation sub-agent to suggest similar podcasts based on the analyzed content.
4. Finally, synthesizing all analyses, the agent produces a comprehensive summary including headline, key topics, target audience, sentiment insights, and podcast recommendations.

This capability aims to help podcast listeners quickly understand episode content, decide which episodes to fully listen to, retain important information from consumed content, and discover similar podcasts.


### Agent architecture:

This agent uses a coordinator-sub-agent architecture:
- **Podcast Coordinator Agent**: Main agent that processes transcripts and generates summaries
- **Sentiment Analyzer Sub-agent**: Specialized agent for emotional and sentiment analysis  
- **Podcast Recommender Sub-agent**: Finds and recommends similar podcasts using Google search

## Setup and Installation

1.  **Prerequisites**

    *   Python 3.8+
    *   Google ADK (Agent Development Kit)
    *   Google API Key (for Gemini models)

2.  **Installation**

    ```bash
    # Clone this repository
    git clone https://github.com/yourusername/podcast-summarizer-agent.git
    cd podcast-summarizer-agent
    
    # Install dependencies
    pip install -r requirements.txt
    ```

3.  **Configuration**

    *   Set up Google API credentials.
        *   Create a `.env` file in the project root:

        ```bash
        GOOGLE_GENAI_USE_VERTEXAI=FALSE
        GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
        ```
        * Get your API key from https://aistudio.google.com/apikey

## Running the Agent

**Using `adk`**

ADK provides convenient ways to bring up agents locally and interact with them.
You may talk to the agent using the CLI:

Use web interface:

```bash
adk web
```

The command `adk web` will start a web server on your machine and print the URL.
You may open the URL, select "podcast_summarizer" in the top-left drop-down menu, and
a chatbot interface will appear on the right.

### Example Interaction

Below is an example interaction with the Podcast Summarizer:

```
 * user: Hello, what can you do?

Hello! I am a Podcast Analysis Agent. My primary function is to analyze podcast scripts provided by you and help you quickly understand the podcast to save time.

I can:
- Summarize podcast episodes with headlines and key takeaways
- Extract main topics discussed (maximum 3 words each)
- Extract notable quotes and resources mentioned
- Identify the target audience
- Perform sentiment analysis on the entire episode
- Analyze speaker-specific sentiments
- Identify key emotional tones
- Recommend similar podcasts based on content analysis

Would you like to provide a podcast transcript for analysis?

 * user: [Provides podcast transcript]

Thank you for providing the transcript. I will now analyze it for you.

**Podcast Summary:**

**Headline:** This episode covers [main topic] with Host [name, credential] and Guests [name, credential].

**Topics:** [Topic 1], [Topic 2], [Topic 3]

**Episode Summary:** 
[Few sentences capturing the most important details]

**Key Takeaways:**
- [Key point 1]
- [Key point 2]
- [Key point 3]

**Resources Mentioned:**
- [Book/Website/Tool 1]
- [Book/Website/Tool 2]

**Notable Quotes:**
- "[Quote 1]"
- "[Quote 2]"

**Target Audience:** [Description of who would benefit most from this episode]

Now performing sentiment analysis...

**Sentiment Analysis Report:**

**Overall Sentiment:** Positive

**Speaker Sentiments:**
- Host: Curious and engaged
- Guest: Informative and enthusiastic

**Key Emotional Tones:** 
- [Tone 1]: [Associated statement]
- [Tone 2]: [Associated statement] 
- [Tone 3]: [Associated statement]

Would you like recommendations for similar podcasts?

**Podcast Recommendations:**
- [Similar Podcast 1] - [Link]
- [Similar Podcast 2] - [Link]
- [Similar Podcast 3] - [Link]

Would you like me to analyze another podcast transcript?
```

## Project Structure

```
podcast-summarizer-agent/
├── README.md                   # This file
├── .env                        # Environment variables (not tracked)
└── podcast_summarizer/         # Main package
    ├── __init__.py            # Package initialization
    ├── agent.py               # Main podcast coordinator agent
    ├── prompt.py              # Prompt templates for analysis
    └── sub_agents/            # Specialized sub-agents
        ├── sentiment_analyzer/
        │   ├── __init__.py
        │   ├── agent.py       # Sentiment analysis agent
        │   └── prompt.py      # Sentiment analysis prompts
        └── podcast_recommender/
            ├── __init__.py
            ├── agent.py       # Podcast recommendation agent
            └── prompt.py      # Recommendation prompts
```

## Key Components

### Podcast Coordinator Agent (`podcast_summarizer/agent.py`)
- **Model**: Gemini 2.5 Flash
- **Role**: Main orchestrator for podcast analysis
- **Responsibilities**:
  - Process podcast transcripts
  - Generate summaries (max 250 words)
  - Extract main topics (3 topics, max 3 words each)
  - Extract key takeaways, quotes, and resources
  - Identify target audience
  - Coordinate with sentiment analyzer and podcast recommender
  - Compile final analysis report

### Sentiment Analyzer Sub-agent (`sub_agents/sentiment_analyzer/agent.py`)
- **Model**: Gemini 2.5 Flash
- **Role**: Specialized emotional and sentiment analysis
- **Responsibilities**:
  - Analyze overall episode sentiment (Positive, Negative, Neutral, Mixed)
  - Identify speaker-specific sentiments
  - Detect 2-3 key emotional tones with associated statements
  - Provide detailed sentiment report

### Podcast Recommender Sub-agent (`sub_agents/podcast_recommender/agent.py`)
- **Model**: Gemini 2.5 Flash
- **Role**: Find and recommend similar podcasts
- **Responsibilities**:
  - Analyze podcast content and sentiment data
  - Use Google search to find similar podcasts
  - Provide curated list of podcast recommendations with links

## Acknowledgments

- Built with Google ADK (Agent Development Kit)
- Powered by Google Gemini AI models
- Inspired by the need for efficient podcast content consumption
