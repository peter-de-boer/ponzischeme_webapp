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
        selectedIndustryTile: null
    },
    getters: {
        selectedIndustryTile: state => {
            return state.selectedIndustryTile;
        },
        selectedFundCard: state => {
            return state.selectedFundCard;
        }
    },
    mutations: {
        selectIndustryTile: (state, payload) => {
            Vue.set(state, "selectedIndustryTile", payload);
        },    
        selectFundCard: (state, payload) => {
            Vue.set(state, "selectedFundCard", payload);
        }    
    },
    actions: {
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
        isPhase1: state => {
            if (state.gameStateLoaded) {
                return state.gameState.status.phase==1;
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
            if (state.gameStateLoaded) {
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
