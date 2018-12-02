<template>
    <div class="container">
        <h1>Game</h1>
        {{round}}/{{phase}}
        {{startPlayerName}}
        {{activePlayerName}}
        <div class="row">
                <select-player></select-player>
                <hr>
        </div>
        <div class="row">
            <div class="col-sm-6">
                <end-of-game v-if="gameStateLoaded && gameEnded"></end-of-game>
                <action-box v-if="gameStateLoaded && !gameEnded"></action-box>
                <luxury-tiles v-if="gameStateLoaded"></luxury-tiles>
                <industry-tiles v-if="gameStateLoaded"></industry-tiles>
                <funding-board v-if="gameStateLoaded"></funding-board>
                <discard-pile v-if="gameStateLoaded"></discard-pile>
                <deck v-if="gameStateLoaded"></deck>
            </div>
            <div class="col-sm-offset-1 col-sm-5">
                <player v-if="gameStateLoaded" v-for="plr in players" :player="plr"></player>
                <log></log>
            </div>
        </div>
    </div>
</template>

<script>
    import SelectPlayer from './SelectPlayer.vue';
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
            axios.get('/game')
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
            selectPlayer: SelectPlayer,
            fundingBoard: Board,
            deck: Deck,
            discardPile: DiscardPile,
            player: Player
        },
        computed: {
            ...mapGetters([
                'phase',
                'round',
                'startPlayerName',
                'activePlayerName',
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
