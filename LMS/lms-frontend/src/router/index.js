import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Course from '../views/Course.vue'
import Coursework from '../views/Coursework.vue'
import Forum from '../views/Forum.vue'
import Coding from '../views/Coding.vue'
import Learn from '../views/Learn.vue'
import CourseDashboard from '../views/CourseDashboard.vue'
import CodeEditor from '../components/CodeEditor.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/course',
      name: 'course',
      component: Course
    },
    {
      path: '/forum',
      name: 'forum',
      component: Forum
    },
    {
      path: '/coursework',
      name: 'coursework',
      component: Coursework
    },
    {
      path: '/coding',
      name: 'coding',
      component: CodeEditor
    },
    {
      path: '/learn',
      name: 'learn',
      component: Learn
    },
    {
      path: '/coursedashboard',
      name: 'coursedashboard',
      component: CourseDashboard
    },
  ]
})

export default router
