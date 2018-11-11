<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-2" v-for="plr in players" @click="selectCurrentPlayer(plr)">
                <p :class="[{notcurrent: (!currentPlayer ||currentPlayer.name!=plr.name) }, 
                            {current: (currentPlayer && currentPlayer.name==plr.name) }]"> {{plr.name}} </p>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';
    import {mapActions} from 'vuex';

    export default {
        computed: {
            ...mapGetters([
                'currentPlayer',
                'players'
            ])    
        },
        methods: {
            ...mapActions([
                'selectCurrentPlayer'
            ])    
        }
    }    
</script>

<style scoped>
.current {
    background-color: orange;
}
.notcurrent {
    background-color: lightgreen;
}
</style>
