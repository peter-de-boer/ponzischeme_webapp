import copy

class Finance(object):
    def __init__(self, players, dummy = False):
        #  finance overview
        # store:
        #                   money                       trades
        # financePublic   fun/int/lux                var.
        # financeSecret   fun/int/lux                real values
        # finance[plr]   fun/int/lux/known trades    var. for unknown trades
        #
        # finance[plr]:  show to plr during the game
        # financePublic: show to other players/viewers during the game
        # financeSecret: show to all after the game
        #
        # dummy is used for old and running games
        #
        self.dummy = dummy
        if dummy:
            self.finance = None
        else:
            self.players = [p.name for p in players]
            self.finance = {}
            self.tradeCount = 0
            for player in players:
                self.finance[player.name] = {}
                self.finance[player.name]['trades'] = []
                self.finance[player.name]['money'] = {}
                for player2 in players:
                    self.finance[player.name]['money'][player2.name]= 0
            self.financePublic = {}
            self.financePublic['trades'] = []
            self.financePublic['money'] = {}
            for player2 in players:
                self.financePublic['money'][player2.name]= 0
            self.financeSecret = {}
            self.financeSecret['trades'] = []
            self.financeSecret['money'] = {}
            for player2 in players:
                self.financeSecret['money'][player2.name]= 0

    def change(self, playerName, value, player2Name = None):
        # changes the money of player
        # if player2Name is None, then this is public information
        # else only known to player2Name
        if not self.dummy:
            if player2Name is None:
                self.financePublic['money'][playerName] += value
                self.financeSecret['money'][playerName] += value
                for p in self.players:
                    self.finance[p]['money'][playerName] += value
            else:
                self.finance[player2Name]['money'][playerName] += value


    def trade(self, playerA, playerB, value):
        # assumption: value is positive, playerA pays value to playerB
        # the value is only known to playerA and playerB
        # add this trade to the trade lists of the other players
        # change the money for player A and playerB
        if not self.dummy:
            self.change(playerA, -value, playerA)
            self.change(playerA, -value, playerB)
            self.change(playerB,  value, playerA)
            self.change(playerB,  value, playerB)
            self.tradeCount += 1
            plustrade = '+t' + str(self.tradeCount)
            mintrade =  '-t' + str(self.tradeCount)
            trade = {}
            trade['playerA'] = playerA
            trade['playerB'] = playerB
            trade['valueA'] = mintrade
            trade['valueB'] = plustrade
            self.financePublic['trades'].append(trade)
            for p in self.players:
                if p != playerA and p!= playerB:
                    self.finance[p]['trades'].append(trade)
            realtrade = {}
            realtrade['playerA'] = playerA
            realtrade['playerB'] = playerB
            realtrade['valueA'] = -value
            realtrade['valueB'] = +value
            self.financeSecret['trades'].append(realtrade)

    def hideHiddenInfo(self, playerInfo):
        if not self.dummy:
            self.financeSecret = None
            if playerInfo['name'] in self.finance:
                self.finance = self.finance[playerInfo['name']]
            else:
                self.finance = self.financePublic

    def revealHiddenInfo(self):
        if not self.dummy:
            self.finance = self.financeSecret
