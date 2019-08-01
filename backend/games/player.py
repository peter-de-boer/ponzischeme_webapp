from backend.games.fundCard import FundCard

class Player(object):
    def __init__(self, player):
        self.id = player['id']
        self.name = player['name']
        self.money = 0
        self.wheel =  [[],[],[],[],[],[]]
        self.bankrupt = False
        self.industryTiles = [0]*4
        self.luxuryTiles = []
        self.points = 0
        self.maxCardValue = 0

    def __eq__(self, other):
        return self.points==other.points and \
               self.maxCardValue == other.maxCardValue

    def __lt__(self, other):
        return self.points<other.points or \
               (self.points==other.points and \
                self.maxCardValue < other.maxCardValue)

    def identical(self, player):
        # returns true if player name and id is identical to self
        return (player and self.name==player['name'] and self.id==player['id'])

    def changeName(self, name):
        self.name = name

    def getMaxCardValue(self):
        maxValue = 0
        for cards in self.wheel:
            for card in cards:
                if card.value>maxValue:
                    maxValue = card.value
        return maxValue

    def selectCard(self, fundCard):
        self.money = self.money + fundCard.value
        self.wheel[fundCard.time].append(fundCard)

    def selectCardAndTile(self, fundCard, tile):
        self.industryTiles[tile]+=1
        self.selectCard(fundCard)

    def turnWheel(self, double=False):
        self.wheel.append(self.wheel.pop(0))
        if double:
            self.wheel[1].extend(self.wheel[0])
            self.wheel[0]= []
            self.wheel.append(self.wheel.pop(0))

    def payInterest(self, log, finance):
        interest = 0
        for card in self.wheel[0]:
            interest = interest + card.interest
        if interest > self.money:
            log.add(self.name + " cannot pay $" + str(interest) + \
                    " interest (only $" + str(self.money) + " left).")
            log.add(self.name + " is bankrupt.")
            finance.change(self.name, -self.money)
            self.money = 0
            self.bankrupt = True
        else:
            log.add(self.name + " pays $" + str(interest) + \
                    " interest.")
            finance.change(self.name, -interest)
            self.money = self.money - interest

    def moveFundCards(self):
        for card in self.wheel[0]:
            self.wheel[card.time].append(card)
        self.wheel[0] = []

    def canSell(self, tile):
        return self.industryTiles[tile] > 0

    def sell(self, tile, price):
        self.industryTiles[tile] -= 1
        self.money = self.money + price

    def canBuy(self, tile, price):
        return (self.industryTiles[tile] > 0) & (self.money >= price)

    def buy(self, tile, price):
        self.industryTiles[tile] += 1
        self.money = self.money - price

    def discardTile(self, tile):
        self.industryTiles[tile] -= 1

    def discardableTiles(self):
        discardable=[]
        maxTiles = max(self.industryTiles)
        if maxTiles > 0:
            for index, tiles in enumerate(self.industryTiles):
                if tiles==maxTiles:
                    discardable.append(index)
        return discardable

    def buyLuxuryTile(self, luxuryTile):
        self.luxuryTiles.append(luxuryTile)
        self.money -= luxuryTile.value

    def cashPoints(self):
        if self.money < 30:
            return 0
        elif self.money < 56:
            return 1
        elif self.money < 78:
            return 2
        elif self.money < 96:
            return 3
        else:
            return 4

    def luxuryTilePoints(self):
        points = 0
        for tile in self.luxuryTiles:
            points += tile.points
        return points

    def tilePoints(self):
        points = 0
        for tiles in self.industryTiles:
            points += (tiles*(tiles+1))/2
        return points

    def calculatePoints(self, advanced=False):
        if advanced:
            self.points = self.tilePoints() + self.luxuryTilePoints()
        else:
            self.points = self.tilePoints() + self.cashPoints()
        self.maxCardValue = self.getMaxCardValue()
