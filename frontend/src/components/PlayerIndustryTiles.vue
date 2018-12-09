<template>
    <div>
        <div class="row" v-for="row in maxTiles()" :key="row + 'row'">
            <div class="col-2" v-for="(tiles, i) in industryTiles" :key="i + 'x'">
                <div 
                    v-if="row>(maxTiles()-tiles)" 
                    @click="selectPlayerIndustryTile(i, row, name)">
                   <div class="bar" :class="[tileStyle(i), hiLight(i, row, name, selectedPlayerAndTile)]" ></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';
    import {mapActions} from 'vuex';

    export default {
        props: ['industryTiles', 'name'],
        computed: {
            ...mapGetters([
                'tradeOffer',
                'currentIsActive',
                'activePlayerName',
                'phase',
                'selectedPlayerAndTile'
            ])
        },
        methods: {
            ...mapActions([
                'setGameState',
                'selectPlayerAndTile',
                'selectOpponentName',
                'selectIndustryTile'
            ]),
            maxTiles() {
                var max = 0;
                for (var i in this.industryTiles) {
                    if (this.industryTiles[i] > max) {
                        max = this.industryTiles[i]
                    }
                }
                return max
            },
            selectPlayerIndustryTile(tile, row, name) {
                var playerAndTile = {
                    tile: tile,
                    row: row,
                    name: name
                }
                if (this.currentIsActive && 
                    ((this.activePlayerName != name && 
                      this.phase==2 && 
                      !this.tradeOffer) ||
                    (this.activePlayerName == name && this.phase==4)))  {
                    if (this.selectedPlayerAndTile!=null && 
                        this.selectedPlayerAndTile.tile == tile &&
                        this.selectedPlayerAndTile.row == row && 
                        this.selectedPlayerAndTile.name == name) {
                        this.selectPlayerAndTile(null)
                    } else {
                        this.selectPlayerAndTile(playerAndTile)
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
            hiLight(tile,row,name,sel) {
                if (sel && (tile==sel.tile) && (row==sel.row) && (name==sel.name)) {
                    return "hilight";
                } else {
                    return "nohilight";
                }
            }
        }
    }    
</script>

<style scoped>

.hilight {
}

.nohilight {
    border-color: transparent;
}

.bar {
    height: 6px;
    margin-top:6px;
    border-style: solid;
    border-width: 2px;
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
