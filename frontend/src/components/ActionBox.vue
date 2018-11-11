<template>
    <div>
        <action-funding v-if="isPhase1"></action-funding>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import ActionFunding from './ActionFunding.vue';
    export default {
        computed: {
            ...mapGetters([
                'isPhase1'
            ])    
        },
        components: {
            actionFunding: ActionFunding
        }
    }    
</script>

<style scoped>

</style>
