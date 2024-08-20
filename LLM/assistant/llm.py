import os
from dotenv import load_dotenv
load_dotenv()

from typing import List, Dict

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

class LLM:
    def __init__(self, model="llama3-70b-8192", temperature=0):
        self.model = model
        self.client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )

    def generate(self, messages:List[Dict[str, str]]):
        chat_completion = self.client.chat.completions.create(
            messages=messages,
            model=self.model,
        )

        return chat_completion.choices[0].message.content
