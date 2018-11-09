<template>
    <div class="container">
        <h1>Game</h1>
        <div class="row">
                <select-player></select-player>
                <hr>
        </div>
        <div class="row">
            <div class="col-sm-5">
                <funding-board v-if="gameStateLoaded"></funding-board>
                <deck v-if="gameStateLoaded"></deck>
            </div>
            <div class="col-sm-7">
                <player v-for="plr in players" :player="plr"></player>
            </div>
        </div>
    </div>
</template>

<script>
    import SelectPlayer from './SelectPlayer.vue';
    import axios from 'axios';
    import Board from './FundingBoard.vue';
    import Deck from './Deck.vue';
    import Player from './Player.vue';
    import {mapActions} from 'vuex';
    import {mapGetters} from 'vuex';

    export default {
        name: 'Game',
        created() {
            axios.get('/game')
                .then( res => {
                    console.log(res)
                    this.setGameState(res.data)
                }, error => {
                    console.log(error)
                }); 
        },
        components: {
            selectPlayer: SelectPlayer,
            fundingBoard: Board,
            deck: Deck,
            player: Player
        },
        computed: {
            ...mapGetters([
                'fundingBoard',
                'gameStateLoaded',
                'players'
            ])    
        },
        methods: {
            ...mapActions([
                'setGameState'
            ])    
        }


    }
</script>

<style scoped>
</style>
