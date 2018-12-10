<template>
    <div>
        <h1>Game</h1>
        {{round}}/{{phase}}
        {{startPlayerName}}
        {{activePlayerName}}
                <select-player></select-player>
                <hr>
        <div class="row">
            <div class="col-12 col-sm-6">
                <end-of-game v-if="gameStateLoaded && gameEnded"></end-of-game>
                <action-box v-if="gameStateLoaded && !gameEnded"></action-box>
            </div>
            <div class="col-12 col-sm-6">
                <log></log>
            </div>
        </div>
        <div class="row">
            <div class="col-12 col-sm-6">
                <luxury-tiles v-if="gameStateLoaded"></luxury-tiles>
                <industry-tiles v-if="gameStateLoaded"></industry-tiles>
                <funding-board v-if="gameStateLoaded"></funding-board>
                <discard-pile v-if="gameStateLoaded"></discard-pile>
            </div>
            <div class="col-12 col-sm-offset-1 col-sm-5">
                <player v-if="gameStateLoaded" v-for="plr in players" :player="plr"></player>
            </div>
        </div>
        <div class="row">
            <div class="col-12 col-sm-6">
                <deck v-if="gameStateLoaded"></deck>
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
