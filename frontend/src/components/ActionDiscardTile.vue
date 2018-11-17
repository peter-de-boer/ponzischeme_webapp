<template>
    <div class="action">
        <h2>Discard Tile</h2>
        <p>Please select an industry tile to discard</p>
        <p><button class="btn btn-default" 
                @click="discardTile(selectedIndustryTile)"> 
                    Discard Tile
           </button> 
             {{selectedIndustryTile}}</p>
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
                'selectedIndustryTile'
            ])    
        },
        methods: {
            ...mapActions([
                'setGameState'
            ]),
            discardTile(tile) {
                console.log("in discardTile")
                if (this.currentPlayer) {
                    var json = {"tile": tile, "name": this.currentPlayer.name}
                    console.log(json)
                    axios.put('/game/discardTile', json)
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
            }
        }
    }
</script>

<style scoped>
.action {
  border-style: solid;
}
</style>
