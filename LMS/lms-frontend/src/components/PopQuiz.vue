<template>
    <div class="pop-quiz">
      <h2>Pre-registration Test</h2>
      <div v-for="question in questions" :key="question.id">
        <QuizQuestion :question="question" />
      </div>
      <button @click="submitQuiz">Submit</button>
    </div>
  </template>
  
  <script>
  import { mapGetters, mapActions } from 'vuex';
  import QuizQuestion from './QuizQuestion.vue';
  
  export default {
    components: {
      QuizQuestion,
    },
    computed: {
      ...mapGetters(['getQuestions']),
      questions() {
        return this.getQuestions;
      },
    },
    methods: {
      ...mapActions(['submitQuiz']),
    },
  };
  </script>
  
  <style scoped>
  .pop-quiz {
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
  }
  </style>
  