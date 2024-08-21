# AI-Powered Learning Management System (LMS)

This project is an AI-driven Learning Management System (LMS) designed to enhance the learning experience by incorporating state-of-the-art generative AI features. This system helps students access quick course summaries, take prerequisite tests, participate in discussions, and more—all powered by AI.

## Key Features

1. **AI-Powered Course Summaries**: Generate concise summaries of course content, helping students quickly grasp the core concepts before enrolling.
2. **Prerequisite Assessments**: Allow students to assess their knowledge through prerequisite tests, helping them determine whether they are ready for the course.
3. **Peer-Driven Insights**: Enable students to ask questions and receive insights from their peers and AI-generated responses.
4. **Pop-up Quizzes**: Deliver real-time pop-up quizzes to assess students' understanding of course materials.
5. **AI Coding Assistant**: Assist students in solving coding assignments by providing hints, syntax suggestions, and feedback on their code.
6. **Forum Discussions**: Provide a discussion forum where students can engage with peers, ask questions, and receive AI-generated discussion summaries.

## Project Structure

### Frontend (Vue.js)
- **Course Catalog**: Users can browse through a catalog of available courses, filter by categories such as domain, organization, price, etc., and select courses based on their preferences.
- **Course Details**: Detailed information about each course, including fees, prerequisites, and learning objectives.
- **Course Summaries**: AI-powered component that generates concise summaries of courses, helping students quickly understand the content.
- **Quizzes**: Randomly generated quiz questions to test students' comprehension of course material.

### Backend (Flask + RESTful API)
- **Course Management**: Provides endpoints for managing courses, including creating, retrieving, and summarizing courses.
- **Prerequisite Assessments**: Provides endpoints for prerequisite tests and retrieving results.
- **Discussion Forum**: Allows users to participate in discussions and retrieve discussion summaries.
- **AI Assistants**: Includes AI-powered assistants for course summaries, pop-up quizzes, code assistance, and peer-driven insights.

### Generative AI Integration
- **LLM Models**: The system integrates with advanced language models like `Phi-3-Mini` and `LLaMa-70B` to generate text summaries, provide insights, and assist in coding assignments.
- **vLLM Inference Engine**: Optimizes performance for large language models by efficiently handling inference requests.

## Architecture

The system follows a modular architecture with separate components for course management, AI assistants, and forums. The key components include:

1. **Stateful and Stateless Generative AI Services**: Used for generating course summaries, managing student interactions, and delivering assessments.
2. **Structured and Redis Data Stores**: Used for storing and retrieving course-related data, session contexts, and user inputs.
3. **Vector Search Data Store**: Enables semantic searches within course materials and discussion topics to provide relevant results to the students.

## LLM Application

This project integrates advanced Large Language Models (LLM) to enhance various educational features within the Learning Management System. The LLM application is built using FastAPI and provides several endpoints to assist users with AI-powered responses, course summaries, coding assistance, quizzes, and peer-driven insights.

### Application Architecture

The application is built using a `FastAPI` backend, with models defined using Pydantic for request and response validation. The application is deployed with `Uvicorn` as the ASGI server and supports both stateful and stateless generation of content.

Key Middleware:
- **CORS Middleware**: Ensures that the application allows cross-origin requests from various frontends, making it accessible to all clients.

### LLM Endpoints

1. **Peer Driven Insights** (`/api/v1/peer_driven_insights`)
   - **Method**: POST
   - **Description**: Processes user inputs and generates peer-driven insights using stateful conversation context.
   - **Request Model**: `PeerDrivenInsightsRequest`
   - **Response Model**: `PeerDrivenInsightsResponse`

2. **Support Assistant** (`/api/v1/support_assistant`)
   - **Method**: POST
   - **Description**: Provides AI-powered support for answering course-related queries.
   - **Request Model**: `SupportAssistantRequest`
   - **Response Model**: `SupportAssistantResponse`

3. **Code Assistant** (`/api/v1/code_assistant`)
   - **Method**: POST
   - **Description**: Assists users in coding-related queries and provides suggestions or code completion based on the submitted code.
   - **Request Model**: `CodeAssistantRequest`
   - **Response Model**: `CodeAssistantResponse`

4. **Course Summaries** (`/api/v1/course_summaries`)
   - **Method**: POST
   - **Description**: Generates concise summaries of course content to help students quickly grasp the core concepts.
   - **Request Model**: `CourseSummariesRequest`
   - **Response Model**: JSON object containing the generated summaries.

5. **Pop Quiz** (`/api/v1/pop_quiz`)
   - **Method**: POST
   - **Description**: Generates pop-up quizzes to assess a student's understanding of course content in real-time.
   - **Request Model**: `PopQuizRequest`
   - **Response Model**: JSON object containing the generated quiz questions.

6. **Prerequisite Assessment** (`/api/v1/prerequisite_assessment`)
   - **Method**: POST
   - **Description**: Conducts a prerequisite assessment to evaluate whether a student is ready to take a specific course.
   - **Request Model**: `PrerequisiteAssessment`
   - **Response Model**: JSON object containing the assessment results.

## API Endpoints

Key API endpoints include:

- `/api/courses`: Manages course-related operations (e.g., fetching, creating courses).
- `/api/courses/{course_id}/summarise`: Generates a summary for a specific course.
- `/api/courses/{course_id}/prerequisites`: Manages prerequisite tests and their results.
- `/api/discussions`: Handles the creation and retrieval of discussion topics.
- `/api/support/ai`: Provides AI-powered support for student queries.
- `/api/courses/{course_id}/quizzes/popup`: Manages the pop-up quiz for real-time assessments.
- `/api/courses/{course_id}/assignments`: Handles coding assignment submissions and provides hints.

For detailed API documentation, please refer to the [API Documentation](https://github.com/siddhant-192/soft-engg-project-may-2024-se-may-6).

## Testing

Unit tests are included for each API endpoint, testing both successful and error scenarios. The key test cases include:

1. Fetching courses and course details
2. Submitting prerequisite test answers and retrieving results
3. Creating and fetching discussion topics
4. Generating AI-based course summaries
5. Handling pop-up quizzes and retrieving results
6. Assisting with coding assignments

## Installation & Setup

To set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/siddhant-192/soft-engg-project-may-2024-se-may-6.git
   cd soft-engg-project-may-2024-se-may-6
   ```

### Setup the LMS part:
1. Install the required dependencies:
   ```bash
   cd LMS
   pip install -r lms-backend/data/requirements.txt
   npm install
   ```

2. Run the backend server:
   ```bash
   python lms-backend/data/main.py
   ```

3. Run the frontend server:
   ```bash
   cd lms-frontend
   npm run serve
   ```

4. Access the application at `http://localhost:8080`.

### Setup the LLM part
1. Install the required dependencies:
   ```bash
   cd LLM
   pip install -r requirements.txt
   ```

2. Get the API key from Groq and put as environment variable as GROQ_API_KEY
   (https://console.groq.com/keys)
   
2. Run the backend server for the LLM application:
   ```bash
   python app/app.py
   ```


## Team

- **Kushan Sharma** (LMS Team Developer)
- **Aditya Kapadia** (Project Management, Scrum Master)
- **Siddhant Mantri** (LLM Team Developer)
- **Aditya Khanna** (Project Management, Scrum Master)
- **Supreeth Rao** (LLM Team Developer)
- **Rohit Shinde** (LMS Team Developer)
- **Abhinav Udupi** (LMS Team Developer)
- **Kumar Gaurav** (LMS Team Developer)
