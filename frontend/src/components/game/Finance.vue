<template>
    <div class="finance">
        <div class="row">
            <div class="col-12">
                <h2> Finance Overview </h2>
            </div>
            <div class="col-12">
                {{finance}}
            </div>
        </div>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';

    export default {
        computed: {
            ...mapGetters([
                'gameStateLoaded',
                'finance'
            ])
        }
    }    
</script>

<style scoped>
.finance {
    border-style: solid;
}
</style>
