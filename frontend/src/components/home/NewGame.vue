<template>
    <div class="newgame">
        Game id: {{game.id}} <br>
        
        Variant: {{game.advanced ? "advanced" : "standard"}} <br>
        # players: {{game.nplayers}} <br>
        <div v-for="(player, index) in game.players" :key="index">
            <span class="player">{{player.username}}</span> 
                <button v-if="username==player.username &&
                              username!=game.owner.username"
                        @click="leaveGame(game.id)"  > X </button>
        </div>
        <div v-if="game.players.length < game.nplayers">
            <button :disabled="canNotJoin(game.players)"
                    @click="joinGame(game.id)"> join </button>
            <div v-for="i in (game.nplayers-game.players.length-1)">  
                <button disabled> join </button>
            </div>
        </div>
        <div v-if="game.owner.username==username">
            <button v-if="game.nplayers==game.players.length"
                    @click="startGame(game.id)"> start </button>
            <button @click="deleteGame(game.id)"> delete game</button>
        </div>
        <div v-else-if="game.nplayers==game.players.length">
            Waiting for {{game.owner.username}} to start
        </div>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import { mapActions } from 'vuex';

    export default {
        props: ['game'],
        computed: {
            ...mapGetters([
                'username',
                'token'
            ])    
        },
        methods: {
            ...mapActions([
                'doListAction'
            ])    ,
            canNotJoin(players) {
                return !this.username || players.some(player => player.username==this.username)
            },
            deleteGame(id) {
                if (this.token) {
                    var json = {"id": id, "token": this.token}
                    this.doListAction({route: '/deleteGame', json})
                }
                else {
                }
            },
            joinGame(id) {
                if (this.token) {
                    var json = {"id": id, "token": this.token}
                    this.doListAction({route: '/joinGame', json})
                }
                else {
                }
            },
            leaveGame(id) {
                if (this.token) {
                    var json = {"id": id, "token": this.token}
                    this.doListAction({route: '/leaveGame', json})
                }
                else {
                }
            },
            startGame(id) {
                if (this.token) {
                    var json = {"id": id, "token": this.token}
                    this.doListAction({route: '/startGame', json})
                }
                else {
                }
            }
        }

    }    
</script>

<style scoped>

.newgame {
    border-style: outset;
    border-width: 2px;
    background-color: lightgrey;
    margin-bottom: 5px;
    margin-top: 5px;
}

.player {
    font-weight: bold;
}


</style>
