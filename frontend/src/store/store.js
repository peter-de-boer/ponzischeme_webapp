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
        selectedOpponent: {},
        tradeMoney: null
    },
    getters: {
        tradeMoney: state => {
            return state.tradeMoney;
        },
        selectedOpponent: state => {
            return state.selectedOpponent;
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
        selectOpponent: (state, payload) => {
            Vue.set(state, "selectedOpponent", payload);
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
        selectOpponent: ({ commit }, payload) => {
            commit('selectOpponent', payload)
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
