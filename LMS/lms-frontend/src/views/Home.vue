<template>
  <div class="container">
    <h1 class="heading">Courses</h1>
    <input class='text-box' type="text" v-model="filterText" placeholder="Filter courses..." />
    <div class="course-list">
      <div @click="openCourse(course.id)" class="course-card" v-for="course in filteredCourses" :key="course.id">
        <h2>{{ course.name }}</h2>
        <p><strong>Instructor:</strong> {{ course.instructor }}</p>
        <p><strong>Duration:</strong> {{ course.duration }}</p>
        <p><strong>Description:</strong> {{ course.desc }}</p>
      </div>
    </div>
    <!-- <ChatBot></ChatBot> -->
  </div>
  
</template>

<script>
import axios from 'axios';
import ChatBot from '../components/ChatBot.vue'

export default {
  name: 'Home',
  components: {
    ChatBot,
  },
  data() {
    return {
      courses: [],
      filterText: ''
    }
  },
  created() {
    this.fetchCourses()
    sessionStorage.setItem('sid', 2)    //hard coding student number "2"
  },
  methods: {
    // fetching courses from backend
    fetchCourses() {
      axios.get('http://localhost:8080/api/courses')
        .then(response => {
          this.courses = this.courses.concat(response.data.data);
        })
        .catch(error => {
          console.error('Error fetching courses:', error);
        });
    },
    openCourse(cid) {
      sessionStorage.setItem("cid", cid);
      this.$router.push({path: "/course"});
    }
    // fetch data with api
    // async fetchCourses(){
    //   try {const response = await fetch('https//:course_api')
    //   const data = response.json()
    //   this.courses = data
    //   }
    //   catch (error){
    //     console.log(error)
    //   }
    // }
  },
  computed: {
    filteredCourses() {
      const filter = this.filterText.toLowerCase();
      return this.courses.filter(course => 
        course.name.toLowerCase().includes(filter) ||
        course.instructor.toLowerCase().includes(filter) ||
        course.duration.toString().toLowerCase().includes(filter)
      );
    }
  }
}
</script>

<style scoped>

.container {
  text-align: center;
  padding: 20px;
  margin-bottom: 300px;
  margin-left: 100px
}

.heading {
  font-size: 2.5em;
  margin-top: 20px;
  color: #333;
}

.text-box{
  padding: 10px;
  font-size: 1em;
  width: 100%;
  max-width: 400px;
  margin: 20px auto;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
}

.text-box:focus {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  outline: none;
}

.course-list {
  display: flex;
  gap: 20px;
  margin-top: 20px;
  justify-content: center;
  overflow-x: auto; 
}

.course-card {
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  padding: 20px;
  width: 300px; 
  height: 250px; 
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background: linear-gradient(to right, #ffffff, #f8f8f8);
  text-align: left;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow: hidden; 
}

.course-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.course-card h2 {
  margin: 0 0 10px;
  font-size: 1.5em;
  color: #333;
}
</style>

