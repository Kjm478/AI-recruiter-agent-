from typing import Dict, Any
from swarm import Agent 

def profile_enhancer_agent(extracted_info: Dict[str, Any]) -> Dict[str, Any]:
    #enhance the profile
   enhanced_profile = extracted_info.copy()
   total_experience_years = sum(item['years'] for item in extracted_info['experience'])
   enhanced_profile['summary'] = (f"""{extracted_info['name']} has {total_experience_years} years of experience in {extracted_info['industry']} industry.
    """)
   
   return enhanced_profile

profile_enhancer_agent = Agent(
    name = "profile_enhancer_agent",
    model = "llama3.2",
    instructions = "Enhance the extracted profile information by adding a summary of the candidate's experience and skills.",
    functions = [profile_enhancer_agent],
    
    )
   