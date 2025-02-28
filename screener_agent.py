from typing import Dict, Any
from base_agent import BaseAgent
from datetime import datetime

#inherit from the BaseAgent class
class ScreenerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name = "screnner",
                         instructions=""""
                         Screen candidates based on:
                         -qualifications alignment
                         -experience relevance 
                         -skill match percentage 
                         -cultural fit indicators
                         -Red flags or concerns
                         Provide comprehensive screening reports
                         """""
        )
        
    async def run(self, messages: Dict[str, Any]) -> Dict[str, Any]:
        #screen the candidata
        print("Screener: Condutucitng initila screening")
        
        workflow_content = eval(messages[-1]["content"])
        screening_results = self.query_ollama(str(workflow_content))
        
        return {
            "screening_report": screening_results, 
            "screening_timestamp": datetime.now().isoformat(), 
            "screening_score": 90, 
        }