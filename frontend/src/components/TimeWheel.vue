<template>
    <div>
        <div class="row row-eq-height mb-1 custom-gutter">
            <div v-for="(cards, index) in wheel" class="col-2" :key="index + 'top'">
                <div class="timestep h-100">
                    <div class="row custom-gutter">
                        <div class="col-6 offset-2">
                            <div class="index mt-1 mb-2" :class="index==0 ? 'first' : ''">
                                {{index}}
                            </div>
                        </div>
                    </div>
                    <div v-for="card in cards">
                        <div class="interestline row my-1 mx-1 custom-gutter">
                            <div class="col-6 time">
                                <{{card.time}}> 
                            </div>
                            <div class="col-5 interest"> 
                                ${{card.interest}} 
                            </div>
                        </div> 
                    </div>
                </div>
            </div>
        </div>
        <!--
            <div v-for="(cards, index) in wheel" class="col-2" :key="index + 'top'">
                <span class="timestep">{{index}}</span>
            </div>
        </div>
        <hr>
        <div class="row custom-gutter">
            <div v-for="(cards, index) in wheel" class="col-2" :key="index + 'tot'">
                {{totalInterest(cards)}}
            </div>
        </div>
        <hr>
        <div v-for="row in maxLength()" class="row custom-gutter" :key="row + 'row'">
            <div v-for="(cards, index) in wheel" class="col-2" v-if="cardOnWheel(cards,row)" :key="index + row">
                {{cards[row-1].interest}} ({{cards[row-1].time}})
            </div>
            <div v-else class="col-2"></div>
        </div>
        -->
    </div>
</template>

<script>
    export default {
        props: ['wheel'],
        methods: {
            totalInterest(cards) {
                var total = 0;
                //debugger
                var i
                for (i in cards) {
                    total = total + cards[i].interest; 
                }
                return total
            },
            maxLength() {
                var max = 0
                for (var i in this.wheel) {
                    if (this.wheel[i].length > max) {
                        max = this.wheel[i].length
                    }
                }
                return max
            },
            cardOnWheel(cards,row) {
                return (row-1<cards.length)
            }
        }
    }
</script>

<style scoped>
.custom-gutter > [class*='col-'] {
    padding-right:2px;
    padding-left:2px;
}

.row {
    margin-left: 0;
    margin-right: 0;
}

.timestep {
    background-color: #1F3642;
}

.first {
    color: red;
}

.index {
    text-align: center;
    font-size: 1.5em; 
    font-weight: 1000;
    background-color: white;
}

.interestline {
    line-height: 1.0em;
    background-color: #FAED95;
    font-size: 0.8em; 
}

.interest {
    text-align: right;
}

.time {
    text-align: center;
}

</style>
