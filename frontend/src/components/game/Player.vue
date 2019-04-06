<template>
    <div class="player" 
        :class="hiLight(player.name, selectedPlayerAndTile)">
        <p class="player-name">
            <span v-if="activePlayer && activePlayer.name==player.name"> 
               > 
            </span>
            {{player.name}}
        </p>
        <p class="moneyandpoints">
            <span class="money" >
                ${{player.money}} 
            </span>
            <br>
            <span class="points">
                points: {{tilesPoints()}}
                <span v-if="!advanced">  
                    (tot: {{totalPoints()}}) 
                </span>
            </span>
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
                'activePlayer',
                'advanced'
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
            },
            points(tiles) {
                return tiles*(tiles+1)/2
            },
            tilesPoints() {
                var p = 0;
                for (var i in this.player.industryTiles) {
                    p = p + this.points(this.player.industryTiles[i])
                }
                for (var i in this.player.luxuryTiles) {
                    p = p + this.player.luxuryTiles[i].points
                }
                return p
            },
            moneyPoints(money) {
                if (money < 30) {
                    return 0
                } else if (money < 56) {
                    return 1
                } else if (money < 78) {
                    return 2
                } else if (money < 96) {
                    return 3
                } else {
                    return 4
                }
            },
            totalPoints() {
                if (this.player.money === null) {
                    return "?"
                } else {
                    return this.tilesPoints() + this.moneyPoints(this.player.money)
                }
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

.moneyandpoints {
    font-size: 1.5em;
	float: right;
}

.money {
    font-weight: bold;
}

.points {
    font-style: italic;
}

.hilight {
}

.nohilight {
    border-color: transparent;
}

</style>
