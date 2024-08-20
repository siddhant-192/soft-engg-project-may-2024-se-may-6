import requests
import base64
import time
from assistant.llm import LLM
from assistant.stateless_generation.base_generator import StatelessGenerator

class CodeAssistant(StatelessGenerator):
    def __init__(self, course_id: str, context: str = "default context"):
        super().__init__(course_id, context)
        self.llm = LLM()
        self.api_url = "https://judge0-ce.p.rapidapi.com/submissions?base64_encoded=true&wait=false&fields=*"
        self.api_key = "6efdc2a7bamsh3439bce5f1dc05ap1442b0jsn4cb5c8590aba"  # Replace with your own key
        self.language_id = 71  # Example language_id for Python 3, adjust based on user's language choice

    def send_code_to_judge0(self, program: str, stdin: str = "") -> dict:
        # Encode the source code and stdin in base64
        encoded_program = base64.b64encode(program.encode('utf-8')).decode('utf-8')
        encoded_stdin = base64.b64encode(stdin.encode('utf-8')).decode('utf-8')

        # Prepare the payload
        payload = {
            "language_id": self.language_id,
            "source_code": encoded_program,
            "stdin": encoded_stdin
        }

        headers = {
            'x-rapidapi-key': self.api_key,
            'x-rapidapi-host': "judge0-ce.p.rapidapi.com",
            'Content-Type': "application/json"
        }

        # Send the code to Judge0 API
        response = requests.post(self.api_url, json=payload, headers=headers)
        
        if response.status_code != 201:
            return {"error": f"Failed to submit code: {response.status_code}"}

        # Parse the response to get the submission token
        submission_data = response.json()
        return submission_data

    def get_judge0_result(self, token: str) -> dict:
        # Poll for the result until the execution is completed
        url = f"https://judge0-ce.p.rapidapi.com/submissions/{token}?base64_encoded=true&fields=*"
        headers = {
            'x-rapidapi-key': self.api_key,
            'x-rapidapi-host': "judge0-ce.p.rapidapi.com"
        }

        while True:
            response = requests.get(url, headers=headers)
            result = response.json()

            # Check if the submission is completed
            if result.get("status", {}).get("id") in {1, 2}:  # Status id 1 or 2 means in queue or processing
                time.sleep(2)  # Wait for a while before checking again
            else:
                return result

    def generate(self, program: str, stdin: str = ""):
        # Send the code to Judge0 API
        submission_data = self.send_code_to_judge0(program, stdin)
        
        # Check if an error occurred during submission
        if "error" in submission_data:
            return submission_data["error"]

        token = submission_data.get("token")
        if not token:
            return "Error: Unable to submit code."

        # Get the result of the code execution
        result = self.get_judge0_result(token)

        # Check if there were any errors in code execution
        if result.get("status", {}).get("description") != "Accepted":
            error_message = result.get("stderr") or "An error occurred."
            return f"Error in code execution: {error_message}"

        # Get the output of the program
        output = base64.b64decode(result.get("stdout")).decode('utf-8') if result.get("stdout") else "No output."

        # Use the output to generate suggestions via LLM
        llm_message = [
            {
                "role": "system",
                "content": "You are a code assistant. You will be given output to code and you have to give proper recommendation to the user. You will also be given access to the code that was compiled. Based on all of that give the recommendation for the code. if there is an error give the problem and suggest corrections. if the code has compiled successfully then you can give suggestions to make the code better."
            },
            {
                "role": "assistant",
                "content": f"Code executed:\n{program} . Here is the output:\n{output}"
            }
        ]

        # Generate LLM-based suggestions based on the code output
        return self.llm.generate(llm_message)
