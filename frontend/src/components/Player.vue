<template>
    <div>
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
    export default {
        props: ['player'],
        components: {
            timeWheel: TimeWheel
        }
    }
</script>
