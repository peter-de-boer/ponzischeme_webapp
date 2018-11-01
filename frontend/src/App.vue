<template>
	<div id="app">
        <h1>Top page</h1>
        <router-view></router-view>
	</div>
</template>

<script>
import Game from './components/Game.vue'

export default {
  name: 'app',
  components: {
    appGame: Game
  }
}
</script>

<style>
</style>
