<template>
    <div class="example-component">
      <h1>{{ message }}</h1>
      <p>video content here >>></p>
      <h2>transcripts here</h2>

      <button @click="handleClick">chat</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Learn',
    data() {
      return {
        message: sessionStorage.getItem("cid")
      };
    },
    methods: {
      handleClick() {
        this.$router.push({path: "/forum"});
      }
    }
  };
  </script>