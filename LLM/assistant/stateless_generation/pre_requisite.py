from assistant.llm import LLM
from assistant.stateless_generation.base_generator import StatelessGenerator

class PreRequisite(StatelessGenerator):
    def __init__(self, course_id: str, context: str):
        super().__init__(course_id, context)
        self.llm = LLM()

    def generate(self):
        messages = [
            {
                "role": "system",
                "content": "You are an expert at identifying course prerequisites.You will be given contents of a course. Generate a check list of prerequisites for the given course. Give it as points structure that need to be covered before starting this course and keep it simple and short points."
                
            },
            {
                "role": "assistant",
                "content": "Here is the course content:\n " + self.get_data()
            }
        ]
        return self.llm.generate(messages)