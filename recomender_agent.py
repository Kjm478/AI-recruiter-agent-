from typing import Dict, Any
from base_agent import BaseAgent
from datetime import datetime


class RecommenderAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name = "recommender",
            instructions = """Generate final recomendations considering : 
            1. extracted profile 
            2. skills analysis 
            3. job matches 
            4. Screening results 
            Provide clear next steps and specific recomendations 
            """
        )
        
    async def run(self, messages: Dict[str, Any]) -> Dict[str, Any]:
        print("Recommender: Generating final recommendations")
        
        workflow_content = eval(messages[-1]["content"])    
        final_recomendation = self.query_ollama(str(workflow_content))
        
        return {
            "final_recomendation": final_recomendation,
            "recomendation_timestamp": datetime.now().isoformat(),
            "confidence_leval": "high"
        }