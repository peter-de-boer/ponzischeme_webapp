<template>
    <div>
        <player-industry-tiles :industryTiles="player.industryTiles" :name="player.name"></player-industry-tiles>
        <time-wheel :wheel="player.wheel"></time-wheel>
        <p>name:  {{player.name}} </p>
        <p>money: {{player.money}} </p>
        <p>tiles: {{player.industryTiles}} </p>
        <p>bankrupt: {{player.bankrupt}} </p>
        <hr>
    </div>
</template>

<script>
    import TimeWheel from './TimeWheel.vue'
    import PlayerIndustryTiles from './PlayerIndustryTiles.vue'
    export default {
        props: ['player'],
        components: {
            timeWheel: TimeWheel,
            playerIndustryTiles: PlayerIndustryTiles
        }
    }
</script>
