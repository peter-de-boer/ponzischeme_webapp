<template>
    <div>
        Finished Games <br>
        <div v-for="(game, index) in finishedGames" :key="index">
            <finished-game :game="game"></finished-game>
        </div>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import FinishedGame from './FinishedGame.vue';

    export default {
        computed: {
            ...mapGetters([
                'finishedGames'
            ])    
        },
        components: {
            finishedGame: FinishedGame
        }
    }    
</script>

<style scoped>
</style>
