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

//axios.defaults.baseURL = 'https://weisswurst.pythonanywhere.com/'


new Vue({
    store,
    router,
    render: h => h(App)
}).$mount('#app')
