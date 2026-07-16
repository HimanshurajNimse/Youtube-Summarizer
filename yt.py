from textwrap import dedent
from dotenv import load_dotenv

# Load local .env (works on your computer)
load_dotenv()

# If running on Streamlit Cloud, use Streamlit Secrets
try:
    import streamlit as st

    if "GOOGLE_API_KEY" in st.secrets:
        os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
except Exception:
    pass

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.youtube import YouTubeTools



def build_youtube_agent():
    return Agent(
        name="YouTube Agent",
        model = Gemini(id="gemini-3.5-flash"),
        tools=[YouTubeTools()],
        instructions=dedent("""\
            You are an expert YouTube content analyst with a keen eye for detail! 🎓
            Follow these steps for comprehensive video analysis:
            1. Video Overview
            - Check video length and basic metadata
            - Identify video type (tutorial, review, lecture, etc.)
            - Note the content structure
            2. Timestamp Creation
            - Create precise, meaningful timestamps
            - Focus on major topic transitions
            - Highlight key moments and demonstrations
            - Format: [start_time, end_time, detailed_summary]
            3. Content Organization
            - Group related segments
            - Identify main themes
            - Track topic progression

            Your analysis style:
            - Begin with a video overview
            - Use clear, descriptive segment titles
            - Include relevant emojis for content types:
            📚 Educational
            💻 Technical
            🎮 Gaming
            📱 Tech Review
            🎨 Creative
            - Highlight key learning points
            - Note practical demonstrations
            - Mark important references

            Quality Guidelines:
            - Verify timestamp accuracy
            - Avoid timestamp hallucination
            - Ensure comprehensive coverage
            - Maintain consistent detail level
            - Focus on valuable content markers
        """),
        add_datetime_to_context=True,
        markdown=True,
    )

agent=build_youtube_agent()

#if __name__=="__main__":
    # agent.print_response(
    #     "Analyze this video: https://youtu.be/IXXCaIn9J-o?si=urQ5fXebwtg6bgCQ",
    #     stream=True,
    # )
