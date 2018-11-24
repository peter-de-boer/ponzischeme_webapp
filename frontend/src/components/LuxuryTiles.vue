<template>
    <div>
        <h2>Luxury Tiles</h2>
        <div class="row">
            <div class="col-sm-2" v-for="(tile, i) in luxuryTiles" :key="i">
                <div class="tile" :class="hiLight(i, selectedLuxuryTile)" 
                     @click="selectLuxuryTile(i)" >
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
                'luxuryTiles',
                'selectedLuxuryTile'
            ])    
        },
        methods: {
            ...mapActions([
                'setGameState',
                'selectLuxuryTile'
            ]),
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
