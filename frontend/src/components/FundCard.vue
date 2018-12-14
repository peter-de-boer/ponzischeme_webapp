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
    border-width: 0px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: center;
}

.hilight {
    box-shadow: 5px 5px 5px grey;
}

.nohilight {
    border-color: transparent;
}

.bear {
    background-image: linear-gradient(to right, #FAED95, #D46993);
}    

.start {
    background-image: linear-gradient(to right, #FAED95, lightblue);
}    

.normal {
    background-color: #FAED95;
}    

.value {
    font-size: 2em;
    font-weight: bold;
    text-shadow: -2px 0 white, 0 2px white, 2px 0 white, 0 -2px white;
}

.timeandinterest {
    display: flex;
    flex: 1;
    flex-direction: horizontal;
    justify-content: space-evenly;
    width: 100%;
    font-weight: bold;
}

.interest {
    text-shadow: -1px 0 white, 0 1px white, 1px 0 white, 0 -1px white;
}

.average {
    text-align: right;
    font-size: 0.5em;
}
</style>
