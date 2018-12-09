<template>
    <div class="log"> 
        <!--
            need an additional div to get the scroll 
            down to bottom feature working 
            https://stackoverflow.com/questions/18614301/keep-overflow-div-scrolled-to-bottom-unless-user-scrolls-up
        -->
        <div>
            <h2> Log </h2>
            <div v-for="line in log"> {{line}} </div>
        </div>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    export default {
        computed: {
            ...mapGetters([
                'log'
            ])    
        }
    }    
</script>

<style scoped>
.log {
    border-style: solid;
    height: 350px;
    overflow: auto;
    display: flex;
    flex-direction: column-reverse;
}
</style>
