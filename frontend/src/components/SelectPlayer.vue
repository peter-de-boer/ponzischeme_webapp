<template>
    <div>
        <div class="row">
            <div class="col-2 col-lg-1 " v-for="plr in players" @click="selectCurrentPlayer(plr)" :key="plr.name">
                <p :class="[{notcurrent: (!username ||username.name!=plr.name) }, 
                            {current: (username && username.name==plr.name) }]"> {{plr.name}} </p>
            </div>
            <div class="col-2 col-lg-1 " @click="selectCurrentPlayer(dummy)">
                <p :class="[{notcurrent: (!username ||username.name!=dummy.name) }, 
                            {current: (username && username.name==dummy.name) }]"> {{dummy.name}} </p>
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
                'username',
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
