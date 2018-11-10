<template>
    <div>
        <div v-for="(cards,time) in wheel" :key="time">
            <div class="row">
                <div class="col-sm-2">
                    {{time}} {{totalInterest(cards)}}
                </div>
                <div class="col-sm-8">
                    <div v-for="card in cards" :key="card.value">
                       {{card.interest}} ({{card.time}})
                    </div>
                </div>
            </div>
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
            }
        }
    }
</script>
