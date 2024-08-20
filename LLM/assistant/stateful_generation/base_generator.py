from abc import ABC, abstractmethod

class StatefulGenerator(ABC):
    def __init__(self, course_id: str):
        self.course_id = course_id
    
    def chat(self, message: str):
        # TODO: Implement this method

        raise NotImplementedError