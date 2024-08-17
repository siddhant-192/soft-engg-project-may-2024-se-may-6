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
                        "You will be given a context and a conversation which will include chat from the user and your past response to that enquiry. Based on the past conversation you have to return a reply. There are 2 people in the conversation, the role with value user is is the user interacting with they system and the role with assistant is the replies you have given with respect to the conversation.\n"
                        "The past conversation is:\n" + messages_str+"\n so based on this conversation provide a reply and you can give empty reply.")
        })
        
        # Generate response from the LLM
        return self.llm.generate(messages)
