<template>
    <div class="row">
        <div class="col-xs-12 col-sm-6 col-md-3 col-lg-2 col-xl-2" >
            <router-link
                tag="button"
                :to="{name: 'game', params: {id: game.id}}">
                    Game id: {{game.id}} 
            </router-link>
            {{game.advanced ? "adv" : ""}} <br>
            {{game.nplayers}} players <br>
            <div v-for="(player, index) in game.players" :key="index">
                {{player.username}} <br>
            </div>
        </div>
    </div>
</template>

<script>

    export default {
        props: ['game'],
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
