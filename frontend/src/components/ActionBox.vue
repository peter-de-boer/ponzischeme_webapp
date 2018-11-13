<template>
    <div>
        <action-funding v-if="phase==1"></action-funding>
        <action-pass-marker v-if="phase==3"></action-pass-marker>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import ActionFunding from './ActionFunding.vue';
    import ActionPassMarker from './ActionPassMarker.vue';
    export default {
        computed: {
            ...mapGetters([
                'phase'
            ])    
        },
        components: {
            actionFunding: ActionFunding,
            actionPassMarker: ActionPassMarker
        }
    }    
</script>

<style scoped>

</style>
