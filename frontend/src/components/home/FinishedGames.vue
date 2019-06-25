<template>
    <div>
        Finished Games <br>
        <div v-for="(game, index) in paginatedData" :key="index">
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
                let l = (this.finishedGames == null ? 0 : this.finishedGames.length), 
                    s = this.size; 
                return Math.ceil(l/s); 
            },
            paginatedData() { 
                const start = this.pageNumber * this.size, 
                      end = start + this.size; 
                return (this.finishedGames==null ? null : this.finishedGames.slice(start, end)); 
            }
        },
        components: {
            finishedGame: FinishedGame
        }
    }    
</script>

<style scoped>
</style>
