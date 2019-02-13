<template>
    <div>
        <h2>Luxury Tiles</h2>
        <div class="row">
            <div class="col-3" v-for="(tile, i) in luxuryTiles" :key="i">
                    <luxury-tile 
                        :value="tile.value" 
                        :points="tile.points" 
                        @click.native="select(i)">
                    </luxury-tile>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';
    import {mapActions} from 'vuex';
    import LuxuryTile from './LuxuryTile.vue';

    export default {
        components: {
            luxuryTile: LuxuryTile
        },
        computed: {
            ...mapGetters([
                'tradeOffer',
                'phase',
                'userIsActive',
                'luxuryTiles',
                'selectedLuxuryTile'
            ])    
        },
        methods: {
            ...mapActions([
                'selectLuxuryTile'
            ]),
            select(i) {
                if (this.phase==2 && !this.tradeOffer && this.userIsActive) {
                    if (this.selectedLuxuryTile==i) {
                        this.selectLuxuryTile(null)
                    } else {
                        this.selectLuxuryTile(i)
                    }
                }
            }
        }
    }    
</script>

<style scoped>
</style>
