from google.adk.agents import Agent
from resume_agent.tools.resume_tools import generate_report

suggester_agent = Agent(
    name="suggester_agent",
    model="gemini-2.0-flash-lite",
    instruction="""You suggest improvements for a resume.
    Based on missing skills and gaps found:
    1. Suggest keywords to add
    2. Suggest how to rewrite weak sections
    3. Generate a final improvement report and save it.""",
    tools=[generate_report]
)