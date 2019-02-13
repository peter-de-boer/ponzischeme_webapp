<template>
    <div>
        Number of players:
        <input type="radio" name="npl" value=3 v-model.number="nplayers"  checked> 3
        <input type="radio" name="npl" value=4 v-model.number="nplayers" > 4
        <input type="radio" name="npl" value=5 v-model.number="nplayers" > 5<br>
        Advanced <input type="checkbox" id="adv" v-model="advanced"> <br>
        <button @click="createGame(nplayers,advanced)">Create</button>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    export default {
        data: function() {
            return {
                nplayers: 3,
                advanced: false
            }
        },
        computed: {
            ...mapGetters([
                'token',
                'isAuthenticated'
            ])    
        },
        methods: {
            createGame(nplayers,advanced) {
                if (this.token) {
                    var json = {"nplayers": nplayers, "advanced": advanced, "token": this.token}
                    //axios.put('/creategame', json)
                    //    .then( res => {
                    //        console.log(res)
                    //}, error => {
                    //    console.log(error)
                    //}); 
                }
                else {
                    console.log("no token")
                }
            }
        }
    }    
</script>

<style scoped>
</style>
