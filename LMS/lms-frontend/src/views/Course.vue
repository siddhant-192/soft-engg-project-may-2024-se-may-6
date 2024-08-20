<template>
  <div class="example-component">
    <CourseDetails />
  </div>
</template>

<script>
import CourseDetails from '../components/CourseDetails.vue';
export default {
    name: 'Course',
    data() {
        return {
            message: sessionStorage.getItem("cid")
        };
    },
    methods: {
        handleClick() {
            this.$router.push({ path: "/" });
        }
    },
    components: { CourseDetails }
};
</script>