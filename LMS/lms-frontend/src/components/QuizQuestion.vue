<template>
    <div class="quiz-question">
      <p>{{ question.text }}</p>
      <div v-for="(option, index) in question.options" :key="index">
        <label>
          <input
            type="radio"
            :name="`question-${question.id}`"
            :value="index"
            @change="selectAnswer(index)"
          />
          {{ option }}
        </label>
      </div>
    </div>
  </template>
  
  <script>
  import { mapMutations } from 'vuex';
  
  export default {
    props: {
      question: Object,
    },
    methods: {
      ...mapMutations(['setAnswer']),
      selectAnswer(index) {
        this.setAnswer({ questionId: this.question.id, answerIndex: index });
      },
    },
  };
  </script>
  
  <style scoped>
  .quiz-question {
    margin-bottom: 20px;
  }
  </style>
  