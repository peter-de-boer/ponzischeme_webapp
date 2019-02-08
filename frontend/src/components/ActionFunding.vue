<template>
    <div>
        <div>
            <h2>Funding</h2>
            <div v-if="userIsActive">
                <p>Please select an industry tile and a fund card, or pass</p>
                <p><button class="btn btn-default" 
                        :class="enableButton(selectedFundCard, selectedIndustryTile, username)"
                        @click="selectTileAndCard(selectedFundCard, selectedIndustryTile)"> 
                            Select Tile/Card 
                   </button> 
                     {{selectedFundCard ? selectedFundCard.value : ""}} {{selectedIndustryTile}}</p>
                <button class="btn btn-default" @click="passFunding()"> Pass </button> 
            </div>
            <div v-else>
                {{activePlayerName}} must select an industry tile and a fund card, or pass
            </div>
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
                'fundingBoard',
                'userIsActive',
                'activePlayerName',
                'username',
                'isPhase1',
                'selectedFundCard',
                'selectedIndustryTile'
            ])    
        },
        methods: {
            ...mapActions([
                'setGameState',
                'clearSelections'
            ]),
            getRow(myCard) {
                var row = 0
                if (this.fundingBoard) {
                    for (const [index, card] of this.fundingBoard.entries()) {
                        if (card.value == myCard.value) {
                            row = Math.floor(index/3) + 1
                        }
                    }
                } 
                return row
            },
            correctSelection(card, tile, player) {
                return (player && card!= null && tile!=null && 
                        player.industryTiles[tile]+1==this.getRow(card))
            },
            enableButton(card, tile, player) {
                if (this.correctSelection(card, tile, player)) {
                    return ""
                } else {
                    return "disabled"
                }
            },
            selectTileAndCard(card,tile) {
                console.log("in selectTileAndCard")
                // if (this.username && card != null && tile != null) {
                if (this.correctSelection(card, tile, this.username)) {
                    var json = {"value": card.value, "tile": tile, "name": this.username}
                    console.log(json)
                    axios.put('/game/selectTileAndCard', json)
                        .then( res => {
                            console.log(res)
                            if (res.data.error) {
                                console.log(res.data.error)
                            } else {
                                this.setGameState(res.data)
                //                this.clearSelections()
                            }
                    }, error => {
                        console.log(error)
                    }); 
                }
            },
            passFunding() {
                console.log("in passFunding")
                if (this.username) {
                    var json = {"name": this.username}
                    axios.put('/game/passFunding', json)
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
</style>
