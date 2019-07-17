from backend.games.tradeOffer import TradeOffer

class Status(object):
    def __init__(self, numPlayers, players, log):
        self.numPlayers = numPlayers
        # only store players name, for logging purposes
        self.players = [""]*numPlayers
        for i in range(numPlayers):
            self.players[i] = players[i].name
        self.start = 0
        self.round = 0
        self.endOfGame = False
        self.marketCrash = False
        self.tradeOffer = None
        self.log = log
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

    def setEndOfGame(self):
        """
        set end of game status
        and set the properties so that the frontend does not break
        """
        self.endOfGame = True

    @staticmethod
    def phaseStyle(phase):
        return "<span style='font-weight: bold'>Phase: " + phase + "</span>"

    def phase1Start(self):
        self.round += 1
        self.phase = 1
        self.active = self.getPlayerOrder()
        self.log.add("<span style='font-style: italic'>*** Round " + \
                     str(self.round) + " ***</span>")
        self.log.add(self.phaseStyle("Funding"))

    def phase2Start(self):
        self.log.add(self.phaseStyle("Clandestine Trading"))
        if self.round == 1:
            self.log.add("Clandestine Trading Phase is skipped in Round 1.")
            self.phase3Start()
        else:
            self.phase = 2
            self.active = self.getPlayerOrder()
            self.tradeOffer = None

    def phase2SetTrade(self, tile, money, offeringPlayerIndex, opponentIndex):
        self.tradeOffer = TradeOffer(tile, money, offeringPlayerIndex, opponentIndex)
        self.active.insert(0, opponentIndex)

    def phase2RemoveTrade(self):
        self.tradeOffer = None
        del self.active[0]

    def phase3Start(self):
        self.phase = 3
        self.start = (self.start+1)%self.numPlayers
        self.active = [self.start]
        self.log.add(self.phaseStyle("Pass the Start Player Marker"))
        self.log.add(self.players[self.start] + " is the new start player.")

    def phase4Start(self):
        self.phase = 4
        self.log.add(self.phaseStyle("Market Crash"))
        return

    def phase4SetMarketCrash(self):
        self.marketCrash = True
        self.active = self.getPlayerOrder()

    def phase5Start(self):
        self.phase = 5
        self.log.add(self.phaseStyle("Turn the Wheel"))
        return

    def phase6Start(self):
        self.phase = 6
        self.log.add(self.phaseStyle("Pay the Interest"))
        return

    def next(self):
        if self.phase==1:
            del self.active[0]
            if len(self.active)==0:
                self.phase2Start()
        elif self.phase==2:
            del self.active[0]
            if len(self.active)==0:
                self.phase3Start()
        elif self.phase==3:
            del self.active[0]
            if len(self.active)==0:
                self.phase4Start()
        elif self.phase==4:
            if (self.marketCrash):
                del self.active[0]
                if len(self.active)==0:
                    self.phase5Start()
            else:
                self.phase5Start()
        elif self.phase==5:
            self.marketCrash = False
            self.phase6Start()
        elif self.phase==6:
            self.phase1Start()
