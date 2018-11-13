
class Status(object):
    def __init__(self, numPlayers, startPlayer=0):
        self.numPlayers = numPlayers
        self.start = startPlayer
        self.round = 0
        self.phase1Start()
        """
        phase:
            1: Pay The Interest
            2: Clandestine Trade
            3: Pass the Marker
            4: Market Crash
            5: Turn the Wheel
            6: Pay the Interest
        """

    def getPlayerOrder(self):
        """
        return a list of integers 0..numPlayer-1, rotated
        so that the startPlayer is the first in the list
        """
        order = list(range(self.numPlayers))
        for i in range(self.numPlayers):
            order[i]= (order[i] +  self.start)%self.numPlayers
        return(order)


    def phase1Start(self):
        self.round += 1
        self.phase = 1
        self.active = self.getPlayerOrder()
        self.opponent = None

    def phase2Start(self):
        self.phase = 2
        self.active = self.getPlayerOrder()
        self.opponent = None

    def phase3Start(self):
        self.phase = 3
        self.start = (self.start+1)%self.numPlayers
        self.active = [self.start]
        self.opponent = None

    def phase4Start(self):
        self.phase = 4
        return

    def phase5Start(self):
        self.phase = 5
        return

    def phase6Start(self):
        self.phase = 6
        return

    def next(self):
        if self.phase==1:
            del self.active[0]
            if len(self.active)==0:
                self.phase2Start()
        if self.phase==2:
            del self.active[0]
            if len(self.active)==0:
                self.phase3Start()
