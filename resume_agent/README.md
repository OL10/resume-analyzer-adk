# Smart Resume Analyzer (Multi-Agent System using Google ADK)

## Overview
This project implements a multi-agent resume analysis system using Google ADK. The system analyzes a resume against a job description, performs market research using Google Search, compares keywords, and generates an improvement report.

## Architecture
The system consists of:
- Root Agent (Orchestrator)
- Extractor Agent (extracts resume content)
- Analyzer Agent (compares keywords)
- Suggester Agent (generates improvement suggestions)

Each agent is responsible for a specific task, ensuring modularity and orchestration.

## Tools Used
- Built-in: google_search (ADK)
- Custom:
  - extract_resume_text
  - compare_keywords
  - generate_report

## Setup Instructions
1. Create virtual environment
2. Install dependencies:
   pip install -r requirements.txt
3. Add GOOGLE_API_KEY to .env
4. Run:
   adk run resume_agent

## How It Works
User provides resume text and job description. The system extracts content, searches industry keywords, compares skills, and generates a structured improvement report.