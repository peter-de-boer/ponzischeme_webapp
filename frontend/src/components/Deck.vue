<template>
    <div>
        <h2>Deck</h2>
        <div class="row" v-for="card in fundDeck">
            <div class="col-xs-4">
                <fund-card :card="card"></fund-card>
            </div>
            
        </div>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';
    import FundCard from './FundCard.vue';

    export default {
        components: {
            FundCard
        },
        computed: {
            ...mapGetters([
                'fundingBoard',
                'gameStateLoaded',
                'fundDeck'
            ])    
        }
    }    
</script>

<style scoped>
</style>
