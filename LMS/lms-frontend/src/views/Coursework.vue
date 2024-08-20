<template>
    <div class="container">
      <h1 class="heading">Registered Courses</h1>
      <div class="course-list">
        <div @click="openCourse(course)" class="course-card" v-for="course in courses" :key="course.id">
          <h2>{{ course }}</h2>
          <p><strong>Instructor:</strong> {{ course }}</p>
          <p><strong>Description:</strong> {{ course }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
  name: 'Coursework',
  data() {
    return {
      courses: [],
      sid: null,
    };
  },
  methods: {
    fetchCourses() {
        const res = fetch("http://127.0.0.1:8080/api/student/course/"+this.sid.toString(),
        {
        method: "GET",
        headers:{"Content-Type":"application/json"},
        }
        );  
        this.courses = [];
        res
        .then((response) => response.json())
        .then((data) => {
          if (data["status"] == "success") {
            for (const i of data["data"]) {
              this.courses.push(i);
            }
          } 
        });
    },
    openCourse(cid) {
      sessionStorage.setItem("cid", cid);
      this.$router.push({path: "/learn"});
    }
    },    
  created: function() {
    this.sid = sessionStorage.getItem("sid");
    this.fetchCourses();
  },
  };
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
