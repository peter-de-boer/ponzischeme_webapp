<template>
    <div class="newgame">
        Game id: {{game.id}} 
        
        {{game.advanced ? "adv" : ""}} <br>
        {{game.nplayers}} players <br>
        <div v-for="(player, index) in game.players" :key="index">
            {{player.username}} 
                <button v-if="username==player.username &&
                              username!=game.owner.username"> X </button>
        </div>
        <div v-if="game.players.length < game.nplayers">
            <button :disabled="canNotJoin(game.players)"> join </button>
            <div v-for="i in (game.nplayers-game.players.length)">  
                <button disabled> join </button>
            </div>
        </div>
        <div v-if="game.owner.username==username">
            <button> delete game</button>
            <button v-if="game.nplayers==game.players.length"> start </button>
        </div>
        <div v-else-if="game.nplayers==game.players.length">
            Waiting for owner to start
        </div>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';

    export default {
        props: ['game'],
        computed: {
            ...mapGetters([
                'username'
            ])    
        },
        methods: {
            canNotJoin(players) {
                return !this.username || players.some(player => player.username==this.username)
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




</style>
