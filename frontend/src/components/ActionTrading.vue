<template>
    <div class="action">
        <h2>Trading</h2>
        <p>Please select an industry tile from and opponent and offer an amount of money, or pass</p>
        <p><button class="btn btn-default" 
                @click="offerTrade(selectedIndustryTile, selectedOpponentName, money)"> 
                    Offer Trade
           </button> 
             {{tradeMoney}} {{selectedIndustryTile}} {{selectedOpponentName}} </p>
        <button class="btn btn-default" @click="passTrading()"> Pass </button> 
    </div>
</template>

<script>
    import axios from 'axios';
    import { mapGetters } from 'vuex';
    import { mapActions } from 'vuex';

    export default {
        computed: {
            ...mapGetters([
                'currentPlayer',
                'selectedOpponentName',
                'selectedIndustryTile',
                'tradeMoney'
            ])    
        },
        methods: {
            ...mapActions([
                'setGameState'
            ]),
            offerTrade(tile, opponentName, money) {
                console.log("in offerTrade")
                if (this.currentPlayer && tile != null && money != null) {
                    var json = {"money": money, "tile": tile, "opponentName": opponentName,
                                "name": this.currentPlayer.name}
                    console.log(json)
                    axios.put('/game/offerTrade', json)
                        .then( res => {
                            console.log(res)
                            if (res.data.error) {
                                console.log(res.data.error)
                            } else {
                                this.setGameState(res.data)
                            }
                    }, error => {
                        console.log(error)
                    }); 
                }
            },
            passTrading() {
                console.log("in passTrade")
                if (this.currentPlayer) {
                    var json = {"name": this.currentPlayer.name}
                    axios.put('/game/passTrading', json)
                        .then( res => {
                            console.log(res)
                            if (res.data.error) {
                                console.log(res.data.error)
                            } else {
                                this.setGameState(res.data)
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
