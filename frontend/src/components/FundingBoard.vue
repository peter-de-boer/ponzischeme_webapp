<template>
    <div>
        <h2>Funding Board</h2>
        <div class="row small-gutter" v-for="i in 3" :key="i">
            <div class="col-sm-4" v-for="j in 3" :key="j+3*i">
                <fund-card :card="fundingBoard[3*(i-1)+j-1]" 
                           @click.native="select(fundingBoard[3*(i-1)+j-1])">
                </fund-card>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';
    import {mapActions} from 'vuex';
    import FundCard from './FundCard.vue';

    export default {
        data() {
            return {
                card: {}
            }
        },
        components: {
            FundCard
        },
        computed: {
            ...mapGetters([
                'phase',
                'currentIsActive',
                'currentPlayer',
                'fundingBoard',
                'selectedFundCard',
                'gameStateLoaded'
            ])    
        },
        methods: {
            ...mapActions([
                'setGameState',
                'selectFundCard'
            ]),
            select(card) {
                if (this.currentIsActive && (this.phase==1 || this.phase ==3)) {
                    this.selectFundCard(card)
                }
            }
        }
    }    
</script>

<style scoped>
.small-gutter > [class*='col-'] {
    padding-right:2px;
    padding-left:2px;
    padding-top:4px;
}
</style>
