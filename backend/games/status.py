
class Status(object):
    def __init__(self, numPlayers, startPlayer=0):
        self.numPlayers = numPlayers
        self.phase = 1
        self.start = startPlayer
        self.active = self.getPlayerOrder()
        self.opponent = None
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
        self.phase1 = 1
        self.active = getPlayerOrder()
        self.opponent = None

    def phase2Start(self):
        self.phase1 = 2
        self.active = getPlayerOrder()
        self.opponent = None

    def next():
        if self.phase==1:
            del self.active[0]
            if len(self.active)==0:
                phase2Start()
        if self.phase==2:
            del self.active[0]
            if len(self.active)==0:
                phase3Start()
