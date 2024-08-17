from assistant.llm import LLM
from assistant.stateless_generation.base_generator import StatelessGenerator

class CourseSummaries(StatelessGenerator):
    def __init__(self, course_id: str, context: str):
        super().__init__(course_id, context)
        self.llm = LLM()

    def generate(self):
        messages = [
            {
                "role": "system",
                "content": "You are an expert at summarizing academic content. You will be given contents of a course. Generate a summary of the course based on the given content. Keep the summary short and simple to understand."
            },
            {
                "role": "assistant",
                "content": "Here is the course content:\n " + self.get_data()
            }
        ]
        return self.llm.generate(messages)
