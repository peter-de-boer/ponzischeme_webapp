<template>
  <div>
    <h1>Game</h1>
    <funding-board v-if="gameStateLoaded"></funding-board>
    <deck v-if="gameStateLoaded"></deck>
  </div>
</template>

<script>
    import axios from 'axios';
    import Board from './FundingBoard.vue';
    import Deck from './Deck.vue';
    import {mapActions} from 'vuex';
    import {mapGetters} from 'vuex';

    export default {
        name: 'Game',
        created() {
            axios.get('/game')
                .then( res => {
                    this.setGameState(res.data)
                }, error => {
                    console.log(error)
                }); 
        },
        components: {
            fundingBoard: Board,
            deck: Deck
        },
        computed: {
            ...mapGetters([
                'fundingBoard',
                'gameStateLoaded'
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
