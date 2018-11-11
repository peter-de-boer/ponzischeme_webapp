<template>
    <div class="container">
        <h2>Funding Board</h2>
        <div class="row small-gutter" v-for="i in 3" :key="i">
            <div class="col-sm-2" v-for="j in 3" :key=j>
                <fund-card :card="fundingBoard[3*(i-1)+j-1]" ></fund-card>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';
    import {mapActions} from 'vuex';
    import FundCard from './FundCard.vue';

    export default {
        components: {
            FundCard
        },
        computed: {
            ...mapGetters([
                'currentPlayer',
                'fundingBoard',
                'gameStateLoaded'
            ])    
        },
        methods: {
            ...mapActions([
                'setGameState',
                'selectFundCard'
            ])    
        }
    }    
</script>

<style scoped>
.small-gutter > [class*='col-'] {
    padding-right:2px;
    padding-left:2px;
}
</style>
