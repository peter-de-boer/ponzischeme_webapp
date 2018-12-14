<template>
    <div>
        <h2>Industry Tiles</h2>
        <div class="row">
            <div class="col-3" v-for="(tiles, i) in industryTiles" :key="i">
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
    box-shadow: 5px -5px, 10px -10px;
    text-align: center;
    font-weight: bold;
    width: 60px;
    height: 20px;
}

.hilight {
}

.nohilight {
    border-color: transparent;
}

.transport {
    background-color: #5F7F9D;
}

.grain {
    background-color: #E1C908;
}

.medix {
    background-color: #50A492;
}

.realestate {
    background-color: #A70909;
}

</style>
