import json
from typing import List, Dict

from assistant.llm import LLM
from assistant.stateful_generation.base_generator import StatefulGenerator

class SupportAssistant(StatefulGenerator):
    def __init__(self, course_id: str):
        super().__init__(course_id)
        self.llm = LLM()    
    
    def chat(self, context: str, messages: List[Dict[str, str]]):
        # Convert Pydantic objects to dicts first if needed
        messages_dict = [message.dict() if hasattr(message, 'dict') else message for message in messages]
        
        # Convert dict to a JSON-formatted string for context
        context_str = json.dumps(context)
        
        # Insert the system message at the beginning of the conversation
        messages_dict.insert(0, {
            "role": "system",
            "content": ("You are an expert chatbot. You will be given some context, and questions will be asked based on the context. "
                        "Provide answers to the questions based on the context.\nThe context is:\n" + context)
        })
        
        # Generate response from the LLM
        return self.llm.generate(messages_dict)
