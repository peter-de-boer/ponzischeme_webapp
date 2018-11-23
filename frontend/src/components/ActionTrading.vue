<template>
    <div>
        <action-respond-to-trade-offer v-if="tradeOffer"></action-respond-to-trade-offer>
        <action-offer-trade v-else></action-offer-trade>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import ActionOfferTrade from './ActionOfferTrade.vue';
    import ActionRespondToTradeOffer from './ActionRespondToTradeOffer.vue';
    export default {
        computed: {
            ...mapGetters([
                'tradeOffer'
            ])    
        },
        components: {
            actionOfferTrade: ActionOfferTrade,
            actionRespondToTradeOffer: ActionRespondToTradeOffer
        }
    }    
</script>

<style scoped>

</style>
