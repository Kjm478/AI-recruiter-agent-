from typing import Dict, Any
import json
from datetime import datetime
from base_agent import BaseAgent

class MatcherAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="matcher",
                         instructions="""
                        Match candidate profiles with posted job positions. 
                        Consider: skills match, experience level, location preference, and other relevant factors.
                        Provide detailed reasoning and compatibility scores. 
                        Return matches in JSON format with title, match_score, and location.
                         """)
        
    async def run(self, messages: Dict[str, Any]) -> Dict[str, Any]:
        print("Matcher: Finding Suitable job matches")
        
        # Safely parse message content (assuming JSON input)
        try:
            workflow_content = json.loads(messages[-1]["content"])
        except (json.JSONDecodeError, TypeError):
            workflow_content = messages[-1]["content"]  # Fallback to string if not JSON
        
        # Get initial profile analysis from Ollama
        profile_prompt = f"Analyze this candidate profile and extract skills: {workflow_content}"
        matching_results = self.query_ollama(profile_prompt)  # Await since run is async
        
        # Parse the profile analysis (assuming Ollama returns a string)
        profile_data = self.parse_json(matching_results)
        skills = profile_data.get("skill_analysis", matching_results)  # Fallback to raw string if no JSON
        
        sample_jobs = [
            {"title": "Data Scientist", "required_skills": ["Python", "Machine Learning", "Statistics"], "location": "New York, NY"},
            {"title": "Software Engineer", "required_skills": ["Java", "Spring", "SQL"], "location": "San Francisco, CA"},
            {"title": "Product Manager", "required_skills": ["Product Management", "Agile", "UX"], "location": "Seattle, WA"}
        ]
        
        # Query Ollama for job matches
        matching_response = self.query_ollama(
            f"""Analyze the following profile and provide job matches in valid JSON format. 
            profile: {skills}
            available_jobs: {sample_jobs}
            
            Return ONLY a JSON object with this exact structure: 
            {{
                "matched_jobs": [
                    {{
                        "title": "Job Title",
                        "match_score": 85,
                        "location": "job location"
                    }}
                ],
                "matching_timestamp": "{datetime.now().isoformat()}",
                "number_of_matches": 2
            }}
             """
        )
        
        parsed_response = self.parse_json(matching_response)
       
        if "error" in parsed_response:
           return { 
                   "matched_jobs": [{"title": "No Matches Found", "match_score": 0, "location": "N/A"}],
                   "matching_timestamp": datetime.now().isoformat(),
                   "number_of_matches": 0
           }
           
        return parsed_response

# Make query_ollama async to match run
async def query_ollama(self, prompt: str) -> str:
    try:
        response = self.ollama_client.chat.completions.create(
            model="llama3.2",
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=2000,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error querying Ollama: {str(e)}")
        raise