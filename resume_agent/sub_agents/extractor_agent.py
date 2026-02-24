from google.adk.agents import Agent
from resume_agent.tools.resume_tools import extract_resume_text

extractor_agent = Agent(
    name="extractor_agent",
    model="gemini-2.0-flash-lite",
    instruction="""You extract key information from resumes.
    Extract: name, skills, experience, education, projects.
    Return it in a clean structured format.""",
    tools=[extract_resume_text]
)