<template>
    <div>
        <h2>Funding Board</h2>
        <div class="row" v-for="i in 3" :key="i">
            <div class="col-xs-2 col-md-1" 
                v-for="j in 3" 
                :key=j
                @click="selectCard(fundingBoard[3*(i-1)+j-1].value)">
                    <fund-card :card="fundingBoard[3*(i-1)+j-1]" ></fund-card>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import {mapGetters} from 'vuex';
    import {mapActions} from 'vuex';
    import FundCard from './FundCard.vue';

    export default {
        components: {
            FundCard
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
            ]),    
            selectCard(value) {
                console.log("in selectcard")
                var json = {"value": value}
                axios.put('/game/selectCard', json)
                    .then( res => {
                        console.log(res)
                        this.setGameState(res.data)
                }, error => {
                    console.log(error)
                }); 
            }
        }
    }    
</script>

<style scoped>
</style>
