import copy

class Log(object):
    def __init__(self, players, advanced, id):
        # store two logs: log2 is meant for storing hidden information
        # at the end of the game, log can be replaced by log2
        # plus one for each player, showing the trades he was involved in
        self.log = []
        self.log2 = []
        self.playerNames = [p.name for p in players]
        self.playerLog = [[] for p in players]
        self.add("Game started.")
        self.add("Players in seat order: ")
        for index, player in enumerate(players):
            self.add(str(index+1) + " "  + player.name)

    def add(self, logtxt, log2txt=None, involvedPlayers=None):
        self.log.append(logtxt)
        if log2txt is not None:
            self.log2.append(log2txt)
            for playerName, playerLog in zip(self.playerNames, self.playerLog):
                if playerName in involvedPlayers:
                    playerLog.append(log2txt)
                else:
                    playerLog.append(logtxt)
        else:
            self.log2.append(logtxt)
            for playerLog in self.playerLog:
                playerLog.append(logtxt)

    def replace(self, logtxt, log2txt=None, involvedPlayers=None):
        # replace the last entry by logtxt
        self.log[-1] = logtxt
        if log2txt is not None:
            self.log2[-1] = log2txt
            for playerName, playerLog in zip(self.playerNames, self.playerLog):
                if playerName in involvedPlayers:
                    playerLog[-1] = log2txt
                else:
                    playerLog[-1] = logtxt
        else:
            self.log2[-1] = logtxt
            for playerLog in self.playerLog:
                playerLog[-1] = logtxt

    def revealHiddenInfo(self):
        self.log = copy.deepcopy(self.log2)

    def showKnownInfo(self, playerInfo):
        for playerName, playerLog in zip(self.playerNames, self.playerLog):
            if playerName == playerInfo['name']:
                self.log = playerLog
