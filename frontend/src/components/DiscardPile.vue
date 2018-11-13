<template>
    <div class="container">
        <h2>Discard Pile</h2>
        <div class="row" v-for="card in discardPile">
            <div class="col-xs-2">
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
                'gameStateLoaded',
                'discardPile'
            ])    
        }
    }    
</script>

<style scoped>
</style>
