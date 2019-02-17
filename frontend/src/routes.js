import Vue from 'vue'
import VueRouter from 'vue-router'

import Game from './components/game/Game.vue'
import Home from './components/home/Home.vue'
import NotFound from './components/NotFound.vue'
import DashboardPage from './components/dashboard/dashboard.vue'
import SignupPage from './components/auth/signup.vue'
import SigninPage from './components/auth/login.vue'

Vue.use(VueRouter)

const routes = [
    { path: '', component:  Home },
    { path: '/urlgame', component:  Game },
    { path: '/signup', component: SignupPage },
    { path: '/login', name: 'login', component: SigninPage },
    {
      path: '/dashboard',
      component: DashboardPage,
      beforeEnter (to, from, next) {
        if (store.state.idToken) {
          next()
        } else {
          next('/login')
        }
      }
    },
    { path: '*', component: NotFound }
]

export default new VueRouter({mode: 'history', routes})

