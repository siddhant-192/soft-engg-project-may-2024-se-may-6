from assistant.llm import LLM
from assistant.stateless_generation.base_generator import StatelessGenerator

class PopQuiz(StatelessGenerator):
    def __init__(self, course_id: str, context: str):
        super().__init__(course_id, context)  # Make sure both arguments are passed correctly
        self.llm = LLM()

    def generate(self):
        messages = [
            {
                "role": "system",
                "content": "You are an expert at creating pop quizzes. You will be given the contents of a course for which you will create pop quiz which should be simple and test the basic understanding of the given concepts. Based on the context given, generate a pop quiz with 10 questions in the format of a list of JSON objects, where each object contains the question, options, and answer. Only return the list of JSON objects. Do not include any other text."
            },
            {
                "role": "assistant",
                "content": "Here is the course content:\n" + self.get_data()
            }
        ]
        return self.llm.generate(messages)