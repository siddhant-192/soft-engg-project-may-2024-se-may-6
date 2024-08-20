<template>
    <div class="course-dashboard">
      <header class="dashboard-header">
        <h1>{{ course.name }} Dashboard</h1>
        <p>{{ course.short_desc }}</p>
      </header>
  
      <section class="course-content">
        <h2>Course Content</h2>
        <div class="content">
          <div class="video-section">
            <h3>Videos</h3>
            <div v-for="(video, index) in course.videos" :key="index" class="video">
              <h4>{{ video.title }}</h4>
              <video controls :src="video.url" class="video-player">
                Your browser does not support the video tag.
              </video>
            </div>
          </div>
  
          <div class="text-content">
            <h3>Course Materials</h3>
            <p>{{ course.materials }}</p>
          </div>
        </div>
      </section>
  
      <section class="additional-resources">
        <h2>Additional Resources</h2>
        <ul>
          <li v-for="(resource, index) in course.resources" :key="index">
            <a :href="resource.url" target="_blank">{{ resource.title }}</a>
          </li>
        </ul>
      </section>
  
      <section class="assignments">
        <h2>Assignments</h2>
        <div v-for="(assignment, index) in course.assignments" :key="index" class="assignment">
          <h3>{{ assignment.title }}</h3>
          <p>{{ assignment.description }}</p>
          <p><strong>Due Date:</strong> {{ assignment.dueDate }}</p>
        </div>
      </section>
      <div class="actions">
        <button style="margin-bottom: 50px;" class="btn btn-primary " @click="codeEditor"> Open Code Editor </button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'CourseDashboard',
    data() {
      return {
        course: {
          name: 'Introduction to Vue.js',
          short_desc: 'Learn the fundamentals of Vue.js with hands-on examples.',
          videos: [
            { title: 'Getting Started with Vue.js', url: 'https://www.youtube.com/watch?v=ZtFjx3-gRkY' },
            { title: 'Vue.js Components', url: 'https://youtu.be/bSqRlNBzwfs' },
          ],
          materials: 'In this course, you will learn about Vue.js components, directives, and state management.',
          resources: [
            { title: 'Vue.js Official Documentation', url: 'https://vuejs.org' },
            { title: 'Vue Mastery - Vue.js Courses', url: 'https://www.vuemastery.com' },
          ],
          assignments: [
            { title: 'Create a Vue.js Component', description: 'Build a basic Vue.js component and display it on a web page.', dueDate: '2024-08-31' },
            { title: 'Vue.js State Management Exercise', description: 'Implement state management in a Vue.js application using Vuex.', dueDate: '2024-09-15' },
          ],
        },
      };
    },
    methods:{
      codeEditor(){
        this.$router.push("/coding");
      }
    }
  };
  </script>
  
  <style scoped>
  /* .course-dashboard {
    font-family: Arial, sans-serif;
    background-color: #f7f9fc;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  } */
  
  .dashboard-header {
    margin-bottom: 20px;
  }
  
  h1 {
    color: #2c3e50;
  }
  
  h2 {
    color: #34495e;
    margin-top: 20px;
    margin-bottom: 10px;
  }
  
  h3 {
    color: #2c3e50;
    margin-bottom: 10px;
  }
  
  .video-section,
  .text-content,
  .additional-resources,
  .assignments {
    margin-bottom: 20px;
  }
  
  .video {
    margin-bottom: 15px;
  }
  
  .video-player {
    width: 100%;
    max-width: 600px;
    height: auto;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    margin-bottom: 10px;
  }
  
  li a {
    color: #3498db;
    text-decoration: none;
  }
  
  li a:hover {
    text-decoration: underline;
  }
  
  .assignment {
    background-color: #ecf0f1;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 10px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
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
  </style>
  