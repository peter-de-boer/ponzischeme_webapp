<template>
    <div>
        <h2>Pass the Start Player Marker</h2>
        <div v-if="userIsActive">
            <p>Please select a fund card to discard (or remove, if blue)</p>
            <p><button class="btn btn-default" 
                    :class="enableButton(selectedFundCard)"
                    @click="selectCardToDiscard(selectedFundCard)"> 
                        Select Card 
               </button> 
               <span v-if="selectedFundCard">
                    fundcard {{selectedFundCard.value}} 
               </span>
            </p>
        </div>
        <div v-else>
            <p>{{activePlayer.name}} must select a fund card to discard (or remove, if blue)</p>
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
                'selectedFundCard'
            ])    
        },
        methods: {
            ...mapActions([
                'doAction'
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
            enableButton(card) {
                if (this.correctSelection(card)) {
                    return ""
                } else {
                    return "disabled"
                }
            },
            selectCardToDiscard(card) {
                if (this.token && this.correctSelection(card)) {
                    var json = {"value": card.value, "token": this.token, "id": this.id}
                    this.doAction({route: '/game/selectCardToDiscard', json})
                }
            }
        }
    }
</script>

<style scoped>
</style>
