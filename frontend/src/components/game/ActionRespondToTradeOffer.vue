<template>
    <div>
        <h2>Trading</h2>
        <div v-if="userIsActive">
            <p> {{tradeOffer.offeringPlayerName}} offers 
                {{tradeOffer.tradeMoney}} to
                you for a 
                {{tradeOffer.tileName}} tile </p>
            <p>Please accept the trade offer (sell) or place an counter-offer (buy)</p>
            <p><button class="btn btn-default" @click="sellTrade()"> Sold! </button> </p>
            <p><button class="btn btn-default" 
                :class="enableButton()"
                @click="buyTrade()"> Counter Offer </button> </p>
        </div>
        <div v-else>
            <p> {{tradeOffer.offeringPlayerName}} offers 
                {{tradeOffer.tradeMoney}} to
                {{tradeOffer.opponentName}} for a 
                {{tradeOffer.tileName}} tile </p>
            <p>{{tradeOffer.opponentName}} must accept the trade offer (sell) or place an counter-offer (buy)</p>
        </div>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import { mapActions } from 'vuex';

    export default {
        computed: {
            ...mapGetters([
                'id',
                'activePlayer',
                'userIsActive',
                'token',
                'username',
                'tradeOffer'
            ])
        },
        methods: {
            ...mapActions([
                'doAction'
            ]),
            counterOfferPossible() {
                return (this.userIsActive && 
                        this.activePlayer.money >= this.tradeOffer.tradeMoney)
            },
            enableButton() {
                if (this.counterOfferPossible()) {
                    return ""
                } else {
                    return "disabled"
                }
            },
            sellTrade() {
                if (this.token) {
                    var json = {"token": this.token, "id": this.id}
                    this.doAction({route: '/game/sellTrade', json})
                }
            },
            buyTrade() {
                if (this.counterOfferPossible()) {
                    var json = {"token": this.token, "id": this.id}
                    this.doAction({route: '/game/buyTrade', json})
                }
            }
        }
    }
</script>

<style scoped>
</style>
