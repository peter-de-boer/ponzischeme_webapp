<template>
    <div>
        <h2>Luxury Tiles</h2>
        <div class="row">
            <div class="col-sm-2" v-for="(tile, i) in luxuryTiles" :key="i">
                <div class="tile" :class="hiLight(i, selectedLuxuryTile)" 
                     @click="select(i)" >
                    {{tile.value}} {{tile.points}}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';
    import {mapActions} from 'vuex';

    export default {
        computed: {
            ...mapGetters([
                'tradeOffer',
                'phase',
                'currentIsActive',
                'luxuryTiles',
                'selectedLuxuryTile'
            ])    
        },
        methods: {
            ...mapActions([
                'setGameState',
                'selectLuxuryTile'
            ]),
            select(i) {
                if (this.phase==2 && !this.tradeOffer && this.currentIsActive) {
                    if (this.selectedLuxuryTile==i) {
                        this.selectLuxuryTile(null)
                    } else {
                        this.selectLuxuryTile(i)
                    }
                }
            },
            hiLight(i, sel) {
                if (sel==i) {
                    return "hilight";
                } else {
                    return "nohilight";
                }
            }
        }
    }    
</script>

<style scoped>

.tile {
    border-style: inset;
    border-width: 2px;
    background-color: grey;
}

.hilight {
}

.nohilight {
    border-color: transparent;
}

</style>
