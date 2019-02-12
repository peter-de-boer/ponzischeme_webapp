import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import router from './routes'
import axios from 'axios'

import { store } from './store/store.js';

Vue.config.productionTip = false

//axios.defaults.baseURL = 'https://weisswurst.pythonanywhere.com/'


new Vue({
    store,
    router,
    render: h => h(App)
}).$mount('#app')
