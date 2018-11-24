<template>
    <div class="action">
        <h2>Trading</h2>
        <p>Please select an industry tile from and opponent and offer an amount of money, or pass</p>
        <p><button class="btn btn-default" 
                @click="offerTrade(selectedPlayerAndTile, tradeMoney)"> 
                    Offer Trade
           </button> 
             {{tradeMoney}} {{selectedPlayerAndTile.name}} {{selectedPlayerAndTile.tile}}</p>
        <button class="btn btn-default" @click="passTrading()"> Pass </button> 
        <hr>
        <vue-slider ref="slider" v-model="tradeMoney" v-bind="sliderOptions"></vue-slider>
        <input v-model="tradeMoney">
        <hr>
        <p><button class="btn btn-default" 
                   @click="buyLuxuryTile(selectedLuxuryTile)"> 
                   Buy Luxury Tile 
           </button> 
           {{selectedLuxuryTile}}
        </p>
    </div>
</template>

<script>
    import axios from 'axios';
    import { mapGetters } from 'vuex';
    import { mapActions } from 'vuex';
    import vueSlider from 'vue-slider-component';

    export default {
        components: {
            vueSlider
        },
        data() {
            return {
                tradeMoney: 1
            }
        },
        computed: {
            ...mapGetters([
                'currentPlayer',
                'selectedLuxuryTile',
                'selectedPlayerAndTile'
            ]),
            sliderOptions() {
                var max = 1
                if (this.currentPlayer) {
                    max = this.currentPlayer.money
                } 
                return {
                    min: 1,
                    max: max
                }
            }
        },
        methods: {
            ...mapActions([
                'setGameState'
            ]),
            buyLuxuryTile(tile) {
                console.log("in buyLuxuryTile")
                if (this.currentPlayer && tile!=null) {
                    var json = {"tile": tile, "name": this.currentPlayer.name}
                    console.log(json)
                    axios.put('/game/buyLuxuryTile', json)
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
            offerTrade(playerAndTile, money) {
                console.log("in offerTrade")
                if (this.currentPlayer && playerAndTile && money != null) {
                    var json = {"money": money, "tile": playerAndTile.tile, "opponentName": playerAndTile.name,
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
