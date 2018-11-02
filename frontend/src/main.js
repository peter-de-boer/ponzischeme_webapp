import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import { routes } from './routes'
import axios from 'axios'

import { store } from './store/store.js';

Vue.use(VueRouter)

const router = new VueRouter({
    routes,
    mode: 'history'
})

Vue.config.productionTip = false

axios.defaults.baseURL = 'http://127.0.0.1:5000/'


new Vue({
    store,
    router,
    render: h => h(App)
}).$mount('#app')
