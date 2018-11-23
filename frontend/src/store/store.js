import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const selectPlayer = {
    state: {
        currentPlayer: null
    },
    getters: {
        currentPlayer: state => {
            return state.currentPlayer;
        }
    },
    mutations: {
        selectCurrentPlayer: (state, payload) => {
            Vue.set(state, "currentPlayer", payload);
        }    
    },
    actions: {
        selectCurrentPlayer: ({ commit }, payload) => {
            commit('selectCurrentPlayer', payload)
        }
    }    
}

const selectItems = {
    state: {
        selectedFundCard: {},
        selectedIndustryTile: null,
        selectedOpponentName: null,
        tradeMoney: null
    },
    getters: {
        tradeMoney: state => {
            return state.tradeMoney;
        },
        selectedOpponentName: state => {
            return state.selectedOpponentName;
        },
        selectedIndustryTile: state => {
            return state.selectedIndustryTile;
        },
        selectedFundCard: state => {
            return state.selectedFundCard;
        }
    },
    mutations: {
        setTradeMoney: (state, payload) => {
            Vue.set(state, "setTradeMoney", payload);
        },    
        selectOpponentName: (state, payload) => {
            Vue.set(state, "selectedOpponentName", payload);
        },    
        selectIndustryTile: (state, payload) => {
            Vue.set(state, "selectedIndustryTile", payload);
        },    
        selectFundCard: (state, payload) => {
            Vue.set(state, "selectedFundCard", payload);
        }    
    },
    actions: {
        setTradeMoney: ({ commit }, payload) => {
            commit('setTradeMoney', payload)
        },
        selectOpponentName: ({ commit }, payload) => {
            commit('selectOpponentName', payload)
        },
        selectIndustryTile: ({ commit }, payload) => {
            commit('selectIndustryTile', payload)
        },
        selectFundCard: ({ commit }, payload) => {
            commit('selectFundCard', payload)
        }
    }    
}

export const store = new Vuex.Store({
    modules: {
        selectPlayer,
        selectItems
    },
    state: {
        gameStateLoaded: 0,
        gameState: {}
    },
    getters: {
        tileName: (state) => (tile) => {
            switch(tile) {
                case 0:
                    return "transportation";
                case 1:
                    return "grain";
                case 2:
                    return "media";
                case 3:
                    return "real estate";
                default:
                    return "<unknown>";
            }
        },
        playerName: (state) =>  (playerIndex) => {
            if (state.gameStateLoaded) {
                return state.gameState.players[playerIndex].name;
            } else {
                return null;
            }
        },
        tradeOffer: (state, getters) => {
            if (state.gameStateLoaded) {
                if (state.gameState.status.tradeOffer) {
                    return {
                        tileName: getters.tileName(state.gameState.status.tradeOffer.tile),
                        tradeMoney: (state.gameState.status.tradeOffer.money || "some money"),
                        offeringPlayerName: getters.playerName(state.gameState.status.tradeOffer.offeringPlayerIndex),
                        opponentName:       getters.playerName(state.gameState.status.tradeOffer.opponentIndex)
                    }
                } else {
                    return null
                }
            } else {
                return null;
            }    
        },
        log: state => {
            if (state.gameStateLoaded) {
                return state.gameState.log.log;
            } else {
                return null;
            }    
        },
        round: state => {
            if (state.gameStateLoaded) {
                return state.gameState.status.round;
            } else {
                return null;
            }    
        },
        phase: state => {
            if (state.gameStateLoaded) {
                return state.gameState.status.phase;
            } else {
                return null;
            }    
        },
        startPlayer: state => {
            if (state.gameStateLoaded) {
                return state.gameState.players[state.gameState.status.start].name;
            } else {
                return null;
            }    
        },
        activePlayer: state => {
            if (state.gameStateLoaded && !state.gameState.status.endOfGame) {
                return state.gameState.players[state.gameState.status.active[0]].name;
            } else {
                return null;
            }    
        },
        industryTiles: state => {
            if (state.gameStateLoaded) {
                return state.gameState.industryTiles;
            } else {
                return null;
            }    
        },
        fundDeck: state => {
            if (state.gameStateLoaded) {
                return state.gameState.fundDeck;
            } else {
                return null;
            }    

        },
        discardPile: state => {
            if (state.gameStateLoaded) {
                return state.gameState.discardPile;
            } else {
                return null;
            }    

        },
        fundingBoard: state => {
            if (state.gameStateLoaded) {
                return state.gameState.fundingBoard.board;
            } else {
                return null;
            }    

        },
        players: state => {
            if (state.gameStateLoaded) {
                return state.gameState.players;
            } else {
                return null;
            }    
        },    
        gameEnded: state => {
            if (state.gameStateLoaded) {
                return state.gameState.status.endOfGame;
            } else {
                return null;
            }
        },
        gameStateLoaded: state => {
            return state.gameStateLoaded;
        }    
    },
    mutations: {
        setGameState: (state, payload) => {
            Vue.set(state, "gameState", payload);
            state.gameStateLoaded = 1;
        }    
    },
    actions: {
        setGameState: ({ commit }, payload) => {
            commit('setGameState', payload)
        }
    }    

});
