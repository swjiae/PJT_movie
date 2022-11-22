import Vue from 'vue'
import VueRouter from 'vue-router'
import PreMainView from '@/views/PreMainView'
import MainView from '@/views/MainView'
import ProfileView from '@/views/ProfileView'
import MovieDetailView from '@/views/MovieDetailView'
import MovieReviewCreate from '@/components/MovieReviewCreate'

Vue.use(VueRouter)

const routes = [
  {
    path: '/premain',
    name: 'PreMainView',
    component: PreMainView
  },
  {
    path: '/main',
    name: 'MainView',
    component: MainView
  },
  {
    path: '/profile',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/:id',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/review/:id',
    name: 'MovieReviewCreate',
    component: MovieReviewCreate
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
