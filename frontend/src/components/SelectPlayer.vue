<template>
    <div>
        <div class="row">
            <div class="col-sm-2" v-for="plr in players" @click="selectCurrentPlayer(plr)" :key="plr.name">
                <p :class="[{notcurrent: (!currentPlayer ||currentPlayer.name!=plr.name) }, 
                            {current: (currentPlayer && currentPlayer.name==plr.name) }]"> {{plr.name}} </p>
            </div>
            <div class="col-sm-2" @click="selectCurrentPlayer(dummy)">
                <p :class="[{notcurrent: (!currentPlayer ||currentPlayer.name!=dummy.name) }, 
                            {current: (currentPlayer && currentPlayer.name==dummy.name) }]"> {{dummy.name}} </p>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';
    import {mapActions} from 'vuex';

    export default {
        data() {
            return {
                dummy: {
                    name: 'Watcher'
                },
                noPlayer: {
                }
            }
        },
        computed: {
            ...mapGetters([
                'currentPlayer',
                'players'
            ])    
        },
        methods: {
            ...mapActions([
                'selectCurrentPlayer'
            ])    ,
            selectDummyPlayer() {
                
            }
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
