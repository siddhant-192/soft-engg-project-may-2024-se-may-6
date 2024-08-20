<template>
  <div class="chatbox">
    <div class="chatbox-header">
      <h3>Chat with Us</h3>
    </div>
    <div class="chatbox-messages" ref="messages">
      <div v-for="(message, index) in messages" :key="index" :class="['message', message.sender]">
        {{ message.text }}
      </div>
    </div>
    <div class="chatbox-input">
      <input 
        type="text" 
        v-model="userInput" 
        @keyup.enter="sendMessage" 
        placeholder="Type a message..." 
      />
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    courseId: {
      type: String,  
      required: true
    }
  },
  data() {
    return {
      userInput: '',
      messages: [],
      course: null, 
      sessionId: localStorage.getItem('sessionId') || null 
    };
  },
  created() {
    if (this.courseId && this.courseId !== '0') {
      this.fetchCourseDetails();
    }
  },
  methods: {
    fetchCourseDetails() {
      axios.get(`http://localhost:8080/api/course/${this.courseId}`)
        .then(response => {
          this.course = response.data.data;
        })
        .catch(error => {
          console.error('Error fetching course details:', error);
        });
    },
    async sendMessage() {
      if (!this.userInput.trim()) return;

      const userMessage = {
        text: this.userInput,
        sender: 'user'
      };

      this.messages.push(userMessage);
      this.userInput = '';

      let context;

      if (this.courseId == '0') {
        context = 'You are a bot designed to help students understand and learn concepts.';
      } else {
        context = `name: ${this.course.name}, short_description: ${this.course.short_desc}, duration: ${this.course.duration} weeks, price: $${this.course.price}, instructor: ${this.course.instructor}, topics: ${Array.isArray(this.course.topics) ? this.course.topics.join(', ') : 'No specific topics provided'}`;
      }

      try {
        const payload = {
          course_id: this.courseId,
          message: {
            context: context,
            messages: this.messages.map(msg => ({
              role: msg.sender === 'user' ? 'user' : 'assistant',
              content: msg.text
            }))
          }
        };
        const response = await axios.post('http://localhost:80/api/v1/peer_driven_insights', payload);

        const botMessage = {
          text: JSON.stringify(response.data.response.response),
          sender: 'bot'
        };

        this.messages.push(botMessage);

        this.$nextTick(() => {
          this.$refs.messages.scrollTop = this.$refs.messages.scrollHeight;
        });

        if (!this.sessionId) {
          this.sessionId = response.data.sessionId;
          localStorage.setItem('sessionId', this.sessionId);
        }

      } catch (error) {
        console.error('Error sending message:', error);
      }
    }
  }
};
</script>

<style scoped>
body, html {
  height: 100%;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f0f0f0;
}

.chatbox {
  width: 570px;
  height: 500px;
  display: flex;
  margin-top: 30px;
  margin-left: 350px;
  flex-direction: column;
  border: 1px solid #ddd;
  border-radius: 15px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  font-family: 'Roboto', sans-serif;
  transition: transform 0.3s ease-in-out;
}

.chatbox:hover {
  transform: scale(1.02);
}

.chatbox-header {
  background-color: #4b5a96;
  color: white;
  padding: 20px;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
  text-align: center;
  font-weight: bold;
  font-size: 20px;
  border-bottom: 2px solid #4b5a96;
}

.chatbox-messages {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  background-color: #f5f5f5;
}

.message {
  margin-bottom: 20px;
  padding: 15px;
  border-radius: 15px;
  max-width: 75%;
  word-wrap: break-word;
  font-size: 14px;
  line-height: 1.4;
  animation: fadeIn 0.5s ease-in-out;
}

.message.user {
  background-color: #07908b;
  color: white;
  text-align: right;
  margin-left: auto;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.message.bot {
  background-color: #e0e0e0;
  color: #333;
  text-align: left;
  margin-right: auto;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.chatbox-input {
  display: flex;
  border-top: 2px solid #ddd;
  padding: 20px;
  background-color: #ffffff;
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
}

.chatbox-input input {
  flex: 1;
  padding: 12px;
  border: 2px solid #ddd;
  border-radius: 20px;
  font-size: 15px;
  outline: none;
  transition: border-color 0.3s ease-in-out;
}

.chatbox-input input:focus {
  border-color: #4b5a96;
}

.chatbox-input input::placeholder {
  color: #999;
}

.chatbox-input button {
  margin-left: 10px;
  padding: 12px 20px;
  border: none;
  background-color: #4b5a96;
  color: white;
  border-radius: 20px;
  cursor: pointer;
  font-size: 15px;
  font-weight: bold;
  transition: background-color 0.3s ease-in-out;
}

.chatbox-input button:hover {
  background-color: #4b5a96;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
