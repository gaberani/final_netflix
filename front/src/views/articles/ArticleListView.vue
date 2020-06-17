<template>
  <div class="row">
    <div class="col-sm-0 col-lg-2"></div>
    <div class="col-sm-12 col-lg-8">
      <h1 class="text-dark mt-3">게시판</h1>
      <table class="table table-strpied">
        <thead>
          <tr>
            <th class="text-dark" scope="col">글 번호</th>
            <th class="text-dark" scope="col">제목</th>
            <th class="text-dark" scope="col">쟉성자</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="article in articles" :key="`article_${article.id}`">
            <th scope="row" class="text-dark">{{ article.id }}</th>
            <td @click="detailarticle(article)" class="text-dark">{{article.title}}</td>
            <td class="text-dark">{{article.user.username}}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="col-sm-0 col-lg-2"></div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'


export default {
  name: 'ArticleListView',
  data(){
    return{
      articles:[],
      articleData:{},
      // articleNumCount: 0,
    }
  },
  methods:{
    detailarticle(one){
      axios.get(SERVER_URL + `/articles/${one.id}/`)
        .then(() => {
          this.$router.push({name:'ArticleDetail', params: {articleData: one}})
        })
        .catch(err => console.log(err.response))
    },
    ShowArticles(){
      axios.get(SERVER_URL+'/articles/')
        .then(res=>this.articles=res.data)
        .catch(err=>console.log(err.response))
    }
  },
  created(){
    this.ShowArticles()
  }
}
</script>

<style></style>