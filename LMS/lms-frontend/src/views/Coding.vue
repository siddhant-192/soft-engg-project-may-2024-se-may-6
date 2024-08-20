<template>
    <div class="example-component">
      <h1>{{ message }}</h1>
      <button @click="handleClick">Click Me</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ExampleComponent',
    data() {
      return {
        message: 'Hello, Vue!'
      };
    },
    methods: {
      handleClick() {
        this.message = 'Button Clicked!';
      }
    }
  };
  </script>