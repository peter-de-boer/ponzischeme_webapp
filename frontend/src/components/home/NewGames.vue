<template>
    <div>
        New Games <br>
        <div class="row">
            <div class="col-xs-12 col-sm-6 col-md-3 col-lg-2 col-xl-2" 
                v-for="(game, index) in newGames" :key="index">
                    <new-game :game="game"></new-game>
            </div>
        </div>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import NewGame from './NewGame.vue';

    export default {
        computed: {
            ...mapGetters([
                'newGames'
            ])    
        },
        components: {
            newGame: NewGame
        }
    }    
</script>

<style scoped>
</style>
