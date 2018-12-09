<template>
    <div>
        <div class="row small-gutter">
            <div v-for="(cards, index) in wheel" class="col-xs-2" :key="index + 'top'">
                {{index}}
            </div>
        </div>
        <hr>
        <div class="row small-gutter">
            <div v-for="(cards, index) in wheel" class="col-xs-2" :key="index + 'tot'">
                {{totalInterest(cards)}}
            </div>
        </div>
        <hr>
        <div v-for="row in maxLength()" class="row small-gutter" :key="row + 'row'">
            <div v-for="(cards, index) in wheel" class="col-xs-2" v-if="cardOnWheel(cards,row)" :key="index + row">
                {{cards[row-1].interest}} ({{cards[row-1].time}})
            </div>
            <div v-else class="col-xs-2"></div>
        </div>
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

<style>
.small-gutter > [class*='col-'] {
    padding-right:2px;
    padding-left:2px;
}

</style>
