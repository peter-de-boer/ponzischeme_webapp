<template>
    <div class="notes">
        <div class="row">
            <div class="col-10">
                <h2> Notes </h2>
            </div>
            <div class="col-2">
              <!--  {{saveStatus}} -->
            </div>
        </div>
        <div ref="myid" class="nnotes"> 
            <textarea 
                v-model="notes" 
                placeholder="add your notes" 
                style="width:100%; height:100%;"
            >
            </textarea>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import { mapActions } from 'vuex';
    import { mapGetters } from 'vuex';
    import { debounce } from 'lodash';

    export default {
        data () {
            return {
                notes: '',
                currentGameNotes: {},
                saveStatus: ""
            }
        },
        mounted() {
            this.resetNotes()
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
        watch: {
            notes: function(value) {
                this.currentGameNotes.notes = value;
                this.sendToServer()
            }
        },
        methods: {
            ...mapActions([
                'setGameState'
            ]),
            sendToServer: debounce(
                function() {
                    this.saveStatus = "saving...";
                    var json = {"token": this.token, "notes": this.currentGameNotes}
                    axios.put('/game/notes', json)
                        .then( res => {
                            if (res.data[1].error) {
                                this.saveStatus = "not saved";
                                console.log(res.data[1].error)
                            } else {
                                this.setGameState(res.data);
                                this.saveStatus = "saved";
                            }
                        })
                        .catch(error => {
                            this.saveStatus = "not saved";
                            console.log(error)
                        })
                },
                1000
            ),
            resetNotes() {
                var self = this
                setTimeout(function() {
                    self.currentGameNotes = self.gameNotes;
                    self.notes = self.currentGameNotes.notes;
                },1000)
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
