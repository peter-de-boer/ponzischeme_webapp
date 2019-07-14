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
            <p>{{activePlayer.name}} must select an industry tile to discard</p>
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
                'activePlayer',
                'userIsActive',
                'token',
                'username',
                'selectedPlayerAndTile'
            ])    
        },
        methods: {
            ...mapActions([
                'doAction'
            ]),
            discardTile(playerAndTile) {
                console.log("in discardTile")
                if (this.token && playerAndTile && playerAndTile.name==this.activePlayer.name) {
                    var json = {"tile": playerAndTile.tile, "token": this.token, "id": this.id}
                    this.doAction({route: '/game/discardTile', json})
                }
            }
        }
    }
</script>

<style scoped>
</style>
