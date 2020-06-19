<template>
  <div class="main-box">
    <h1 class="tit-main">최근 많이 본 영화</h1>
      <MainView/>
      <br>
  </div>
</template>

<script>
import MainView from '@/views/movies/MainView.vue'

export default {
  name: 'Home',
  components: {
    MainView,
  },
}
</script>

<style>
  .tit-main {
    padding:20px 0 40px;
    font-weight:bold; color:#fff
  }
</style>