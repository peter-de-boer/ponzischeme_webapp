<template>
    <div class="action">
        <h2>Funding</h2>
        <p>Please select an industry tile and a fund card, or pass</p>
        <p><button class="btn btn-default" 
                @click="selectTileAndCard(selectedFundCard.value,selectedIndustryTile)"> 
                    Select Tile/Card 
           </button> 
             {{selectedFundCard.value}} {{selectedIndustryTile}}</p>
        <button class="btn btn-default" @click="passFunding()"> Pass </button> 
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
                'isPhase1',
                'selectedFundCard',
                'selectedIndustryTile'
            ])    
        },
        methods: {
            ...mapActions([
                'setGameState'
            ]),
            selectTileAndCard(value,tile) {
                console.log("in selectTileAndCard")
                if (this.currentPlayer) {
                    var json = {"value": value, "tile": tile, "name": this.currentPlayer.name}
                    console.log(json)
                    axios.put('/game/selectTileAndCard', json)
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
