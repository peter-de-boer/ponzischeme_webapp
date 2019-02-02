import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const auth = {
    state: {
        idToken: null,
        user: null,
        username: null,
        loginStatus: null,
        signupStatus: null
    },
    mutations: {
        loginStatus(state, loginStatus) {
            state.loginStatus = loginStatus.status
        },
        signupStatus(state, signupStatus) {
            state.signupStatus = signupStatus.status
        },
    authUser (state, userData) {
        state.idToken = userData.idToken
        state.username = userData.username
    },
    storeUser (state, user) {
        state.user = user
    },
    clearAuthData (state) {
        state.idToken = null
        state.userId = null
    }
    },
    actions: {
        setLogoutTimer ({commit}, expirationTime) {
            setTimeout(() => {
                commit('clearAuthData')
            }, expirationTime * 1000)
        },
        signup ({commit, dispatch}, authData) {
            console.log('in signup');
            axios.post('/user/signup', {
                email: authData.email,
                username: authData.username,
                password: authData.password,
                returnSecureToken: true
            })
            .then(res => {
                console.log('signup then')
                console.log(res)
                commit('signupStatus', res.data)
                //commit('authUser', {
                //  token: res.data.idToken,
                //  userId: res.data.userId
                //})
                //const now = new Date()
                //const expirationDate = new Date(now.getTime() + res.data.expiresIn * 1000)
                //localStorage.setItem('token', res.data.idToken)
                //localStorage.setItem('userId', res.data.userId)
                //localStorage.setItem('username', res.data.username)
                //localStorage.setItem('expirationDate', expirationDate)
                //dispatch('storeUser', authData)
                //dispatch('setLogoutTimer', res.data.expiresIn)
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
                console.log("login then")
                console.log(res)
                console.log(res.data.idToken)
                console.log(res.data.username)
                commit('loginStatus', res.data)
                localStorage.setItem('token', res.data.idToken)
                localStorage.setItem('username', res.data.username)
                commit('authUser', {
                    idToken: res.data.idToken,
                    username: res.data.username
                })
              })
              .catch(error => console.log(error))
        },
        tryAutoLogin ({commit}) {
            const token = localStorage.getItem('token')
            if (!token) {
                return
            }
            const expirationDate = localStorage.getItem('expirationDate')
            const now = new Date()
            if (now >= expirationDate) {
                return
            }
            const userId = localStorage.getItem('userId')
            commit('authUser', {
                token: token,
                userId: userId
            })
        },
        logout ({commit}) {
            commit('clearAuthData')
            localStorage.removeItem('token')
            localStorage.removeItem('username')
            router.replace('/signin')
        },
        storeUser ({commit, state}, userData) {
            if (!state.idToken) {
                return
            }
            axios.post('/users.json' + '?auth=' + state.idToken, userData)
                .then(res => console.log(res))
                .catch(error => console.log(error))
        },
        fetchUser ({commit, state}) {
            if (!state.idToken) {
                return
            }
            axios.get('/users.json' + '?auth=' + state.idToken)
                .then(res => {
                    console.log(res)
                    const data = res.data
                    const users = []
                    for (let key in data) {
                        const user = data[key]
                        user.id = key
                        users.push(user)
                    }
                    console.log(users)
                    commit('storeUser', users[0])
                })
                .catch(error => console.log(error))
        }
    },
    getters: {
        user (state) {
            return state.user
        },
        isAuthenticated (state) {
            return state.idToken !== null
        },
        loginStatus(state) {
            return state.loginStatus
        },
        signupStatus(state) {
            return state.signupStatus
        },
        token(state) {
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
        tradeMoney: null
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
        }
    },
    mutations: {
        clearSelections: (state) => {
            Vue.set(state, "selectedFundCard", {});
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
        }
    }    
}

export const store = new Vuex.Store({
    modules: {
        auth,
        selectPlayer,
        selectItems
    },
    state: {
        gameStateLoaded: 0,
        gameState: {}
    },
    getters: {
        tileName: () => (tile) => {
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
        currentIsActive: (state, getters) => {
            if (state.gameStateLoaded && getters.activePlayerName && getters.currentPlayer && 
                getters.activePlayerName == getters.currentPlayer.name ) {
                return "True";
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
        startPlayerName: state => {
            if (state.gameStateLoaded) {
                return state.gameState.players[state.gameState.status.start].name;
            } else {
                return null;
            }    
        },
        activePlayerName: state => {
            if (state.gameStateLoaded && !state.gameState.status.endOfGame) {
                return state.gameState.players[state.gameState.status.active[0]].name;
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
            commit('setGameState', payload);
            store.dispatch('clearSelections');
        }
    }    

});
