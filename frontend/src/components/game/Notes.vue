<template>
    <div class="notes">
        <h2> Notes </h2>
        <div ref="myid" class="nnotes"> 
            <textarea 
                v-model="notes" 
                placeholder="add your notes" 
                style="width:100%; height:100%;"
                @keyup="changeNotes"
            >
            </textarea>
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
                notes: '',
            }
        },
        mounted() {
            this.notes = this.gameNotes;
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
                'setGameState',
                'setGameNotes'
            ]),
            changeNotes() {
                this.setGameNotes(this.notes)
            }
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
    background: white;
}
</style>
