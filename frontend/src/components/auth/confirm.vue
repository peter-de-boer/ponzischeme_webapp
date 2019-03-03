<template>
    <div>
        <div v-if="status=='confirmed'">
            Your registration is successfully completed!
            You can now login.
        </div>
        <div v-if="status=='not confirmed'">
            Something went wrong.
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        props: ['token'],
        data() { 
            return {
                status: ""
            }
        },
        created() {
            var json = {"token": this.token}
            console.log(json)
            // need to do put instead of get request, else json arg is not working somehow
            axios.post('/user/confirm', json)
                .then( res => {
                    console.log(res)
                    this.status = res.data.status
                }, error => {
                    console.log(error)
                }); 
        }
      }
</script>

<style scoped>
</style>
