from google.adk.agents import Agent
from google.adk.tools import google_search
from resume_agent.sub_agents.extractor_agent import extractor_agent
from resume_agent.sub_agents.analyzer_agent import analyzer_agent
from resume_agent.sub_agents.suggester_agent import suggester_agent

root_agent = Agent(
    name="resume_analyzer",
    model="gemini-2.0-flash-lite",
    instruction="""You are a smart resume analyzer coordinator.
    When user gives you a job description and resume text:
    1. Use extractor_agent to extract key details from resume
    2. Use analyzer_agent to compare resume with job description
    3. Use suggester_agent to suggest improvements
    4. Use google_search to search for industry keywords for the job role
    Give a final combined summary to the user.""",
    tools=[google_search],
    sub_agents=[extractor_agent, analyzer_agent, suggester_agent]
)