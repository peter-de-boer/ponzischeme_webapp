<template>
  <div>
    <h1>Game</h1>
  </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'Game',
        created() {
            console.log('created')
            axios.get('/game')
                .then(res => console.log(res))
                .catch(error => console.log(error))
        }
    }
</script>

<style scoped>
</style>
