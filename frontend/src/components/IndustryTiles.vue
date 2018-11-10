<template>
    <div class="container">
        <h2>Industry Tiles</h2>
        <div class="row">
            <div class="col-sm-1" v-for="(tiles, i) in industryTiles" :key="i">
                <div :class="tileStyle(i)">
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
                'industryTiles'
            ])    
        },
        methods: {
            ...mapActions([
                'setGameState'
            ]),
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
