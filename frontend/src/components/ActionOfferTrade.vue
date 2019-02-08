<template>
    <div>
        <h2>Trading</h2>
        <div v-if="userIsActive">
            <p>Please select an industry tile from and opponent and offer an amount of money, or pass</p>
            <p><button class="btn btn-default" 
                    :class="enableButton(selectedPlayerAndTile, username)"
                    @click="offerTrade(selectedPlayerAndTile, tradeMoney)"> 
                        Offer Trade
               </button> 
                 {{tradeMoney}} {{selectedPlayer(selectedPlayerAndTile) }} {{selectedTile(selectedPlayerAndTile)}}</p>
            <button class="btn btn-default" @click="passTrading()"> Pass </button> 
            <hr>
            <div v-if="sliderOptions.max>0">
                <vue-slider ref="slider" v-model="tradeMoney" v-bind="sliderOptions"></vue-slider>
                <input v-model="tradeMoney">
                <hr>
            </div>
            <p><button class="btn btn-default" 
                    :class="enableLuxuryButton(selectedLuxuryTile, username)"
                       @click="buyLuxuryTile(selectedLuxuryTile)"> 
                       Buy Luxury Tile 
               </button> 
               {{selectedLuxuryTile}}
            </p>
        </div>
        <div v-else>
            <p> {{activePlayerName}} must offer a trade, or pass</p>
        </div>
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
                'userIsActive',
                'activePlayer',
                'activePlayerName',
                'username',
                'luxuryTiles',
                'selectedLuxuryTile',
                'selectedPlayerAndTile'
            ]),
            sliderOptions() {
                // we know that the user is the active player:
                //      if no money: min=0, max=0
                //      if money: min=1, max = money
                // just in case user does not exist 
                // (should not happen here):
                //       min=0, max=0
                var min = 0
                var max = 0
                if (this.username != null) {
                    max = this.activePlayer.money
                    min = 0 ? max==0 : 1
                } 
                return {
                    min: min,
                    max: max
                }
            }
        },
        methods: {
            ...mapActions([
                'setGameState',
                'clearSelections'
            ]),
            correctLuxurySelection(tile, player) {
                if (tile!=null) {
                    return player.money > this.luxuryTiles[tile].value
                } else {
                    return 0
                }
            },
            enableLuxuryButton(luxuryTile, player) {
                if (this.correctLuxurySelection(luxuryTile, player)) {
                    return ""
                } else {
                    return "disabled"
                }
            },
            correctSelection(playerAndTile, player) {
                var tile = this.selectedTile(playerAndTile)
                if (tile == "no tile") {
                    return 0
                } else {
                    return player.industryTiles[tile] > 0
                }
            },
            enableButton(playerAndTile, player) {
                if (this.correctSelection(playerAndTile, player)) {
                    return ""
                } else {
                    return "disabled"
                }
            },
            selectedTile(sel) {
                if (sel) {
                    return sel.tile 
                } else {
                    return "no tile"
                }
            },
            selectedPlayer(sel) {
                if (sel) {
                    return sel.name 
                } else {
                    return "no name"
                }
            },
            buyLuxuryTile(tile) {
                console.log("in buyLuxuryTile")
                if (this.username && tile!=null &&
                    this.correctLuxurySelection(tile, activePlayer)) {
                    var json = {"tile": tile, "name": this.username}
                    console.log(json)
                    axios.put('/game/buyLuxuryTile', json)
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
                    }); 
                }
            },
            offerTrade(playerAndTile, money) {
                console.log("in offerTrade")
                console.log(this.username, playerAndTile.name, playerAndTile.tile, money)
                console.log(this.correctSelection(playerAndTile, this.username))
                if (this.username && playerAndTile && 
                    money != null && this.correctSelection(playerAndTile, activePlayer)) {
                    var json = {"money": money, "tile": playerAndTile.tile, "opponentName": playerAndTile.name,
                                "name": this.username}
                    console.log(json)
                    axios.put('/game/offerTrade', json)
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
                    }); 
                }
            },
            passTrading() {
                console.log("in passTrade")
                if (this.username) {
                    var json = {"name": this.username}
                    axios.put('/game/passTrading', json)
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
</style>
