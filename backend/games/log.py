
class Log(object):
    def __init__(self, players, advanced, id):
        self.log = []
        self.add("Game started.")
        self.add("Players in seat order: ")
        for index, player in enumerate(players):
            self.add(str(index+1) + " "  + player.name)

    def add(self, logtxt):
        self.log.append(logtxt)

    def replace(self, logtxt):
        # replace the last entry by logtxt
        self.log[-1] = logtxt
