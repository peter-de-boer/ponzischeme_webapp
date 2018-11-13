<template>
    <div>
        <h2>End Of Game</h2>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    export default {
        computed: {
            ...mapGetters([
                'phase'
            ])    
        }
    }    
</script>

<style scoped>

</style>
