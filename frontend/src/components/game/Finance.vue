<template>
    <div class="finance">
        <div class="row">
            <div class="col-12">
                <h2> Finance Help </h2>
            </div>
            <div class="col-12">
                <table>
                    <tr>
                        <!-- <th v-for="money,player in finance.money">{{player}}</th> -->
                        <!-- 
                            loop over players instead of over finance,money because
                            players is an (ordered) list and 
                            finance.money is an (unordered) dictionary
                        -->
                        <th v-for="player in players">{{player.name}}</th>
                    </tr>
                    <tr>
                        <!-- <td v-for="money in finance.money">${{money}}</td> -->
                        <td v-for="player in players">
                            {{finance.money[player.name]}}
                        </td>
                        <td>{{commentMoney()}}</td>
                    </tr>
                    <tr v-for="trade in finance.trades">
                        <!-- <td v-for="money,player in finance.money"> -->
                        <td v-for="player in players">
                            {{tradeValue(trade,player.name)}}
                        </td>
                    </tr>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';

    export default {
        computed: {
            ...mapGetters([
                'gameStateLoaded',
                'gameEnded',
                'advanced',
                'players',
                'finance'
            ])
        },
        methods: {
            tradeValue(trade, player) {
                if (trade.playerA == player) {
                    return trade.valueA
                } else if (trade.playerB == player) {
                    return trade.valueB
                } else {
                    return ""
                }
            },
            commentMoney() {
                var commentString = "=> includes fundings, paid interests and known trades; excludes unknown trades"
                if (this.gameEnded && !this.advanced) { 
                    commentString = "=> includes fundings and paid interests; excludes all trades"
                } else if (this.gameEnded && this.advanced) {
                    commentString = "=> includes fundings, bought luxuruy tiles and paid interests; excludes all trades"
                } else if (!this.gameEnded && this.advanced) {
                    commentString = "=> includes fundings, bought luxury tiles, paid interests and known trades; excludes unknown trades"
                }
                return commentString
            }
        }
    }    
</script>

<style scoped>
.finance {
    border-style: solid;
}

table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>
