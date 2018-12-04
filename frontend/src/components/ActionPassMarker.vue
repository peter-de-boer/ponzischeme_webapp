<template>
    <div class="action">
        <h2>Pass the Start Player Marker</h2>
        <div v-if="currentIsActive">
            <p>Please select a fund card to discard (or remove, if blue)</p>
            <p><button class="btn btn-default" 
                    :class="enableButton(selectedFundCard)"
                    @click="selectCardToDiscard(selectedFundCard)"> 
                        Select Card 
               </button> 
                 {{selectedFundCard.value}} </p>
        </div>
        <div v-else>
            <p>{{activePlayerName}} must select a fund card to discard (or remove, if blue)</p>
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
                'currentIsActive',
                'activePlayerName',
                'currentPlayer',
                'selectedFundCard'
            ])    
        },
        methods: {
            ...mapActions([
                'clearSelections',
                'setGameState'
            ]),
            correctSelection(card) {
                var correct = 0
                if (card) { 
                    for (var i=0; i<this.fundingBoard.length; i++) {
                        if (this.fundingBoard[i].value==card.value) {
                            correct = 1
                        }
                    }
                }
                return correct

            },
            enableButton(card, player) {
                if (this.correctSelection(card)) {
                    return ""
                } else {
                    return "disabled"
                }
            },
            selectCardToDiscard(card) {
                console.log("in selectCardToDiscard")
                if (this.currentPlayer && this.correctSelection(card)) {
                    var json = {"value": card.value, "name": this.currentPlayer.name}
                    console.log(json)
                    axios.put('/game/selectCardToDiscard', json)
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
            }
        }
    }
</script>

<style scoped>
.action {
  border-style: solid;
}
</style>
