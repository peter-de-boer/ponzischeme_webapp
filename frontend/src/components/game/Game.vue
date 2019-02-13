<template>
    <div>
        <h1>Game</h1>
        {{round}}/{{phase}}
        {{startPlayerName}}
        {{activePlayer ? activePlayer.name : ""}}
        <div class="row">
            <div class="col-12 col-sm-4">
                <end-of-game v-if="gameStateLoaded && gameEnded"></end-of-game>
                <action-box v-if="gameStateLoaded && !gameEnded"></action-box>
            </div>
            <div class="col-12 col-sm-8">
                <log></log>
            </div>
        </div>
        <div class="row">
            <div class="col-12 col-sm-4">
                <luxury-tiles v-if="gameStateLoaded"></luxury-tiles>
                <industry-tiles v-if="gameStateLoaded"></industry-tiles>
                <funding-board v-if="gameStateLoaded"></funding-board>
                <discard-pile v-if="gameStateLoaded"></discard-pile>
            </div>
            <div class="col-12 col-sm-8">
                <player v-if="gameStateLoaded" v-for="plr in players" :player="plr"></player>
            </div>
        </div>
        <div class="row">
            <div class="col-12 col-sm-4">
                <deck v-if="gameStateLoaded"></deck>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import Board from './FundingBoard.vue';
    import Deck from './Deck.vue';
    import DiscardPile from './DiscardPile.vue';
    import Player from './Player.vue';
    import LuxuryTiles from './LuxuryTiles.vue';
    import IndustryTiles from './IndustryTiles.vue';
    import ActionBox from './ActionBox.vue';
    import EndOfGame from './EndOfGame.vue';
    import Log from './Log.vue';
    import {mapActions} from 'vuex';
    import {mapGetters} from 'vuex';

    export default {
        name: 'Game',
        created() {
            var json = {"token": this.token}
            console.log(json)
            // need to do put instead of get request, else json arg is not working somehow
            axios.put('/game', json)
                .then( res => {
                    console.log(res)
                    this.setGameState(res.data)
                }, error => {
                    console.log(error)
                }); 
        },
        components: {
            log: Log,
            endOfGame: EndOfGame,
            actionBox: ActionBox,
            luxuryTiles: LuxuryTiles,
            industryTiles: IndustryTiles,
            fundingBoard: Board,
            deck: Deck,
            discardPile: DiscardPile,
            player: Player
        },
        computed: {
            ...mapGetters([
                'token',
                'phase',
                'round',
                'startPlayerName',
                'activePlayer',
                'fundingBoard',
                'gameEnded',
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
