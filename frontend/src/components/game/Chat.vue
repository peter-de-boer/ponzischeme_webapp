<template>
    <div class="chat">
        <h2> Chat </h2>
        <div ref="myid" class="posts"> 
            <!--
                see Log.vue for scroll issue
            -->
                <div v-for="line in gameChat" v-html="line">  </div>
        </div>
        <form @submit.prevent="onSubmit">
            <input
                type="text"
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

    export default {
        data () {
            return {
                post: '',
            }
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
                'setGameState'
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
                    axios.put('/game/chat', json)
                        .then( res => {
                            if (res.data.error) {
                                console.log(res.data.error)
                            } else {
                                this.setGameState(res.data);
                                this.post="";
                                this.scrollToEnd();
                            }
                    }, error => {
                        console.log(error)
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
