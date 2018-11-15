<template>
    <div>
        <action-funding v-if="phase==1"></action-funding>
        <action-pass-marker v-if="phase==3"></action-pass-marker>
        <action-discard-tile v-if="phase==4"></action-discard-tile>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import ActionFunding from './ActionFunding.vue';
    import ActionPassMarker from './ActionPassMarker.vue';
    import ActionDiscardTile from './ActionDiscardTile.vue';
    export default {
        computed: {
            ...mapGetters([
                'phase'
            ])    
        },
        components: {
            actionFunding: ActionFunding,
            actionPassMarker: ActionPassMarker,
            actionDiscardTile: ActionDiscardTile
        }
    }    
</script>

<style scoped>

</style>
