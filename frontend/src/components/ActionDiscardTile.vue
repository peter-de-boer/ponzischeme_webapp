<template>
    <div>
        <h2>Discard Tile</h2>
        <div v-if="userIsActive">
            <p>Please select an industry tile to discard</p>
            <p><button class="btn btn-default" 
                    @click="discardTile(selectedPlayerAndTile)"> 
                        Discard Tile
               </button> 
                 {{selectedPlayerAndTile ? selectedPlayerAndTile.tile : ""}}</p>
        </div>
        <div v-else>
            <p>{{activePlayerName}} must select an industry tile to discard</p>
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
                'activePlayerName',
                'userIsActive',
                'username',
                'selectedPlayerAndTile'
            ])    
        },
        methods: {
            ...mapActions([
                'clearSelections',
                'setGameState'
            ]),
            discardTile(playerAndTile) {
                console.log("in discardTile")
                if (this.username && playerAndTile) {
                    var json = {"tile": playerAndTile.tile, "name": playerAndTile.name}
                    console.log(json)
                    axios.put('/game/discardTile', json)
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
</style>
