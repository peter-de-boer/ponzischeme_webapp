<template>
	<div class="container">
        <div class="row">
            <div class="col-12">
                <app-header></app-header>
            </div>
        </div>
                <router-view></router-view>
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
