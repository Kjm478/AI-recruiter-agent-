# AI Recruiter Agency

This repository contains a Streamlit-based web application for an AI-powered recruitment agency. The system processes resumes using a coordinated set of AI agents powered by Ollama (llama3.2), providing detailed analysis, job matching, screening, and recommendations. The application is built with a modular agent architecture and a user-friendly interface.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Resume Processing:** Upload PDF resumes for automated analysis.
- **AI Agents:**
  - **Extractor:** Extracts structured data (e.g., skills, experience, education) from resumes.
  - **Analyzer:** Analyzes candidate profiles for skills, experience level, and achievements.
  - **Matcher:** Matches candidates to job openings based on profile analysis.
  - **Screener:** Screens candidates for qualifications, relevance, and fit.
  - **Recommender:** Provides actionable recommendations and next steps.
  - **Orchestrator:** Coordinates the workflow across all agents.
- **Visualization:** Displays results in tabs with metrics like confidence scores and screening scores.
- **Local LLM Integration:** Uses Ollama (llama3.2) running locally for natural language processing.
- **Logging:** Includes error logging for debugging and monitoring.

## Requirements

- Python 3.8+
- Libraries:
  - `streamlit`
  - `asyncio`
  - `openai` (for Ollama integration)
  - `pdfminer.six` (for PDF text extraction)
  - `pathlib`
- **Ollama**: Local instance of llama3.2 running on `http://localhost:11434/v1`.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ai-recruiter-agency.git
   cd ai-recruiter-agency
