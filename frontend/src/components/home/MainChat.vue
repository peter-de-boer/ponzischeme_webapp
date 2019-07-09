<template>
    <div class="chat">
        <div ref="mymainid" class="posts"> 
            <!--
                see Log.vue for scroll issue
            -->
                <div v-for="line in mainChat">  
                    <span style='font-weight: bold'>{{line[0]}}</span>: {{line[1]}}
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

    export default {
        data () {
            return {
                post: '',
            }
        },
        created() {
            this.getMainChat()
        },
        mounted() {
            this.scrollToEnd()
        },
        computed: {
            ...mapGetters([
                'token',
                'mainChat'
            ])
        },
        methods: {
            ...mapActions([
                'setMainChat'
            ]),
            scrollToEnd() {
              var self = this
              setTimeout(function() {
                var container = self.$refs["mymainid"];
                container.scrollTop = container.scrollHeight;
              },500)
            },
            getMainChat() {
                var json = {"token": this.token}
                axios.get('/mainchat', { params: json })
                    .then( res => {
                        if (res.data[1].error) {
                            console.log(res.data[1].error)
                        } else {
                            this.setMainChat(res.data);
                            this.scrollToEnd();
                        }
                }, error => {
                    console.log(error)
                }); 
            },
            onSubmit () {
                if (this.token) {
                    var json = {"post": this.post, "token": this.token}
                    axios.put('/mainchat', json)
                        .then( res => {
                            if (res.data[1].error) {
                                console.log(res.data[1].error)
                            } else {
                                this.setMainChat(res.data);
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
    height: 305px;
}
.posts {
    height: 275px;
    overflow: auto;
}
</style>
