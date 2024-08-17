import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import sys
import os

# Add the parent directory of the 'app' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import (
    ChatResponse, 
    CodeAssistantRequest, 
    CodeAssistantResponse, 
    CourseSummariesRequest, 
    PeerDrivenInsights, 
    PopQuizRequest, 
    PeerDrivenInsightsResponse, 
    SupportAssistantRequest, 
    SupportAssistantResponse, 
    PrerequisiteAssessment
)

from assistant.stateless_generation.course_summaries import CourseSummaries
from assistant.stateless_generation.pop_quiz import PopQuiz
from assistant.stateless_generation.pre_requisite import PreRequisite
from assistant.stateless_generation.code_assistant import CodeAssistant

from assistant.stateful_generation.peer_driven_insight import PeerDrivenInsight
from assistant.stateful_generation.support_assistant import SupportAssistant


app = FastAPI()
  
app.add_middleware(  
    CORSMiddleware,  
    allow_origins=["*"],  
    allow_credentials=True,  
    allow_methods=["*"],  
    allow_headers=["*"],  
)  

# Stateful Generators
@app.post("/api/v1/peer_driven_insights", response_model=PeerDrivenInsightsResponse)
async def process_peer_driven_insights(insights: PeerDrivenInsightsRequest):
    # Instantiate the logic class PeerDrivenInsight
    insight_generator = PeerDrivenInsight()  # Notice we are using PeerDrivenInsight, not PeerDrivenInsightsRequest
    # Generate the response using the chat method
    response_content = insight_generator.chat(insights.message.messages)
    
    # Wrap the response in the correct Pydantic model
    return PeerDrivenInsightsResponse(response=ChatResponse(response=response_content))


@app.post("/api/v1/support_assistant", response_model=SupportAssistantResponse)
async def process_support_assistant(assistant: SupportAssistantRequest):
    # Create an instance of your logic class SupportAssistant
    support_assistant = SupportAssistant(assistant.course_id)
    
    # Generate response using your logic class, ensuring Pydantic messages are handled correctly
    response_content = support_assistant.chat(assistant.message.context, assistant.message.messages)
    
    # Return the response wrapped in the Pydantic response model
    return SupportAssistantResponse(response=ChatResponse(response=response_content))


@app.post("/api/v1/code_assistant", response_model=CodeAssistantResponse)
async def process_code_assistant(assistant: CodeAssistantRequest):
    # Instantiate the business logic class (CodeAssistant)
    code_helper = CodeAssistant(assistant.course_id)
    # Generate the response using the logic class
    response_content = code_helper.generate(assistant.program)
    # Return the response wrapped in the correct Pydantic model
    return CodeAssistantResponse(response=response_content)


# Stateless Generators

@app.post("/api/v1/course_summaries")
async def get_course_summaries(summaries: CourseSummariesRequest):
    # Instantiate the business logic class
    summaries_generator = CourseSummaries(summaries.course_id, summaries.context)
    
    # Generate the summaries using the business logic
    response_content = summaries_generator.generate()
    
    # Return the result wrapped in a standard dictionary or a Pydantic response model
    return {"summaries": response_content}

@app.post("/api/v1/pop_quiz")
async def initiate_pop_quiz(quiz: PopQuizRequest):
    # Instantiate the business logic class
    pop_quiz_generator = PopQuiz(quiz.course_id, quiz.context)
    
    # Generate the quiz using the logic class
    response_content = pop_quiz_generator.generate()
    
    # Return the result as a dictionary or a Pydantic model
    return {"quiz": response_content}

@app.post("/api/v1/prerequisite_assessment")
async def conduct_prerequisite_assessment(assessment: PrerequisiteAssessment):
    prerequisite_assessment = PreRequisite(assessment.course_id, assessment.context)
    return {"assessment": prerequisite_assessment.generate()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)