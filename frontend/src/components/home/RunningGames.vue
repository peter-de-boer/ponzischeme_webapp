<template>
    <div>
        Running Games <br>
        <div v-for="(game, index) in runningGames" :key="index">
            <running-game :game="game"></running-game>
        </div>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import RunningGame from './RunningGame.vue';

    export default {
        computed: {
            ...mapGetters([
                'runningGames'
            ])    
        },
        components: {
            runningGame: RunningGame
        }
    }    
</script>

<style scoped>
</style>
