<template>
    <div class="blue"
         :class="fundType(card.fundtype)">
        <p>value: {{card.value}}</p>
        <p>time: {{card.time}}</p>
        <p>interest:{{card.interest}}</p>
        <!-- <p>fundtype:{{fundType(card.fundtype)}}</p> -->
        <p>average: {{card.averageInterestPerc.toFixed(2)}}</p>
    </div>
</template>

<script>
    export default {
        props: ['card'],
        methods: {
            fundType(fundtype) {
                if (fundtype == "Starting Fund Card") {
                    return "start";
                } else if (fundtype == "Bear Fund Card") {
                    return "bear";
                } else {
                    return "normal";
                }    
            }
        }
    }    
</script>

<style scoped>

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
