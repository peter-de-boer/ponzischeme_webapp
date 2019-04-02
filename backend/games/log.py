import copy

class Log(object):
    def __init__(self, players, advanced, id):
        # store two logs: log2 is meant for sotring hidden information
        # at the end of the game, log can be replaced by log2
        self.log = []
        self.log2 = []
        self.add("Game started.")
        self.add("Players in seat order: ")
        for index, player in enumerate(players):
            self.add(str(index+1) + " "  + player.name)

    def add(self, logtxt, log2txt=None):
        self.log.append(logtxt)
        if log2txt is not None:
            self.log2.append(log2txt)
        else:
            self.log2.append(logtxt)


    def replace(self, logtxt, log2txt=None):
        # replace the last entry by logtxt
        self.log[-1] = logtxt
        if log2txt is not None:
            self.log2[-1] = log2txt
        else:
            self.log2[-1] = logtxt

    def revealHiddenInfo(self):
        self.log = copy.deepcopy(self.log2)
