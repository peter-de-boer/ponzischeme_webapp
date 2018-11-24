<template>
    <div class="player" :class="hiLight(player.name, selectedPlayerAndTile)">
        <player-industry-tiles :industryTiles="player.industryTiles" :name="player.name"></player-industry-tiles>
        <time-wheel :wheel="player.wheel"></time-wheel>
        <p>name:  {{player.name}} money: {{player.money}} </p>
        <hr>
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
                'selectedPlayerAndTile'
            ])
        },
        components: {
            timeWheel: TimeWheel,
            playerIndustryTiles: PlayerIndustryTiles
        },
        methods: {
            hiLight(name, sel) {
                if (sel && name==sel.name) {
                    return "hilight";
                } else {
                    return "nohilight";
                }
                    
            }
        }
    }
</script>

<style scoped>

.player {
    border-style: inset;
    border-width: 2px;
}

.hilight {
}

.nohilight {
    border-color: transparent;
}

</style>
