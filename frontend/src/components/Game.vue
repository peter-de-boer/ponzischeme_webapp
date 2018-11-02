<template>
  <div>
    <h1>Game</h1>
    <funding-board></funding-board>
  </div>
</template>

<script>
    import axios from 'axios';
    import Board from './FundingBoard.vue';

    export default {
        name: 'Game',
        created() {
            console.log('created')
            axios.get('/game')
                .then(res => console.log(res))
                .catch(error => console.log(error))
        },
        components: {
            fundingBoard: Board
        }

    }
</script>

<style scoped>
</style>
