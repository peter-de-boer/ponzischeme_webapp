<template>
    <div>
        <li class="nav-item mx-2"><router-link to="/urlgame">Game</router-link></li>
        <hr>
        <create-game v-if="isAuthenticated"></create-game>
        <hr>
        <new-games></new-games>
        <hr>
        <running-games></running-games>
    </div>
</template>

<script>
    import axios from 'axios';
    import { mapGetters } from 'vuex';
    import { mapActions } from 'vuex';
    import CreateGame from './CreateGame.vue';
    import NewGames from './NewGames.vue';
    import RunningGames from './RunningGames.vue';

    export default {
        name: 'Home',
        created() {
            axios.get('/gameList')
                .then( res => {
                    console.log(res)
                    this.setGameList(res.data)
                }, error => {
                    console.log(error)
                }); 
        },
        computed: {
            ...mapGetters([
                'isAuthenticated',
                'token'
            ]),   
        },
        methods: {
            ...mapActions([
                'setGameList'
            ]),   
        },
        components: {
            createGame: CreateGame,
            runningGames: RunningGames,
            newGames: NewGames
        }
    }
</script>

<style scoped>
</style>
