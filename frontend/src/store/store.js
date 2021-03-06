import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import router  from '../routes';

Vue.use(Vuex);

const auth = {
    state: {
        idToken: null,
        username: null,
        email: null,
        authenticated: null
    },
    mutations: {
        authUser (state, userData) {
            Vue.set(state, "idToken", userData.idToken);
            Vue.set(state, "username", userData.username);
            Vue.set(state, "authenticated", "success");
        },
        clearAuthData (state) {
            Vue.set(state, "idToken", null);
            Vue.set(state, "username", null);
            Vue.set(state, "authenticated", null);
        },
        setAuthStatus (state, authStatus) {
            Vue.set(state, "authenticated", authStatus);
        },
        accountData (state, data) {
            Vue.set(state, "email", data.email)
        }
    },
    actions: {
        clearAuthData ({commit}) {
            commit('clearAuthData')
            localStorage.removeItem('token')
            localStorage.removeItem('username')
        },
        signup ({commit, dispatch}, authData) {
            axios.post('/user/signup', {
                email: authData.email,
                username: authData.username,
                password: authData.password,
                returnSecureToken: true,
                url: location.origin
            })
            .then(res => {
            })
            .catch(error => console.log(error))
        },
        login ({commit, dispatch}, authData) {
            axios.post('/user/login', {
                username: authData.username,
                password: authData.password,
                returnSecureToken: true
            })
            .then(res => {
                console.log(res.data);
                if (res.data.status=="authenticated") {
                    localStorage.setItem('token', res.data.idToken)
                    localStorage.setItem('username', res.data.username)
                    commit('authUser', {
                        idToken: res.data.idToken,
                        username: res.data.username
                    })
                    router.replace({name: 'home'})
                } else {
                    commit('setAuthStatus', 'failed');
                }
              })
              .catch(error => console.log(error))
        },
        clearFailedStatus({commit}) {
            commit('setAuthStatus', null);
        },
        tryAutoLogin ({commit}) {
            const token = localStorage.getItem('token')
            if (!token) {
                return
            }
            //const expirationDate = localStorage.getItem('expirationDate')
            //const now = new Date()
            //if (now >= expirationDate) {
            //    return
           // }
            const username = localStorage.getItem('username')
            commit('authUser', {
                idToken: token,
                username: username
            })
        },
        logout ({commit}) {
            commit('clearAuthData')
            localStorage.removeItem('token')
            localStorage.removeItem('username')
            router.replace({name: 'login'})
        },
        fetchUser ({commit, dispatch, state}) {
            if (!state.idToken) {
                return
            }
            var json = {"token": state.idToken}
            axios.put('/user/account', json)
                .then(res => {
                    if (res.data.status=="success") {
                        commit('accountData', {
                            email: res.data.email
                        })
                    } else {
                        dispatch('clearAuthData');
                    }
                })
                .catch(error => console.log(error))
        }
    },
    getters: {
        isAuthenticated (state) {
            return state.idToken !== null
        },
        authFailed (state) {
            return state.authenticated == "failed"
        },
        username(state) {
            return state.username
        },
        email(state) {
            return state.email
        },
        token(state) {
            return state.idToken
            //return localStorage.getItem('token')
        },
        tokenStorage() {
            return localStorage.getItem('token')
        }
    }
}

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
        selectedFundCard: null,
        selectedPlayerAndTile: null,
        selectedIndustryTile: null,
        selectedLuxuryTile: null,
        selectedOpponentName: null,
        tradeMoney: null,
        showFullFundCards: false
    },
    getters: {
        tradeMoney: state => {
            return state.tradeMoney;
        },
        selectedOpponentName: state => {
            return state.selectedOpponentName;
        },
        selectedPlayerAndTile: state => {
            return state.selectedPlayerAndTile;
        },
        selectedIndustryTile: state => {
            return state.selectedIndustryTile;
        },
        selectedLuxuryTile: state => {
            return state.selectedLuxuryTile;
        },
        selectedFundCard: state => {
            return state.selectedFundCard;
        },
        showFullFundCards: state => {
            return state.showFullFundCards;
        }
    },
    mutations: {
        clearSelections: (state) => {
            Vue.set(state, "selectedFundCard", null);
            Vue.set(state, "selectedPlayerAndTile", null);
            Vue.set(state, "selectedIndustryTile", null);
            Vue.set(state, "selectedLuxuryTile", null);
            Vue.set(state, "selectedOpponentName", null);
            Vue.set(state, "tradeMoney", null);
        },    
        setTradeMoney: (state, payload) => {
            Vue.set(state, "setTradeMoney", payload);
        },    
        selectOpponentName: (state, payload) => {
            Vue.set(state, "selectedOpponentName", payload);
        },    
        selectPlayerAndTile: (state, payload) => {
            Vue.set(state, "selectedPlayerAndTile", payload);
        },    
        selectIndustryTile: (state, payload) => {
            Vue.set(state, "selectedIndustryTile", payload);
        },    
        selectLuxuryTile: (state, payload) => {
            Vue.set(state, "selectedLuxuryTile", payload);
        },    
        selectFundCard: (state, payload) => {
            Vue.set(state, "selectedFundCard", payload);
        },    
        switchShowFullFundCards: (state, payload) => {
            Vue.set(state, "showFullFundCards", payload);
        }    
    },
    actions: {
        clearSelections: ({ commit }) => {
            commit('clearSelections')
        },
        setTradeMoney: ({ commit }, payload) => {
            commit('setTradeMoney', payload)
        },
        selectOpponentName: ({ commit }, payload) => {
            commit('selectOpponentName', payload)
        },
        selectPlayerAndTile: ({ commit }, payload) => {
            commit('selectPlayerAndTile', payload)
        },
        selectIndustryTile: ({ commit }, payload) => {
            commit('selectIndustryTile', payload)
        },
        selectLuxuryTile: ({ commit }, payload) => {
            commit('selectLuxuryTile', payload)
        },
        selectFundCard: ({ commit }, payload) => {
            commit('selectFundCard', payload)
        },
        switchShowFullFundCards: ({ commit, getters }) => {
            commit('switchShowFullFundCards', !getters.showFullFundCards)
        }
    }    
}

const games = {
    state: {
        newGames: null,
        runningGames: null,
        finishedGames: null
    },
    getters: {
        newGames: state => {
            return state.newGames;
        },
        runningGames: state => {
            return state.runningGames;
        },
        finishedGames: state => {
            return state.finishedGames;
        }
    },
    mutations: {
        setNewGames: (state, payload) => {
            Vue.set(state, "newGames", payload);
        },    
        setRunningGames: (state, payload) => {
            Vue.set(state, "runningGames", payload);
        },    
        setFinishedGames: (state, payload) => {
            Vue.set(state, "finishedGames", payload);
        }
    },
    actions: {
        setGameList: ({ commit, dispatch }, data) => {
            // data is a json array with two elements
            // first is authentication data, second the game list
            if (!data[0].name) {
                // apparently an invalid or expired token was provided
                dispatch('clearAuthData')
            }
            var games = data[1];
            commit('setNewGames', games['new']);
            commit('setRunningGames', games['running']);
            commit('setFinishedGames', games['finished'].slice().reverse());
        },
        doListAction: ({commit, dispatch}, {route, json}) => {
            dispatch('loadingOn');
            axios.put(route, json)
                .then( res => {
                    dispatch('setGameList', res.data)
                })
                .catch( error => {
                    console.log(error)
                })
                .then(() => {
                    dispatch('loadingOff');
                }); 
        }
    }    
}

const mainchat = {
    state: {
        mainChat: []
    },
    getters: {
        mainChat: state => {
            return state.mainChat;
        }
    },
    mutations: {
        setMainChat: (state, payload) => {
            Vue.set(state, "mainChat", payload);
        }
    },
    actions: {
        setMainChat: ({ commit, dispatch }, data) => {
            // data is a json array with two elements
            // first is authentication data, second the chat
            if (!data[0].name) {
                // apparently an invalid or expired token was provided
                dispatch('clearAuthData')
            }
            commit('setMainChat', data[1]);
        }
    }    
}

export const store = new Vuex.Store({
    modules: {
        mainchat,
        games,
        auth,
        selectPlayer,
        selectItems
    },
    state: {
        gameStateLoaded: 0,
        gameState: {},
        gameChat: [],
        gameNotes: "",
        loading: false,
    },
    getters: {
        loading: state => {
            return state.loading;
        },
        tileName: () => (tile) => {
            switch(tile) {
                case 0:
                    return "transportation(blue)";
                case 1:
                    return "grain(yellow)";
                case 2:
                    return "media(green)";
                case 3:
                    return "real estate(red)";
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
        userIsActive: (state, getters) => {
            if (state.gameStateLoaded && getters.activePlayer && 
                getters.activePlayer.name && getters.username && 
                getters.activePlayer.name == getters.username ) {
                return "True";
            } else {
                return null;
            }
        },
        userIsPlayer: (state, getters) => {
            if (state.gameStateLoaded && getters.username) {
                var plrs = getters.players;
                for (var plrIndex in plrs) {
                    if (plrs[plrIndex].name==getters.username) {
                        return "True";
                    }
                }
                return null;
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
        id: state => {
            if (state.gameStateLoaded) {
                return state.gameState.id;
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
                return state.gameState.players[state.gameState.status.start];
            } else {
                return null;
            }    
        },
        activePlayer: state => {
            if (state.gameStateLoaded && !state.gameState.status.endOfGame) {
                return state.gameState.players[state.gameState.status.active[0]];
            } else {
                return null;
            }    
        },
        luxuryTiles: state => {
            if (state.gameStateLoaded) {
                return state.gameState.luxuryTiles;
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
        advanced: state => {
            if (state.gameStateLoaded) {
                return state.gameState.advanced;
            } else {
                return null;
            }
        },
        finance: state => {
            if (state.gameStateLoaded && state.gameState.finance) {
                return state.gameState.finance.finance;
            } else {
                return null;
            }
        },
        gameNotes: state => {
            return state.gameNotes;
        },    
        gameChat: state => {
            return state.gameChat;
        },    
        gameStateLoaded: state => {
            return state.gameStateLoaded;
        }    
    },
    mutations: {
        loading: (state, param) => {
            Vue.set(state, "loading", param);
        },    
        setGameState: (state, data) => {
            Vue.set(state, "gameState", data);
            state.gameStateLoaded = 1;
        },    
        setGameChat: (state, data) => {
            Vue.set(state, "gameChat", data);
        },    
        setGameNotes: (state, data) => {
            Vue.set(state, "gameNotes", data);
        }    
    },
    actions: {
        loadingOn: ({commit}) => {
            commit('loading', true);
        },
        loadingOff: ({commit}) => {
            commit('loading', false);
        },
        setGameState: ({ commit, dispatch }, data) => {
            // data is a json array with several elements
            // 0: authentication data
            // 1: game state
            // 2: chat
            // 3: notes
            if (!data[0].name) {
                // apparently an invalid or expired token was provided
                dispatch('clearAuthData')
                localStorage.removeItem('username')
            }
            commit('setGameNotes', data[3]);
            commit('setGameChat',  data[2]);
            commit('setGameState', data[1]);
            store.dispatch('clearSelections');
        },
        setGameNotes: ({commit}, data) => {
            commit('setGameNotes', data);
        },
        doAction: ({commit, dispatch}, {route, json}) => {
            dispatch('loadingOn');
            axios.put(route, json)
                .then( res => {
                    if (res.data[1].error) {
                    } else {
                        dispatch('setGameState', res.data)
                        //this.clearSelections()
                    }
                })
                .catch(  error => {
                    console.log(error)
                })
                .then(() => {
                    dispatch('loadingOff');
                }); 
        }
    }    

});
