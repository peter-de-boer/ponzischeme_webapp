<template>
	<div id="app">
		<app-game></app-game>
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
