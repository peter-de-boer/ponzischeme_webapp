<template>
    <div class="chat">
        <h2> Chat </h2>
        <div ref="myid" class="posts"> 
            <!--
                see Log.vue for scroll issue
            -->
                <div v-for="line in gameChat">  
                    {{getTimeStamp(line[2])}} <span style='font-weight: bold'> {{line[0]}}</span>: {{line[1]}}
                </div>
        </div>
        <form @submit.prevent="onSubmit">
            <input
                type="text"
                autocomplete="off"
                id="post"
                v-model="post">
            <span>
              <button type="submit">Send</button>
            </span>
        </form>
    </div>
</template>

<script>
    import axios from 'axios';
    import { mapActions } from 'vuex';
    import { mapGetters } from 'vuex';
    import shared from '@/shared';

    export default {
        data () {
            return {
                post: '',
            }
        },
        created() {
            this.getTimeStamp = shared.getTimeStamp;
        },
        mounted() {
            this.scrollToEnd()
        },
        computed: {
            ...mapGetters([
                'id',
                'token',
                'gameChat',
                'gameStateLoaded',
                'username'
            ])
        },
        methods: {
            ...mapActions([
                'setGameState',
                'loadingOn',
                'loadingOff'
            ]),
            scrollToEnd() {
              var self = this
              setTimeout(function() {
                var container = self.$refs["myid"];
                container.scrollTop = container.scrollHeight;
              },500)
            },
            onSubmit () {
                if (this.token) {
                    var json = {"post": this.post, "token": this.token, "id": this.id}
                    this.loadingOn()
                    axios.put('/game/chat', json)
                        .then( res => {
                            if (res.data[1].error) {
                                console.log(res.data[1].error)
                            } else {
                                this.setGameState(res.data);
                                this.post="";
                                this.scrollToEnd();
                            }
                        })
                        .catch( error => {
                            console.log(error)
                        })
                        .then( () => {
                            this.loadingOff()
                        }); 
                }
            }
        }
    }    
</script>

<style scoped>
.chat {
    border-style: solid;
    height: 350px;
}
.posts {
    height: 275px;
    overflow: auto;
}
</style>
