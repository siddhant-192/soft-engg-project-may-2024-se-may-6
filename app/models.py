from pydantic import BaseModel
from typing import List

class MessagePrimitive(BaseModel):
    role: str
    content: str

class ChatMessage(BaseModel):
    context: str
    messages: List[MessagePrimitive]

class ChatResponse(BaseModel):
    response: str

class PeerDrivenInsights(BaseModel):
    message: ChatMessage

class PeerDrivenInsightsResponse(BaseModel):
    response: ChatResponse

class SupportAssistantRequest(BaseModel):
    course_id: str
    message: ChatMessage

class SupportAssistantResponse(BaseModel):
    response: ChatResponse

class CodeAssistantRequest(BaseModel):
    course_id: str
    program: str

class CodeAssistantResponse(BaseModel):
    response: str

class CourseSummariesRequest(BaseModel):
    course_id: str
    context: str

class PopQuizRequest(BaseModel):
    course_id: str
    context: str

class PrerequisiteAssessment(BaseModel):
    course_id: str
    context: str