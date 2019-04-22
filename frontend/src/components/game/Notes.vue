<template>
    <div class="notes">
        <h2> Notes </h2>
        <div ref="myid" class="nnotes"> 
                {{gameNotes}}
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import { mapActions } from 'vuex';
    import { mapGetters } from 'vuex';

    export default {
        data () {
            return {
                post: '',
            }
        },
        computed: {
            ...mapGetters([
                'id',
                'token',
                'gameNotes',
                'gameStateLoaded',
                'username'
            ])
        },
        methods: {
            ...mapActions([
                'setGameState'
            ])
        }
    }    
</script>

<style scoped>
.notes {
    border-style: solid;
    height: 350px;
}
.nnotes {
    height: 295px;
    width: 98%;
    margin: 0 auto;
    overflow: auto;
    background: white;
}
</style>
