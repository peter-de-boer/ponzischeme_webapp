<template>
    <div class="action">
        <h2>Funding</h2>
        <p>Please select an industry tile and a fund card, or pass</p>
        <p><button class="btn btn-default">Select Tile/Card</button> {{selectedFundCard.value}}</p>
        <button class="btn btn-default">Pass</button>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';

    export default {
        computed: {
            ...mapGetters([
                'isPhase1',
                'selectedFundCard'
            ])    
        },
        methods: {
            selectTileAndCard() {
                console.log("in selectcard")
                var json = {"value": value, "name": currentPlayer.name}
                axios.put('/game/selectCard', json)
                    .then( res => {
                        console.log(res)
                        this.setGameState(res.data)
                }, error => {
                    console.log(error)
                }); 
            }
        }
    }
</script>

<style scoped>
.action {
  border-style: solid;
}
</style>
