<template>
    <div class="quiz-result" v-if="results">
      <h2>Pre-Registration Test Details</h2>
      <div>
        <p>Score: {{ (results.score * 100).toFixed(2) }}%</p>
        <p>Total Questions: {{ results.totalQuestions }}</p>
      </div>
      <div class="analysis">
        <!-- Placeholder for graph or chart -->
        <p>Areas of Knowledge</p>
        <p>Areas of Improvement</p>
      </div>
      <button @click="resetQuiz">Retry</button>
      <button @click="register">Register</button>
    </div>
  </template>
  
  <script>
  import { mapGetters, mapActions } from 'vuex';
  
  export default {
    computed: {
      ...mapGetters(['getResults']),
      results() {
        return this.getResults;
      },
    },
    methods: {
      ...mapActions(['resetQuiz']),
      register() {
        alert('Proceed to registration...');
      },
    },
  };
  </script>
  
  <style scoped>
  .quiz-result {
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
  }
  .analysis {
    margin-top: 20px;
  }
  </style>
  