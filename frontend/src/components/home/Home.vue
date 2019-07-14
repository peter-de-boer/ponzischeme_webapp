<template>
    <div>
        <hr>
        <main-chat></main-chat>
        <hr>
        <div v-if="isAuthenticated">
            <create-game></create-game>
            <hr>
        </div>
        <new-games></new-games>
        <hr>
        <running-games></running-games>
        <hr>
        <finished-games></finished-games>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import { mapActions } from 'vuex';
    import MainChat from './MainChat.vue';
    import CreateGame from './CreateGame.vue';
    import NewGames from './NewGames.vue';
    import RunningGames from './RunningGames.vue';
    import FinishedGames from './FinishedGames.vue';

    export default {
        name: 'Home',
        created() {
            var json = {"token": this.token}
            this.doListAction({route: '/gameList', json})
        },
        computed: {
            ...mapGetters([
                'isAuthenticated',
                'token'
            ]),   
        },
        methods: {
            ...mapActions([
                'doListAction'
            ]),   
        },
        components: {
            mainChat: MainChat,
            createGame: CreateGame,
            runningGames: RunningGames,
            finishedGames: FinishedGames,
            newGames: NewGames
        }
    }
</script>

<style scoped>
</style>
