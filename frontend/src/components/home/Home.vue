<template>
    <div>
        <create-game v-if="isAuthenticated"></create-game>
        <hr>
        <new-games></new-games>
        <hr>
        <running-games></running-games>
        <hr>
        <finished-games></finished-games>
    </div>
</template>

<script>
    import axios from 'axios';
    import { mapGetters } from 'vuex';
    import { mapActions } from 'vuex';
    import CreateGame from './CreateGame.vue';
    import NewGames from './NewGames.vue';
    import RunningGames from './RunningGames.vue';
    import FinishedGames from './FinishedGames.vue';

    export default {
        name: 'Home',
        created() {
            console.log("Home created()")
            var json = {"token": this.token}
            console.log(json)
            axios.put('/gameList', json)
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
                'token',
                'tokenStorage'
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
            finishedGames: FinishedGames,
            newGames: NewGames
        }
    }
</script>

<style scoped>
</style>
