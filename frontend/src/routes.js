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
import ResetPage from './components/auth/reset.vue'
import RequestResetPage from './components/auth/request_reset.vue'

Vue.use(VueRouter)

const routes = [
    { path: '', name: 'home', component:  Home },
    //{ path: '/urlgame', component:  Game },
    { path: '/game/:id', name:'game', component:  Game, props: true },
    { path: '/signup', component: SignupPage },
    { path: '/confirm/:token', name:'confirm', component:  ConfirmPage, props: true },
    { path: '/reset_password/:token', name:'reset_password', component:  ResetPage, props: true },
    { path: '/request_reset_password', name:'request_reset_password', component:  RequestResetPage },
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

