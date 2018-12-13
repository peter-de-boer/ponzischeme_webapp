<template>
    <div class="card"
         :class="[fundType(card.fundtype), hiLight(card,selectedFundCard)]" >
            <p class="value">
                ${{card.value}}
            </p>
            <div class="timeandinterest">
                <div class="time">
                    <{{card.time}}>
                </div>
                <div class="interest">
                    ${{card.interest}}
                </div>
            </div>
            <!--
            <p class="average">
                {{card.averageInterestPerc.toFixed(2)}}
            </p>
            -->
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
                if (selected!=null && card.value==selected.value) {
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
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: center;
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

.value {
    font-size: 2em;
}

.timeandinterest {
    display: flex;
    flex: 1;
    flex-direction: horizontal;
    justify-content: space-evenly;
    width: 100%;
}

.average {
    text-align: right;
    font-size: 0.5em;
}
</style>
