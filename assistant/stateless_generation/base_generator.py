from abc import ABC, abstractmethod

class StatelessGenerator(ABC):
    def __init__(self, course_id: str, context:str):
        self.course_id = course_id
        self.context = context
    
    def get_data(self) -> str:
        return self.context