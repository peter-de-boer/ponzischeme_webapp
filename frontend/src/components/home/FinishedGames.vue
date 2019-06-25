<template>
    <div>
        Finished Games <br>
        {{finishedGames}}
        <div v-for="(game, index) in finishedGames" :key="index">
            <finished-game :game="game"></finished-game>
        </div>
        <button @click="prevPage" :disabled="pageNumber==0">
            Previous
        </button>
        <button @click="nextPage" :disabled="pageNumber >= pageCount -1">
            Next
        </button>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import FinishedGame from './FinishedGame.vue';

    export default {
        data() { 
            return { 
                pageNumber: 0,  
                size: 10
            } 
        },
        methods: { 
            nextPage() { 
                this.pageNumber++; 
            }, 
            prevPage() { 
                this.pageNumber--; 
            } 
        },
        computed: {
            ...mapGetters([
                'finishedGames'
            ]),
            pageCount() { 
                let l = this.finishedGames.length, 
                    s = this.size; 
                return Math.ceil(l/s); 
            },
            paginatedData() { 
                const start = this.pageNumber * this.size, 
                      end = start + this.size; 
                console.log(this.finishedGames);
                return this.finishedGames.slice(start, end); 
            }
        },
        components: {
            finishedGame: FinishedGame
        }
    }    
</script>

<style scoped>
</style>
