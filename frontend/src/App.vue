<template>
  <div>
    <div class="overlay" v-if="loading">
        <!-- img is generated on ajaxloader.info: 
            arrows, background #E2F7F4, foreground 000000
        -->>
        <img src="./assets/ajax-loader.gif" class="centered">
    </div>
	<div class="container">
        <div class="row">
            <div class="col-xs-12">
                <app-header></app-header>
            </div>
        </div>
        <router-view></router-view>
	</div>
  </div>
</template>

<script>
    //import Header from './components/Header.vue'
    import Header from './components/header/header.vue'
    import { mapActions } from 'vuex';
    import { mapGetters } from 'vuex';

    export default {
        components: {
            appHeader: Header
        },
        methods: {
            ...mapActions([
                'tryAutoLogin'
            ]),
        },
        computed: {
            ...mapGetters([
                'loading'
            ]),
        },
        created() {
            this.tryAutoLogin()
        }
    }
</script>

<style>

body {
font-family: -apple-system, BlinkMacSystemFont, “Segoe UI”, Roboto, “Helvetica Neue”, Arial, sans-serif, “Apple Color Emoji”, “Segoe UI Emoji”, “Segoe UI Symbol”;
/* default is 1rem or 16px */
font-size: 14px;
font-weight: 400;
line-height: 1.3;
background-color: #E2F7F4;
}

/* Increase all font sizes on mobile */
@media (max-width: 767px) {

body {
/* default is 1rem or 16px */
font-size: 14px;
}

}

.overlay {
  position: fixed;
  display: block;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0,0,0,0.5);
  z-index: 10;
}

.centered {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

</style>
