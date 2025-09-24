# Podcast Summarizer


## Overview

AI-driven agent designed to transform lengthy podcast transcripts into comprehensive, digestible summaries with sentiment analysis. Recognizing the challenge listeners face in extracting key insights from hour-long episodes, this agent offers a quick approach to podcast content consumption.

1. It accepts podcast transcripts as text input and analyzes the content to extract key takeaways, notable quotes, and resources mentioned.
2. It leverages a specialized sentiment analysis sub-agent to evaluate emotional tones and speaker sentiments throughout the episode.
3. Finally, synthesizing the content analysis with sentiment findings, the agent produces a comprehensive summary including headline, key points, target audience, and emotional dynamics.

This capability aims to help podcast listeners quickly understand episode content, decide which episodes to fully listen to, and retain important information from consumed content.

## Agent Details

The key features of the Podcast Summarizer include:

| Feature | Description |
| --- | --- |
| **Interaction Type** | Conversational |
| **Complexity**  | Easy |
| **Agent Type**  | Multi Agent |
| **Components**  | Sub-agent: Sentiment Analyzer |
| **Vertical**  | Media & Entertainment |



### Agent architecture:

This agent uses a coordinator-sub-agent architecture:
- **Podcast Coordinator Agent**: Main agent that processes transcripts and generates summaries
- **Sentiment Analyzer Sub-agent**: Specialized agent for emotional and sentiment analysis

## Setup and Installation

1.  **Prerequisites**

    *   Python 3.8+
    *   Google ADK (Agent Development Kit)
    *   A Google Cloud Platform project (for Vertex AI deployment)
    *   Google API Key (for Gemini models)

2.  **Installation**

    ```bash
    # Clone this repository
    git clone https://github.com/yourusername/podcast-summarizer.git
    cd podcast-summarizer
    
    # Install dependencies
    pip install google-generativeai python-dotenv
    ```

3.  **Configuration**

    *   Set up Google API credentials.

        *   Create a `.env` file in the project root:

        ```bash
        GOOGLE_API_KEY=your_google_api_key_here
        ```

        *   For Vertex AI deployment (optional):

        ```bash
        export GOOGLE_GENAI_USE_VERTEXAI=true
        export GOOGLE_CLOUD_PROJECT=<your-project-id>
        export GOOGLE_CLOUD_LOCATION=<your-project-location>
        ```

## Running the Agent

**Using `adk`**

ADK provides convenient ways to bring up agents locally and interact with them.
You may talk to the agent using the CLI:

```bash
adk run podcast_summarizer
```

Or on a web interface:

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
- Extract notable quotes and resources mentioned
- Identify the target audience
- Perform sentiment analysis on the entire episode
- Analyze speaker-specific sentiments
- Identify key emotional tones

Would you like to provide a podcast transcript for analysis?

 * user: [Provides podcast transcript]

Thank you for providing the transcript. I will now analyze it for you.

**Podcast Summary:**

**Headline:** This episode covers [main topic] with guest [name, credential].

**Key Takeaways:**
- [Key point 1]
- [Key point 2]
- [Key point 3]

**Resources Mentioned:**
- [Book/Website/Tool 1]
- [Book/Website/Tool 2]

**Episode Summary:** 
[2-3 sentences capturing the most important details]

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

**Key Emotional Tones:** [Excitement, Hope, Curiosity]

Would you like me to analyze another podcast transcript?
```

## Project Structure

```
podcast-summarizer/
├── __init__.py                 # Package initialization
├── agent.py                    # Main podcast coordinator agent
├── prompt.py                   # Prompt templates for analysis
├── .env                        # Environment variables (not tracked)
├── README.md                   # This file
└── sub_agents/                 # Specialized sub-agents
    └── sentiment_analyzer/
        ├── __init__.py
        ├── agent.py           # Sentiment analysis agent
        └── prompt.py          # Sentiment analysis prompts
```

## Key Components

### Podcast Coordinator Agent (`agent.py`)
- **Model**: Gemini 2.5 Flash
- **Role**: Main orchestrator for podcast analysis
- **Responsibilities**:
  - Process podcast transcripts
  - Generate summaries with configurable word limits
  - Extract key takeaways, quotes, and resources
  - Identify target audience
  - Coordinate with sentiment analyzer
  - Compile final analysis report

### Sentiment Analyzer Sub-agent (`sub_agents/sentiment_analyzer/agent.py`)
- **Model**: Gemini 2.5 Flash Lite
- **Role**: Specialized emotional and sentiment analysis
- **Responsibilities**:
  - Analyze overall episode sentiment
  - Identify speaker-specific sentiments
  - Detect key emotional tones
  - Provide detailed sentiment report

## Customization

The Podcast Summarizer can be customized to better suit your requirements:

1. **Adjust Summary Length**: Modify the `word_limit` parameter in the prompt template to control summary verbosity.

2. **Add Topic Extraction**: Implement additional analysis to automatically identify and categorize discussion topics.

3. **Integrate Transcription**: Add audio-to-text capabilities using Whisper or other ASR models to process audio files directly.

4. **Enhanced Speaker Diarization**: Improve speaker identification and tracking throughout the episode.

5. **Custom Output Formats**: Add support for different output formats (JSON, Markdown, PDF) based on user preference.

6. **Language Support**: Extend the agent to support multiple languages for international podcast content.

7. **Integration with Podcast Platforms**: Connect with podcast RSS feeds or APIs to automatically fetch and process new episodes.

## Testing

To test the agent with sample podcast transcripts:

```bash
# Run with sample transcript
python -m podcast_summarizer.agent < sample_transcript.txt
```

## Deployment

For deployment to Vertex AI Agent Engine:

```bash
# Install deployment dependencies
pip install google-cloud-aiplatform

# Deploy the agent
python deployment/deploy.py --create
```

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - See LICENSE file for details

## Acknowledgments

- Built with Google ADK (Agent Development Kit)
- Powered by Google Gemini AI models
- Inspired by the need for efficient podcast content consumption