<template>
  <div class="container">
    <h1>Programming Assignment</h1>
    <div ref="editor" class="editor"></div> <br>
    <button class="my-button" @click="runCode">Run Code</button>
    <div v-if="output" class="output-section">
      <h3>Output:</h3>
      <pre class="output">{{ output }}</pre>
    </div>
    <div v-if="error" class="error-section">
      <h3>Error:</h3>
      <pre class="error">{{ error }}</pre>
      <h3>Hint:</h3>
      <pre class="hint">{{ hint }}</pre>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import * as ace from 'ace-builds/src-noconflict/ace';
import 'ace-builds/src-noconflict/mode-python';
import 'ace-builds/src-noconflict/theme-monokai';

export default {
  data() {
    return {
      editor: null,
      output: "",
      error: "",
      hint: "",
    };
  },
  mounted() {
    this.editor = ace.edit(this.$refs.editor, {
      mode: "ace/mode/python",
      theme: "ace/theme/monokai",
      value: "# Write your Python code here",
    });
  },
  methods: {
    async runCode() {
      const userCode = this.editor.getValue();
      this.output = "";
      this.error = "";
      this.hint = "";

      try {
        const response = await axios.post(
          "https://judge0-ce.p.rapidapi.com/submissions",
          {
            source_code: userCode,
            language_id: 71,
          },
          {
            headers: {
              "Content-Type": "application/json",
              "X-RapidAPI-Key": "9be19fa8d5mshe96982d0d651372p17c0bajsn156ad20caa4d",
              "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com",
            },
            params: {
              base64_encoded: false,
              wait: true,
            },
          }
        );

        const result = response.data;
        this.output = result.stdout || "";
        this.error = result.stderr || "";

        if (this.error) {
          await this.getHint(this.error, userCode);
        }
      } catch (err) {
        console.error("Error submitting code to Judge0:", err);
        this.error = "Failed to submit code. Please check your network connection and API endpoint.";
      }
    },
    async getHint(error, program) {
      try {
        console.log("calling hint");
        program = JSON.stringify(program) ;
        console.log(program);
        const aiResponse = await axios.post(
          "http://localhost:80/api/v1/code_assistant",
          {
            course_id: "0", 
            program: program
          },
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        );
        console.log(aiResponse);
        this.hint = aiResponse.data.response || "No hint available.";
      } catch (err) {
        console.error("Error getting hint from AI:", err);
      }
    },
  },
};
</script>

<style>
.container {
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
}

h1 {
  font-family: 'Roboto', sans-serif;
  font-size: 2rem;
  color: #333;
  margin-bottom: 20px;
  text-align: center;
}

.editor {
  height: 300px;
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.my-button {
  background-color: #0478ff;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  font-size: 18px;
  font-family: 'Roboto', sans-serif;
  color: white;
  padding: 10px 20px;
  margin: 20px 0;
  cursor: pointer;
  transition: background-color 0.3s ease;
  display: block;
  width: 100%;
  text-align: center;
}

.my-button:hover {
  background-color: #005fcc;
}

.output-section, .error-section {
  margin-top: 20px;
  padding: 15px;
  border-radius: 8px;
}

.output-section h3, .error-section h3 {
  font-family: 'Roboto', sans-serif;
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.output {
  font-family: 'Courier New', monospace;
  background-color: #e8ffe8;
  padding: 10px;
  border-radius: 4px;
  white-space: pre-wrap;
}

.error {
  font-family: 'Courier New', monospace;
  background-color: #ffe8e8;
  padding: 10px;
  border-radius: 4px;
  white-space: pre-wrap;
}

.hint {
  font-family: 'Courier New', monospace;
  background-color: #fff8e8;
  padding: 10px;
  border-radius: 4px;
  white-space: pre-wrap;
}
</style>
