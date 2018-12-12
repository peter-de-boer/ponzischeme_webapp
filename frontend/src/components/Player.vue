<template>
    <div class="player" 
        :class="hiLight(player.name, selectedPlayerAndTile)">
        <p class="player-name">
            {{player.name}}
        </p>
        <p class="money">
            ${{player.money}}
        </p>
        <div style="clear: both;"></div>

        <div class="row">
            <div class="col-3" v-for="(tile, i) in player.luxuryTiles" :key="i">
                <div class="tile" >
                    {{tile.value}} {{tile.points}}
                </div>
            </div>
        </div>

        <player-industry-tiles :industryTiles="player.industryTiles" :name="player.name"></player-industry-tiles>
        <hr>
        <time-wheel :wheel="player.wheel"></time-wheel>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';
    import TimeWheel from './TimeWheel.vue'
    import PlayerIndustryTiles from './PlayerIndustryTiles.vue'

    export default {
        props: ['player'],
        computed: {
            ...mapGetters([
                'phase',
                'selectedPlayerAndTile'
            ])
        },
        components: {
            timeWheel: TimeWheel,
            playerIndustryTiles: PlayerIndustryTiles
        },
        methods: {
            hiLight(name, sel) {
                if (sel && name==sel.name && this.phase==2) {
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
    border-color: transparent;
}

.player {
    border-style: inset;
    border-width: 2px;
    background-color: lightblue;
    margin-bottom: 5px;
    margin-top: 5px;
}

.player-name {
    font-size: 2em;
    font-weight: 1000;
	float: left;
}

.money {
    font-size: 1.5em;
	float: right;
}

.hilight {
}

.nohilight {
    border-color: transparent;
}

</style>
