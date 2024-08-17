from typing import List, Dict

from assistant.llm import LLM
from assistant.stateful_generation.base_generator import StatefulGenerator

class PeerDrivenInsight(StatefulGenerator):
    def __init__(self, course_id: str):
        super().__init__(course_id)
        self.llm = LLM()    
    
    def chat(self, context:str, messages: List[Dict[str, str]]):
        messages.insert(0, {
            "role": "system",
            "content": ("You are an expert at providing insights on academic content.You will be given a context and a conversation. Provide insights on the conversation.\nThe context is:\n" + context)
        }) # Add the system message at the beginning of the conversation
        return self.llm.generate(messages)