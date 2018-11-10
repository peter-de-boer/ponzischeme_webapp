import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const selectPlayer = {
    state: {
        currentPlayer: {}
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

export const store = new Vuex.Store({
    modules: {
        selectPlayer
    },
    state: {
        gameStateLoaded: 0,
        gameState: {}
    },
    getters: {
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
