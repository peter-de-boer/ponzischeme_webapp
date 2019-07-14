<template>
    <div>
        <div>
            <h2>Funding</h2>
            <div v-if="userIsActive">
                <p>Please select an industry tile and a fund card, or pass</p>
                <p><button class="btn btn-default" 
                        :class="enableButton(selectedFundCard, selectedIndustryTile)"
                        @click="selectTileAndCard(selectedFundCard, selectedIndustryTile)"> 
                            Select Tile/Card 
                   </button> 
                     <br> [
                     <span v-if="selectedIndustryTile!=null"> 
                        {{tileName(selectedIndustryTile)}} tile 
                     </span>
                     /
                     <span v-if="selectedFundCard"> 
                       fundcard {{selectedFundCard.value}} 
                     </span>
                     ]
                </p>
                <button class="btn btn-default" @click="passFunding()"> Pass </button> 
            </div>
            <div v-else>
                {{activePlayer.name}} must select an industry tile and a fund card, or pass
            </div>
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
                'fundingBoard',
                'userIsActive',
                'token',
                'activePlayer',
                'username',
                'isPhase1',
                'selectedFundCard',
                'selectedIndustryTile',
                'tileName'
            ])    
        },
        methods: {
            ...mapActions([
                'doAction'
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
            correctSelection(card, tile) {
                return (this.activePlayer && card!= null && tile!=null && 
                        this.activePlayer.industryTiles[tile]+1==this.getRow(card))
            },
            enableButton(card, tile) {
                if (this.correctSelection(card, tile)) {
                    return ""
                } else {
                    return "disabled"
                }
            },
            selectTileAndCard(card,tile) {
                // if (this.username && card != null && tile != null) {
                if (this.correctSelection(card, tile)) {
                    var json = {"value": card.value, "tile": tile, "token": this.token, "id": this.id}
                    this.doAction({route: '/game/selectTileAndCard', json})
                }
            },
            passFunding() {
                if (this.token) {
                    var json = {"token": this.token, "id": this.id}
                    this.doAction({route: '/game/passFunding', json})
                }
            }
        }
    }
</script>

<style scoped>
</style>
