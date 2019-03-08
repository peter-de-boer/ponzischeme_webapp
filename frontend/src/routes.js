import Vue from 'vue'
import VueRouter from 'vue-router'

//need to import store
import { store } from './store/store.js';

import Game from './components/game/Game.vue'
import Home from './components/home/Home.vue'
import NotFound from './components/NotFound.vue'
import DashboardPage from './components/dashboard/dashboard.vue'
import SignupPage from './components/auth/signup.vue'
import SigninPage from './components/auth/login.vue'
import ConfirmPage from './components/auth/confirm.vue'

Vue.use(VueRouter)

const routes = [
    { path: '', name: 'home', component:  Home },
    //{ path: '/urlgame', component:  Game },
    { path: '/game/:id', name:'game', component:  Game, props: true },
    { path: '/signup', component: SignupPage },
    { path: '/confirm/:token', name:'confirm', component:  ConfirmPage, props: true },
    { path: '/login', name: 'login', component: SigninPage },
    {
      path: '/dashboard',
      component: DashboardPage,
      beforeEnter (to, from, next) {
        if (store.state.auth.idToken) {
          next()
        } else {
          next('/login')
        }
      }
    },
    { path: '*', component: NotFound }
]

export default new VueRouter({mode: 'history', routes})

