<template>
    <div class="action">
        <h2>Pass the Start Player Marker</h2>
        <p>Please select a fund card to discard (or remove, if blue)</p>
        <p><button class="btn btn-default" 
                @click="selectCardToDiscard(selectedFundCard.value)"> 
                    Select Tile/Card 
           </button> 
             {{selectedFundCard.value}} </p>
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
                'selectedFundCard'
            ])    
        },
        methods: {
            ...mapActions([
                'setGameState'
            ]),
            selectCardToDiscard(value) {
                console.log("in selectCardToDiscard")
                if (this.currentPlayer) {
                    var json = {"value": value, "name": this.currentPlayer.name}
                    console.log(json)
                    axios.put('/game/selectCardToDiscard', json)
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
            passFunding() {
                console.log("in passFunding")
                if (this.currentPlayer) {
                    var json = {"name": this.currentPlayer.name}
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
.action {
  border-style: solid;
}
</style>
