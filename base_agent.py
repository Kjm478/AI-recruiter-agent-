from typing import Dict, Any 
import json 
from openai import OpenAI

class BaseAgent:
    def __init__(self, name: str, instructions: str):
        self.name = name
        self.instructions = instructions
        # overiding the openai swarm to use it in the local ollama
        self.ollama_client = OpenAI(
            base_url='http://localhost:11434/v1',
            api_key='ollama'
        )

    async def run (self, input: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError("Subclass must implement run()")
    
    def query_ollama(self, prompt: str) -> str:
        try: 
            response = self.ollama_client.chat.completions.create(
                model = "llama3.2", 
                messages = [
                    {"role": "system", "content": self.instructions},
                    {"role": "user", "content": prompt},
                ],
                temperature = 0.7, 
                max_tokens = 2000, 
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error querying the Ollama: {str(e)}")
            raise 
    
    #parse json 
    def parse_json(self, text: str) -> Dict[str, Any]:
        try: 
            start = text.find("{")  
            end = text.rfind("}") 
            if start != -1 and end != -1:
                json_str = text[start:end+1]
                return json.loads(json_str)
            return {"error": "No JSON object found"}
        except json.JSONDecodeError as e:
            return {"error": str(e)}