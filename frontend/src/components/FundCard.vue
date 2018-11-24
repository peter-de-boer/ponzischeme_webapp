<template>
    <div class="card"
         :class="[fundType(card.fundtype), hiLight(card,selectedFundCard)]" >
            <p>value: {{card.value}}</p>
            <p>time: {{card.time}}</p>
            <p>interest:{{card.interest}}</p>
            <!-- <p>fundtype:{{fundType(card.fundtype)}}</p> -->
            <p>average: {{card.averageInterestPerc.toFixed(2)}}</p>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';
    import {mapActions} from 'vuex';

    export default {
        props: ['card'],
        methods: {
            ...mapActions([
                'selectFundCard'
            ]),
            fundType(fundtype) {
                if (fundtype == "Starting Fund Card") {
                    return "start";
                } else if (fundtype == "Bear Fund Card") {
                    return "bear";
                } else {
                    return "normal";
                }    
            },
            hiLight(card, selected) {
                if (card.value==selected.value) {
                    return "hilight";
                } else {
                    return "nohilight";
                }
            }
        },
        computed: {
            ...mapGetters([
                'currentPlayer',
                'selectedFundCard',
                'gameStateLoaded'
            ])    
        }
    }    
</script>

<style scoped>

.card {
    border-style: inset;
    border-width: 2px;
}

.hilight {
}

.nohilight {
    border-color: transparent;
}

.bear {
    background-color: red;
}    

.start {
    background-color: lightblue;
}    

.normal {
    background-color: lightgray;
}    
</style>
