<template>
    <div>
        <h1>Game {{id}}</h1>
        <button @click="getGame()"> Refresh </button> 
        <div class="row">
            <div class="col-12 col-sm-6">
                <log v-if="gameStateLoaded"></log>
            </div>
            <div class="col-12 col-sm-6">
                <chat v-if="gameStateLoaded"></chat>
            </div>
        </div>
        <div class="row">
            <div class="col-12 col-sm-4">
                <luxury-tiles v-if="gameStateLoaded && advanced"></luxury-tiles>
                <industry-tiles v-if="gameStateLoaded"></industry-tiles>
                <funding-board v-if="gameStateLoaded"></funding-board>
                <!-- <discard-pile v-if="gameStateLoaded"></discard-pile> -->
                <end-of-game v-if="gameStateLoaded && gameEnded"></end-of-game>
                <action-box v-if="gameStateLoaded && !gameEnded"></action-box>
            </div>
            <div class="col-12 col-sm-8">
                <player 
                    v-if="gameStateLoaded" 
                    v-for="plr in players" 
                    :player="plr"
                    :key="plr.id"
                >
                </player>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <notes v-if="userIsPlayer"></notes>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <finance v-if="gameStateLoaded && finance"></finance>
            </div>
        </div>
        <div class="row">
            <div class="col-12 col-sm-4">
                <!-- <deck v-if="gameStateLoaded"></deck> -->
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
    import Chat from './Chat.vue';
    import Notes from './Notes.vue';
    import Finance from './Finance.vue';
    import {mapActions} from 'vuex';
    import {mapGetters} from 'vuex';

    export default {
        name: 'Game',
        props: ['id'],
        created() {
            this.getGame()
        },
        components: {
            log: Log,
            chat: Chat,
            notes: Notes,
            finance: Finance,
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
                'fundingBoard',
                'advanced',
                'gameEnded',
                'gameStateLoaded',
                'players',
                'userIsPlayer',
                'finance'
            ])    
        },
        methods: {
            ...mapActions([
                'setGameState',
                'loadingOn',
                'loadingOff'
            ]),
            getGame() {
                var json = {"token": this.token, "id": this.id}
                this.loadingOn()
                // need to do put instead of get request, else json arg is not working somehow
                // ...solved, need params, but let's keep it as it is for now
                axios.put('/game', json)
                    .then( res => {
                        this.setGameState(res.data)
                    })
                    .catch(error => {
                        console.log(error)
                    })
                    .then(() => {
                        this.loadingOff()
                    }); 
            }
        }


    }
</script>

<style scoped>
</style>
