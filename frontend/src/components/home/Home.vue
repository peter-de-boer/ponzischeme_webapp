<template>
    <div>
        <li class="nav-item mx-2"><router-link to="/urlgame">Game</router-link></li>
        <hr>
        <create-game v-if="isAuthenticated"></create-game>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import CreateGame from './CreateGame.vue';

    export default {
        name: 'Home',
        computed: {
            ...mapGetters([
                'isAuthenticated'
            ]),   
        },
        components: {
            createGame: CreateGame
        }
    }
</script>

<style scoped>
</style>
