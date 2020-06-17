import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import LoginView from '@/views/accounts/LoginView.vue'
import SignupView from '@/views/accounts/SignupView.vue'

import MovieList from '@/views/movies/MovieList'
import MovieDetail from '@/views/movies/MovieDetail.vue'
import SearchListView from '@/views/movies/SearchListView.vue'
import MovieRecommend from '@/views/movies/MovieRecommend.vue'

import ArticleCreateView from '@/views/articles/ArticleCreateView.vue'
import ArticleListView from '@/views/articles/ArticleListView.vue'
import ArticleDetail from '@/views/articles/ArticleDetail.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path:'/accounts/login',
    name:'Login',
    component:LoginView

  },
  {
    path:'/accounts/signup',
    name:'Signup',
    component:SignupView
  },
  {
    path:'/movies/MovieList',
    name:'MovieList',
    component: MovieList
  },
  {
    path:'/movies/MovieDetail',
    name:'MovieDetail',
    component : MovieDetail
  },
  {
    path:'/articles/create',
    name:'Create',
    component:ArticleCreateView
  },
  {
    path:'/articles',
    name:'List',
    component:ArticleListView
  },
  {
    path:'/articles/ArticleDetail',
    name:'ArticleDetail',
    component : ArticleDetail
  },
  {
    path:'/movies/SearchList',
    name:'SearchList',
    component:SearchListView
  },
  {
    path:'/movies/MovieRecommend',
    name:'MovieRecommend',
    component:MovieRecommend
  },
]


const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router