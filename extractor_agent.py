from typing import Dict, Any
from pdfminer.high_level import extract_text
from base_agent import BaseAgent

class ExtractorAgent(BaseAgent): 
    def __init__(self):
        super().__init__(name = "extractor",
                         instructions=""""
                         Extract and structure information from  resumes. 
                         focus on: personal information, work experience, education, skills, and certifications. 
                         provide output in a clear structured format
                         """""
        )
        
    async def run (self , messages: Dict[str, Any]) -> Dict[str, Any]:
        #extract the resume content 
        print("Extractor: Extracting resume content")
        
        #parse the resume content 
        resume_data = eval(messages[-1]["content"]) 
        
        if resume_data.get("file_path"):
            raw_text = extract_text(resume_data["file_path"])
        else: 
            raw_text = resume_data.get("text", "")
            
        #get structured information from ollama 
        extracted_info = self.query_ollama(raw_text)
        
        return {
            "raw_text": raw_text,
            "structured_data": extracted_info,
            "extraction_status": "completed",
        }
        
    