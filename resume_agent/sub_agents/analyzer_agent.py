from google.adk.agents import Agent
from resume_agent.tools.resume_tools import compare_keywords

analyzer_agent = Agent(
    name="analyzer_agent",
    model="gemini-2.0-flash-lite",
    instruction="""You compare a resume against a job description.
    Find matching keywords, missing skills, and gaps.
    Give a match percentage and list what is missing.""",
    tools=[compare_keywords]
)