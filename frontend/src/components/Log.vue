<template>
    <div class="log">
        <h2> Log </h2>
        <div v-for="line in log"> {{line}} </div>
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
}
</style>
