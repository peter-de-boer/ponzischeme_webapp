<template>
    <div>
        <h2>Trading</h2>
        <div v-if="userIsActive">
            Please select an industry tile from an opponent and offer an amount of money, or pass.<br>
            <span v-if="advanced">Alternatively, buy a luxury tile.<br></span> <br>
            <p><button class="btn btn-default" 
                    :class="enableButton(selectedPlayerAndTile)"
                    @click="offerTrade(selectedPlayerAndTile, tradeMoney)"> 
                        Offer Trade
               </button> 
               <br>
               <span v-if="selectedPlayerAndTile"> 
                 [offer ${{tradeMoney}} 
                  to {{selectedPlayer(selectedPlayerAndTile) }} 
                  for {{tileName(selectedTile(selectedPlayerAndTile))}} tile]
               </span>
            </p>
            <button class="btn btn-default" @click="passTrading()"> Pass </button> 
            <hr>
            <div v-if="sliderOptions.max>0">
                <vue-slider ref="slider" v-model="tradeMoney" v-bind="sliderOptions"></vue-slider>
                <!-- <input v-model="tradeMoney"> -->
                <hr>
            </div>
            <p v-if="advanced"><button class="btn btn-default" 
                    :class="enableLuxuryButton(selectedLuxuryTile)"
                       @click="buyLuxuryTile(selectedLuxuryTile)"> 
                       Buy Luxury Tile 
               </button> 
               {{selectedLuxuryTile}}
            </p>
        </div>
        <div v-else>
            <p> {{activePlayer.name}} must offer a trade, or pass</p>
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
                'id',
                'userIsActive',
                'activePlayer',
                'token',
                'username',
                'luxuryTiles',
                'selectedLuxuryTile',
                'selectedPlayerAndTile',
                'advanced',
                'tileName'
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
            correctLuxurySelection(tile) {
                if (tile!=null) {
                    return this.activePlayer.money > this.luxuryTiles[tile].value
                } else {
                    return 0
                }
            },
            enableLuxuryButton(luxuryTile) {
                if (this.correctLuxurySelection(luxuryTile)) {
                    return ""
                } else {
                    return "disabled"
                }
            },
            correctSelection(playerAndTile) {
                var tile = this.selectedTile(playerAndTile)
                if (tile == "no tile") {
                    return 0
                } else {
                    return this.activePlayer.industryTiles[tile] > 0
                }
            },
            enableButton(playerAndTile) {
                if (this.correctSelection(playerAndTile)) {
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
                if (this.token && tile!=null &&
                    this.correctLuxurySelection(tile)) {
                    var json = {"tile": tile, "token": this.token, "id": this.id}
                    axios.put('/game/buyLuxuryTile', json)
                        .then( res => {
                            if (res.data[1].error) {
                                console.log(res.data[1].error)
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
                if (this.token && playerAndTile && 
                    money != null && this.correctSelection(playerAndTile)) {
                    var json = {"money": money, "tile": playerAndTile.tile, "opponentName": playerAndTile.name,
                                "token": this.token, "id": this.id}
                    axios.put('/game/offerTrade', json)
                        .then( res => {
                            if (res.data[1].error) {
                                console.log(res.data[1].error)
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
                if (this.token) {
                    var json = {"token": this.token, "id": this.id}
                    axios.put('/game/passTrading', json)
                        .then( res => {
                            if (res.data[1].error) {
                                console.log(res.data[1].error)
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
