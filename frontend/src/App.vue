<template>
	<div class="container">
        <div class="row">
            <div class="col-xs-12 cls-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
                <app-header></app-header>
                <router-view></router-view>
            </div>
        </div>
	</div>
</template>

<script>
    import Header from './components/Header.vue'

    export default {
        components: {
            appHeader: Header
        }
    }
</script>

<style>
</style>
