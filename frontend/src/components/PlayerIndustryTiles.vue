<template>
    <div>
        {{maxTiles()}} {{industryTiles}}
        <div class="row" v-for="row in maxTiles()" :key="row + 'row'">
            <div class="col-sm-2" v-for="(tiles, i) in industryTiles" :key="i + 'x'">
                <div :class="tileStyle(i)" v-if="row>(maxTiles()-tiles)" @click="selectPlayerIndustryTile(i)">
                   <div class="bar"></div> 
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';
    import {mapActions} from 'vuex';

    export default {
        props: ['industryTiles'],
        methods: {
            ...mapActions([
                'setGameState',
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
            selectPlayerIndustryTile(i) {
            },
            tileStyle(i) {
                switch(i) {
                    case 0:
                        return "transport";
                    case 1:
                        return "grain";
                    case 2:
                        return "media";
                    case 3:
                        return "realestate";
                }
            }
        }
    }    
</script>

<style scoped>

.bar {
    height: 5px;
    margin-top:2px;
}

.transport {
    background-color: blue
}

.grain {
    background-color: yellow
}

.media {
    background-color: green
}

.realestate {
    background-color: red
}

</style>
