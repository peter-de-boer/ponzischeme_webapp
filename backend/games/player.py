from backend.games.fundCard import FundCard

class Player(object):
    def __init__(self, player):
        self.id = player['id']
        self.name = player['name']
        self.money = 0
        self.wheel =  [[],[],[],[],[],[]]
        self.bankrupt = False
        self.industryTiles = [0]*4
        self.start = False
        self.active = False

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

    def payInterest(self):
        interest = 0
        for card in self.wheel[0]:
            interest = interest + card.interest
        if interest > self.money:
            self.money = 0
            self.bankrupt = True
        else:
            self.money = self.money - interest

    def moveFundCards(self):
        for card in self.wheel[0]:
            self.wheel[card.time].append(card)
        self.wheel[0] = []

    def canSell(tile):
        return self.industryTiles[tile] > 0

    def sell(tile,price):
        self.industryTiles[tile] -= 1
        self.money = self.money + price

    def canBuy(tile, price):
        return (self.industryTiles[tile] > 0) & (self.money >= price)

    def buy(tile, price):
        self.industryTiles[tile] += 1
        self.money = self.money - price

    def discardTile(tile):
        self.industryTiles[tile] -= 1

    def discardableTiles():
        discardable=[]
        maxTiles = max(this.industryTiles)
        if maxTiles > 0:
            for tile in this.industryTiles:
                if this.industryTile[tile]==maxTiles:
                    discardable.append(tile)
        return discardable
