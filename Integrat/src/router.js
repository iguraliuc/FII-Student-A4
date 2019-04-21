import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home.vue'
import Orar from '@/views/Orar.vue'
import Boarduri from '@/views/Boarduri.vue'
import ContulMeu from '@/views/ContulMeu.vue'
import Prezentare from '@/views/Prezentare.vue'
import Login from "@/views/Login.vue"
import Register from "@/views/Register.vue"
import ForgotPassword from "@/views/ForgotPassword.vue"
import NewsIndividual from "@/components/news/NewsIndividual.vue"

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/home',
      name: 'home',
      component: Home
    },
    {
      path: '/orar',
      name: 'orar',
      component: Orar
    }, {
      path: '/boarduri',
      name: 'boarduri',
      component: Boarduri
    },
    {
      path: '/contul-meu',
      name: 'contul-meu',
      component: ContulMeu
    }, {
      path: '/prezentare',
      name: 'prezentare',
      component: Prezentare
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/forgot-password',
      name: 'forgot-password',
      component: ForgotPassword
    },
    {
      path: '/news',
      name: 'NewsIndividual',
      component: NewsIndividual
    },
  ]
})
