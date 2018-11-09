<template>
    <div>
        <p>name:  {{player.name}} </p>
        <p>money: {{player.money}} </p>
        <p>wheel: {{player.wheel}} </p>
        <p>tiles: {{player.industryTiles}} </p>
        <p>bankrupt: {{player.bankrupt}} </p>
        <p>start: {{player.start}} </p>
        <p>active: {{player.active}} </p>
        <hr>
    </div>
</template>

<script>
    export default {
        props: ['player']
    }
</script>
