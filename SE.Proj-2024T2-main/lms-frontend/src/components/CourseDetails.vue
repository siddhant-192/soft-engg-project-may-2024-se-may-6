<template>
  <div v-if="course" class="course-details">
    <h1>{{ course.name }} Course</h1>
    <h2>{{ course.name }}</h2>
    <p>{{ course.short_desc }}</p>
    <p>{{ course.desc }}</p>

    <div class="instructor-info">
      <h3>by {{ course.instructor }}</h3>
    </div>
    <p><strong>Course ID:</strong> {{ course.id }}</p>
    <p><strong>Duration:</strong> {{ course.duration }} weeks</p>
    <p><strong>Price:</strong> ${{ course.price }}</p>

    <h3>Course Structure & Assessments</h3>
    <p>{{ course.structure || 'Details not provided' }}</p>

    <ul v-if="showAllWeeks">
      <li v-for="(week, index) in course.weeks" :key="index">
        WEEK {{ index + 1 }}: {{ week }}
      </li>
    </ul>
    <button class="toggle-weeks" @click="toggleShowAllWeeks">{{ showAllWeeks ? 'Hide' : 'Show' }} all weeks</button>

    <h3>Prescribed Books</h3>
    <ul>
      <li v-for="(book, index) in course.books" :key="index">{{ book }}</li>
    </ul>

    <div class="actions">
      <button @click="summarizeCourse">Summarize Course</button>
      <button @click="takePrerequisiteTest">Take Prerequisite Test</button>
      <button 
        :class="{
          'register-button': true,
          'gray': !testPassed && prerequisiteTestCompleted,
          'green': testPassed,
          'red': !testPassed && prerequisiteTestCompleted
        }" 
        :disabled="!prerequisiteTestCompleted || !testPassed"
        @click="registerCourse"
      >
        Register
      </button>    
    </div>

    <h3>Reviews</h3>
    <div class="reviews">
      <div v-for="review in course.reviews" :key="review.id" class="review">
        <p>{{ review.comment }} - {{ review.rating }}/5</p>
      </div>
    </div>

    <div class="icons">
      <i class="like-icon" @click="likeCourse">👍</i>
      <i class="share-icon" @click="shareCourse">🔗</i>
    </div>

    <div v-if="summary" class="summary">
      <h3>Course Summary</h3>
      <p>{{ summary.summaries }}</p>
    </div>

    <button class="chatbot-toggle" @click="toggleChatBot">
      🗨️
    </button>
    <ChatBot v-if="showChatBot" ref="chatbot" :courseId="cid"></ChatBot>
  </div>
</template>


<script>
import axios from 'axios';
import ChatBot from './ChatBot.vue'

export default {
  name: "CourseDetails",
  components: {
    ChatBot,
  },
  data() {
    return {
      cid: null,
      course: null,
      showAllWeeks: false,
      summary: null,
      testPassed: false,
      prerequisiteTestCompleted: false,
      showChatBot: false, 
    };
  },
  methods: {
    fetchCourseDetails() {
      axios.get(`http://localhost:8080/api/course/${this.cid}`)
        .then(response => {
          this.course = response.data.data;
        })
        .catch(error => {
          console.error('Error fetching course details:', error);
        });
    },
    toggleShowAllWeeks() {
      this.showAllWeeks = !this.showAllWeeks;
    },
    summarizeCourse() {
      const context = `
        Course Name: ${this.course.name}
        Course Short Description: ${this.course.short_desc}
        Course Description: ${this.course.desc}
        Course Duration: ${this.course.duration}
        Course Price: ${this.course.price}
        Course Instructor: ${this.course.instructor}
      `;

      const payload = {
        course_id: this.course.id.toString(), 
        context: context.trim() 
      };
      axios.post('http://localhost:80/api/v1/course_summaries', payload)
        .then((response) => {
          this.summary = response.data;
        })
        .catch(error => {
          console.error('Error summarizing course:', error);
        });
    },
    takePrerequisiteTest() {
      const context = `
        name: ${this.course.name}, 
        short_description: ${this.course.short_desc}, 
        duration: ${this.course.duration} weeks, 
        price: $${this.course.price}, 
        instructor: ${this.course.instructor}, 
        topics: ${Array.isArray(this.course.topics) ? this.course.topics.join(', ') : 'No specific topics provided'}
      `;

      const payload = {
        course_id: this.course.id.toString(),
        context: context.trim(),
      };

      axios.post('http://localhost:80/api/v1/prerequisite_assessment', payload)
        .then((response) => {
          const questions = this.parseQuestions(response.data.assessment);
          this.generatePrerequisiteTest(questions);
        })
        .catch(error => {
          console.error('Error generating prerequisite test:', error);
        });
    },
    
    parseQuestions(assessmentText) {
      console.log(assessmentText);
      const questions = assessmentText.match(/\d+\.\s.+/g).map(question => question.replace(/^\d+\.\s/, ''));
      return questions;
    },

    generatePrerequisiteTest(questions) {
      const formHtml = `
        <form id="prerequisiteTestForm">
          <h3>Prerequisite Test</h3>
          ${questions.map((question, index) => `
            <div>
              <label>${index + 1}. ${question}</label>
              <div>
                <input type="radio" id="yes${index}" name="question${index + 1}" value="yes" required>
                <label for="yes${index}">Yes</label>
                <input type="radio" id="no${index}" name="question${index + 1}" value="no" required>
                <label for="no${index}">No</label>
              </div>
            </div>
          `).join('')}
          <button type="submit">Submit</button>
        </form>
      `;

      document.querySelector('.course-details').insertAdjacentHTML('beforeend', formHtml);

      document.getElementById('prerequisiteTestForm').addEventListener('submit', this.submitPrerequisiteTest);
    },

    submitPrerequisiteTest(event) {
      event.preventDefault(); 

      const formData = new FormData(event.target);
      const answers = [];

      for (let [key, value] of formData.entries()) {
        answers.push(value);
      }

      const allYes = answers.every(answer => answer === "yes");

      this.testPassed = allYes;  // Update testPassed based on results
      this.prerequisiteTestCompleted = true;  // Mark test as completed

      if (allYes) {
        alert('You are eligible to take this course!');
      } else {
        alert('You do not meet the prerequisites for this course.');
      }

      event.target.remove();
    },
    registerCourse() {
      alert('Registered successfully!');
      this.$router.push("/coursedashboard");
    },
    likeCourse() {
      alert('Liked successfully! (Dummy)');
    },
    shareCourse() {
      alert('Course shared successfully! (Dummy)');
    },
    toggleChatBot() {
      this.showChatBot = !this.showChatBot;
      if (this.showChatBot && this.$refs.chatbot) {
        this.$nextTick(() => {
          this.$refs.chatbot.$el.scrollIntoView({ behavior: 'smooth' });
        });
      }
    },
  },
  created() {
    this.cid = sessionStorage.getItem("cid");
    if (this.cid) {
      this.fetchCourseDetails();
    }
  }
};
</script>


<style scoped>
/* .course-details {
  font-family: 'Arial', sans-serif;
  margin: 20px;
  padding: 20px;
  background-color: #f7f9fc;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
} */

.course-details {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin: 20px;
  padding: 25px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

h1, h2 {
  color: #2d3436;
  margin-bottom: 10px;
  font-weight: 700;
}

h3 {
  color: #636e72;
  margin-top: 20px;
  margin-bottom: 15px;
  font-weight: 600;
}

p {
  color: #636e72;
  line-height: 1.8;
  font-size: 1rem;
  margin-bottom: 15px;
}

.instructor-info {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.instructor-info h3 {
  margin: 0;
  font-weight: 600;
}

ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

li {
  background-color: #dfe6e9;
  margin: 5px 0;
  padding: 12px 15px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  font-size: 1rem;
}

.actions {
  display: flex;
  gap: 15px;
  margin-top: 20px;
}

.actions button {
  padding: 10px 25px;
  background-color: #4b5a96;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.actions button:hover {
  background-color: #4b5a96;
  transform: translateY(-2px);
}

.icons {
  display: flex;
  align-items: center;
  margin-top: 20px;
}

.icons i {
  font-size: 28px;
  cursor: pointer;
  margin-right: 15px;
  color: #0984e3;
  transition: color 0.3s ease, transform 0.2s ease;
}

.icons i:hover {
  color: #74b9ff;
  transform: translateY(-2px);
}

.reviews {
  margin-top: 20px;
}

.review {
  background-color: #dfe6e9;
  padding: 12px 15px;
  border-radius: 5px;
  margin-bottom: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

button.toggle-weeks {
  background: none;
  border: none;
  color: #4b5a96;
  cursor: pointer;
  margin-top: 10px;
  padding: 0;
  font-size: 1rem;
  font-weight: 600;
  transition: color 0.3s ease;
}

button.toggle-weeks:hover {
  color: #8096eb;
  text-decoration: underline;
}

.register-button {
  padding: 10px 25px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.register-button.gray {
  background-color: #b2bec3;
  color: #fff;
}

.register-button.green {
  background-color: #00b894;
  color: #fff;
}

.register-button.red {
  background-color: #d63031;
  color: #fff;
}

.register-button:disabled {
  cursor: not-allowed;
}

.register-button:hover:enabled {
  transform: translateY(-2px);
}

.chatbot-toggle {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background-color: #6c5ce7;
  color: #fff;
  border: none;
  font-size: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.chatbot-toggle:hover {
  background-color: #a29bfe;
  transform: translateY(-2px);
}

</style>
