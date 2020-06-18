<template>
  <div class="main-box">
    <h1 class="tit-main">오늘의 추천</h1>
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
  .main-box {
    padding-top:84px;
  }
  .tit-main {
    margin:60px 0 40px;
    font-weight:bold; color:#fff
  }
</style>