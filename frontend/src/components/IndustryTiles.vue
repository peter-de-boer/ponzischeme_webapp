<template>
    <div>
        <h2>Industry Tiles</h2>
        <div class="row">
            <div class="col-xs-2" v-for="(tiles, i) in industryTiles" :key="i">
                <div class="tile" :class="[tileStyle(i), hiLight(i, selectedIndustryTile)]" 
                     @click="select(i)" >
                    {{tiles}}
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
                'currentIsActive',
                'phase',
                'industryTiles',
                'selectedIndustryTile'
            ])    
        },
        methods: {
            ...mapActions([
                'setGameState',
                'selectIndustryTile'
            ]),
            select(i) {
                if (this.currentIsActive && this.phase==1) {
                    if (this.selectedIndustryTile==i) {
                        this.selectIndustryTile(null)
                    } else {
                        this.selectIndustryTile(i)
                    }
                }
            },
            tileStyle(i) {
                switch(i) {
                    case 0:
                        return "transport";
                    case 1:
                        return "grain";
                    case 2:
                        return "medix";
                    case 3:
                        return "realestate";
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
}

.hilight {
}

.nohilight {
    border-color: transparent;
}

.transport {
    background-color: blue
}

.grain {
    background-color: yellow
}

.medix {
    background-color: green
}

.realestate {
    background-color: red
}

</style>
