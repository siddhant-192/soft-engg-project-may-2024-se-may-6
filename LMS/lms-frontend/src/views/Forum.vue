<template>
  <div class="forum">
    <h1>Forum</h1>
    <div v-for="category in forumCategories" :key="category.id" class="category">
      <h2>{{ category.name }}</h2>
      <ul>
        <li v-for="thread in category.threads" :key="thread.id">
          <div class="thread">
            <h3>{{ thread.title }}</h3>
            <p>Started by {{ thread.author }} | {{ thread.date }}</p>
            <ul class="posts">
              <li v-for="post in thread.posts" :key="post.id">
                <div class="post">
                  <strong>{{ post.author }}:</strong>
                  <p>{{ post.content }}</p>
                  <small>{{ post.date }}</small>
                </div>
              </li>
            </ul>
          </div>
        </li>
      </ul>
    </div>
    <button class="chatbot-toggle" @click="toggleChatBot">
      🗨️
    </button>
    <ChatBot v-if="showChatBot " :courseId="0" />
  </div>
</template>

<script>
import ChatBot from "../components/ChatBot.vue";

export default {
  name: 'Forum',
  components: { ChatBot },
  data() {
    return {
      forumCategories: [
        {
          id: 1,
          name: 'General Discussion',
          threads: [
            {
              id: 1,
              title: 'Welcome to the Forum!',
              author: 'Admin',
              date: '2024-08-18',
              posts: [
                { id: 1, author: 'Admin', content: 'Feel free to introduce yourself!', date: '2024-08-18' },
                { id: 2, author: 'User123', content: 'Hi everyone! Excited to be here.', date: '2024-08-18' },
              ],
            },
            {
              id: 2,
              title: 'What are you working on?',
              author: 'User456',
              date: '2024-08-17',
              posts: [
                { id: 1, author: 'User456', content: 'Share your current projects!', date: '2024-08-17' },
                { id: 2, author: 'DevGuy', content: 'I\'m building a Vue.js app.', date: '2024-08-17' },
              ],
            },
          ],
        },
        {
          id: 2,
          name: 'Development',
          threads: [
            {
              id: 1,
              title: 'Vue.js Best Practices',
              author: 'DevExpert',
              date: '2024-08-16',
              posts: [
                { id: 1, author: 'DevExpert', content: 'Let\'s discuss the best practices for Vue.js development.', date: '2024-08-16' },
                { id: 2, author: 'CodeMaster', content: 'Always use components for reusability.', date: '2024-08-16' },
              ],
            },
          ],
        },
      ],
      showChatBot: false, 
    };
  },
  methods:{
    toggleChatBot() {
      this.showChatBot = !this.showChatBot;
      if (this.showChatBot && this.$refs.chatbot) {
        this.$nextTick(() => {
          this.$refs.chatbot.$el.scrollIntoView({ behavior: 'smooth' });
        });
      }
    },
  }
};
</script>

<style scoped>
.forum {
  padding: 20px;
}
.category {
  margin-bottom: 20px;
}
.thread {
  margin-bottom: 15px;
}
.post {
  margin-left: 20px;
  padding: 5px;
}

.chatbot-toggle {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background-color: #6c5ce7;
  color: #fff;
  border: none;
  font-size: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}
</style>
