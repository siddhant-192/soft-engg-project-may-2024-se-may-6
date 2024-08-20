<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav class="navbar">
      <ul class="navbar-list">
        <li class="navbar-item">
          <RouterLink to="/" class="navbar-link">Home</RouterLink>
        </li>
        <li class="navbar-item">
          <RouterLink to="/forum" class="navbar-link">Forum</RouterLink>
        </li>
        <li class="navbar-item">
          <RouterLink to="/coursework" class="navbar-link">Start Learning</RouterLink>
        </li>
      </ul>
    </nav>
    <RouterView />
  </header>
</template>

<style scoped>
.navbar {
  display: flex;
  background-color: #767697;
  padding: 10px;
}

.navbar-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
}

.navbar-item {
  margin-right: 15px;
}

.navbar-link {
  color: white;
  text-decoration: none;
  padding: 8px 16px;
  display: block;
}

.navbar-link:hover {
  background-color: #aab3d0;
}
</style>


<style scoped>

</style>

