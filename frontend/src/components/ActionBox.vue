<template>
    <div class="action">
        <action-funding v-if="phase==1"></action-funding>
        <action-trading v-if="phase==2"></action-trading>
        <action-pass-marker v-if="phase==3"></action-pass-marker>
        <action-discard-tile v-if="phase==4"></action-discard-tile>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import ActionFunding from './ActionFunding.vue';
    import ActionTrading from './ActionTrading.vue';
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
            actionTrading: ActionTrading,
            actionPassMarker: ActionPassMarker,
            actionDiscardTile: ActionDiscardTile
        }
    }    
</script>

<style scoped>
.action {
  border-style: solid;
  height: 370px
}

</style>
