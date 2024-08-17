from typing import List, Dict

from assistant.llm import LLM
from assistant.stateful_generation.base_generator import StatefulGenerator

import json

class PeerDrivenInsight(StatefulGenerator):
    def __init__(self):
        self.llm = LLM()    
    
    def chat(self, messages: List[Dict[str, str]]):
        # Convert Pydantic objects to dicts first
        messages_dict = [message.dict() if hasattr(message, 'dict') else message for message in messages]
        
        # Convert dict to a JSON-formatted string
        messages_str = json.dumps(messages_dict, indent=2)
        
        # Insert the system message at the beginning of the conversation
        messages.insert(0, {
            "role": "system",
            "content": ("You are an expert at providing insights on academic content. "
                        "You will be given a list of peer driven insights from forum and you have to analyse the insights and then give a summary of what the peerss feel about the course and any other usefull information that the users who have done the course can be extraxted.\n"
                        "The peer insights are:\n" + messages_str+"\n so based on the peer reviews give a short overall review of the course.")
        })
        
        # Generate response from the LLM
        return self.llm.generate(messages)
