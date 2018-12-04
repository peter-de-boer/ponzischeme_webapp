<template>
    <div class="action">
        <h2>Trading</h2>
        <div v-if="currentIsActive">
            <p> {{tradeOffer.offeringPlayerName}} offers 
                {{tradeOffer.tradeMoney}} to
                you for a 
                {{tradeOffer.tileName}} tile </p>
            <p>Please accept the trade offer (sell) or place an counter-offer (buy)</p>
            <p><button class="btn btn-default" @click="sellTrade()"> Sold! </button> </p>
            <p><button class="btn btn-default" @click="buyTrade()"> Counter Offer </button> </p>
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
    import axios from 'axios';
    import { mapGetters } from 'vuex';
    import { mapActions } from 'vuex';

    export default {
        computed: {
            ...mapGetters([
                'currentIsActive',
                'currentPlayer',
                'tradeOffer'
            ])
        },
        methods: {
            ...mapActions([
                'setGameState',
                'clearSelections'
            ]),
            sellTrade() {
                console.log("in sellTrade")
                if (this.currentPlayer) {
                    var json = {"name": this.currentPlayer.name}
                    axios.put('/game/sellTrade', json)
                        .then( res => {
                            console.log(res)
                            if (res.data.error) {
                                console.log(res.data.error)
                            } else {
                                this.setGameState(res.data)
                                //this.clearSelections()
                            }
                        }, error => {
                            console.log(error)
                        }
                    ); 
                }
            },
            buyTrade() {
                console.log("in buyTrade")
                if (this.currentPlayer) {
                    var json = {"name": this.currentPlayer.name}
                    axios.put('/game/buyTrade', json)
                        .then( res => {
                            console.log(res)
                            if (res.data.error) {
                                console.log(res.data.error)
                            } else {
                                this.setGameState(res.data)
                                //this.clearSelections()
                            }
                        }, error => {
                            console.log(error)
                        }
                    ); 
                }
            }
        }
    }
</script>

<style scoped>
.action {
  border-style: solid;
}
</style>
