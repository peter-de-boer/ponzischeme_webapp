<template>
	<div class="container">
        <div class="row">
            <div class="col-xs-12">
                <app-header></app-header>
            </div>
        </div>
        <router-view></router-view>
	</div>
</template>

<script>
    //import Header from './components/Header.vue'
    import Header from './components/header/header.vue'
    import { mapActions } from 'vuex';

    export default {
        components: {
            appHeader: Header
        },
        methods: {
            ...mapActions([
                'tryAutoLogin'
            ]),
        },
        mounted() {
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

</style>
