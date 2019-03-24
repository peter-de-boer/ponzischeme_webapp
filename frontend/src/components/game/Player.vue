<template>
    <div class="player" 
        :class="hiLight(player.name, selectedPlayerAndTile)">
        <p class="player-name">
            <span v-if="activePlayer && activePlayer.name==player.name"> 
               > 
            </span>
            {{player.name}}
        </p>
        <p class="money">
            ${{player.money}}
        </p>
        <div style="clear: both;"></div>

        <div class="row">
            <div class="col-3" v-for="(tile, i) in player.luxuryTiles" :key="i">
                <luxury-tile :value="tile.value" :points="tile.points"></luxury-tile>
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
    import LuxuryTile from './LuxuryTile.vue'

    export default {
        props: ['player'],
        computed: {
            ...mapGetters([
                'phase',
                'selectedPlayerAndTile',
                'startPlayer',
                'activePlayer'
            ])
        },
        components: {
            luxuryTile: LuxuryTile,
            timeWheel: TimeWheel,
            playerIndustryTiles: PlayerIndustryTiles
        },
        methods: {
            hiLight(name, sel) {
                var cl = "nohilight";
                if (sel && name==sel.name && this.phase==2) {
                    cl = "hilight";
                } 
                if (this.startPlayer && this.startPlayer.name==this.player.name) {
                    cl = cl + " startplayer"
                }
                return cl
            }
        }
    }
</script>

<style scoped>

.player {
    border-style: inset;
    border-width: 2px;
    background-color: lightgrey;
    margin-bottom: 5px;
    margin-top: 5px;
}

.player-name {
    font-size: 2em;
    font-weight: 1000;
	float: left;
}

.startplayer {
    background-color: #ffb2c0;
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
