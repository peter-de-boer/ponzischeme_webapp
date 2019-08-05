import json
from backend.games.luxuryTile import LuxuryTile
from backend.games.fundCard import FundCard
from backend.games.fundingBoard import FundingBoard
from backend.games.player import Player
from backend.games.status import Status
from backend.games.log import Log
from backend.games.finance import Finance
from random import shuffle
import sys

class Game(object):
    def __init__(self, players=[{'name': "Alice",   'id': 2},  \
                                {'name': "Bob",     'id': 3},  \
                                {'name': "Charlie", 'id': 4}], \
                advanced=False, id=None):
        self.id = id
        self.numPlayers = len(players)
        self.players = []
        for i in range(len(players)):
            self.players.append(Player(players[i]))
        shuffle(self.players)
        self.log = Log(self.players, advanced, id)
        self.finance = Finance(self.players)
        self.status = Status(self.numPlayers, self.players, self.log)
        #self.gameFlow = GameFlow()
        self.advanced = advanced
        #self.fundCards = self.fundCardsTest()
        self.fundCards = self.fundCards()
        self.luxuryTiles = self.luxuryTiles()
        self.fundingBoard = FundingBoard(self.fundCards[0:9])
        self.fundDeck = self.fundCards[9:]
        shuffle(self.fundDeck)
        self.discardPile =  []
        self.industryTiles = [15]*4
        self.standings = []
        self.bankruptPlayers = []

    def getActivePlayer(self):
        activePlayer = None
        if (len(self.status.active)>0):
            active = self.status.active[0]
            activePlayer = self.players[active]
        return activePlayer

    def removeHiddenInfo(self, playerInfo):
        '''
        playerInfo: dictionary of 'name' and 'id'
        remove the information that is hidden to player
            unless end of game is reached
        hidden information is:
            player's money: hidden to all others
            bid from player A to player B: money involved hidden to all other's
            player-specific logs (contains bids)
            deck: hidden to everyone
            finance overview of the other players
        if player is None or not a player in this game, all this information is hidden
        if player is in this game, it's money and money involved in a bid he is
        involved in is not hidden; also his log should be used
        '''
        self.fundDeck = None
        if not self.status.endOfGame:
            self.log.showKnownInfo(playerInfo)
            self.finance.hideHiddenInfo(playerInfo)
            for player in self.players:
                if not player.identical(playerInfo):
                    player.money = None
        self.log.log2 = None
        self.log.playerLog = None
        # set self.status.tradeOffer.money to None if playerInfo not involved
        if self.status.tradeOffer:
            offeringPlayer = self.players[self.status.tradeOffer.offeringPlayerIndex];
            opponent =       self.players[self.status.tradeOffer.opponentIndex];
            if (not offeringPlayer.identical(playerInfo) and
                not opponent.identical(playerInfo)):
                self.status.tradeOffer.money = None


    def addCardFromDeckToBoard(self):
        card = self.fundDeck.pop(0)
        self.log.add("Funding Card " + card.name() + " enters the board.")
        self.fundingBoard.addCard(card)
        if len(self.fundDeck)==0:
            self.log.add("Deck is empty. The discard pile is " + \
                         "shuffled to form a new deck.")
            self.fundDeck = self.discardPile
            shuffle(self.fundDeck)
            self.discardPile = []

    def removeCardFromBoard(self, value):
        return self.fundingBoard.removeCardFromBoard(value)

    def addCardToDiscardPile(self, card):
        self.discardPile.append(card)

    def numBearCardsGreaterOrEqualNumPlayers(self):
        return self.fundingBoard.numBearCards() >= self.numPlayers

    def checkForEmptyDeck(self):
        if len(self.fundDeck)==0:
            self.fundDeck = self.discardPile
            self.discardPile = []
            shuffle(self.fundDeck)

    def turnWheel(self):
        if self.status.marketCrash:
            self.log.add("The Wheel is turned twice (market crash)!")
        else:
            self.log.add("The Wheel is turned.")
        for player in self.players:
            player.turnWheel(self.status.marketCrash)

    def payInterest(self):
        for player in self.players:
            player.payInterest(self.log, self.finance)

    def gameEnded(self):
        for player in self.players:
            if player.bankrupt:
                self.finance.revealHiddenInfo()
                self.status.setEndOfGame()
        return self.status.endOfGame

    def moveFundCards(self):
        for player in self.players:
            player.moveFundCards()

    """
    Phase 1: Funding
    """

    def selectTileAndCard(self, value, tile, name):
        # TODO: check phase
        # check if player is active player
        if (name is None):
            return self.error("Not a player")
        active = self.status.active[0]
        if (name!=self.players[active].name):
            return self.error(name + " is not the active player")
        # check if player is allowed to take this combination of tile and card
        numberOfTiles = self.players[active].industryTiles[tile]
        row = self.fundingBoard.getRow(value)
        if (row is None):
            return self.error("There is no card with value " + str(value) + \
                              " on the board")
        if (row != numberOfTiles+1):
            return self.error("You have " + str(numberOfTiles) + \
                         " tiles, you cannot select a card from row " + \
                         str(row))
        if (self.industryTiles[tile]<=0):
            return(self.error("No tiles left of that type"))
        card = self.removeCardFromBoard(value)
        self.log.add(name + " takes Funding Card " + \
                     card.name() + " and a " + self.tileName(tile) + " tile.")
        self.finance.change(name, value)
        self.players[active].selectCardAndTile(card, tile)
        self.industryTiles[tile] -= 1
        self.addCardFromDeckToBoard()
        self.status.next()
        self.autoFlow()
        return None

    def passFunding(self, name):
        # TODO: check phase
        # check if player is active player
        if (name is None):
            return self.error("Not a player")
        active = self.status.active[0]
        if (name!=self.players[active].name):
            return self.error(name + " is not the active player")
        # to avoid the situation that everonye passes in round 1,
        # leading to neverending game, we might forbid it. 
        # for now, allow it and see if there is any feedback:
        #if (self.status.round==1):
        #    return self.error("You may not pass in the first round")
        self.log.add(name + " passes.")
        self.status.next()
        self.autoFlow()
        return None

    """
    Phase 2: Clandestine Trading 
    """

    def autoPassTrading(self):
        """
        if possible, autopass the trading phase for the active player:
            advanced option is not used or all luxuryTiles are already bought
            AND
            active player has no industry tiles or none of the other players
            has any tile he has
        """
        if (self.advanced and len(self.luxuryTiles)>1):
            return False
        active = self.status.active[0]
        activePlayer = self.players[active]
        for index, tiles in enumerate(activePlayer.industryTiles):
            if tiles>0:
                for player in self.players:
                    if player.name!=activePlayer.name and \
                      player.industryTiles[index]>0:
                        return False
        # player must pass
        self.log.add( activePlayer.name + \
                     " auto-passes (cannot trade).")
        self.status.next()
        return True

    def passTrading(self, name):
        # TODO: check phase
        # check if player is active player
        if (name is None):
            return self.error("Not a player")
        active = self.status.active[0]
        if (name!=self.players[active].name):
            return self.error(name + " is not the active player")
        self.log.add(name + " passes.")
        self.status.next()
        self.autoFlow()
        return None

    def sellTrade(self, name):
        # TODO: check phase
        if (name is None):
            return self.error("Not a player")
        if (self.status.tradeOffer is None):
            return self.error("There is currently no trade offer")
        active = self.status.active[0]
        if (name!=self.players[active].name):
            return self.error(name + " is not the active player")
        # check if player is the opponent (who got the offer)
        opponent =       self.players[self.status.tradeOffer.opponentIndex];
        offeringPlayer = self.players[self.status.tradeOffer.offeringPlayerIndex];
        tile =                        self.status.tradeOffer.tile
        money =                       self.status.tradeOffer.money
        if (name!=opponent.name):
            return self.error(name + " is not the active player")
        if opponent.industryTiles[tile]<=0:
            return self.error(name + " has no tile " + str(tile))
        #self.log.add("=> " + name + " accepts the trade.")
        logtxt = offeringPlayer.name + " <= " + self.tileName(tile) + \
                    " [<span <soldtag>>sold</span>] $ => " + name
        log2txt = offeringPlayer.name + " <= " + self.tileName(tile) + \
                    " [<span <soldtag>>sold</span>] $" + str(money) + \
                    " => " + name
        self.log.replace(logtxt,log2txt, [name, offeringPlayer.name])
        self.finance.trade(offeringPlayer.name, opponent.name, money)
        offeringPlayer.buy(tile, money)
        opponent.sell(tile, money)
        self.status.phase2RemoveTrade()
        self.status.next()
        self.autoFlow()
        return None

    def buyTrade(self, name):
        # TODO: check phase
        if (name is None):
            return self.error("Not a player")
        if (self.status.tradeOffer is None):
            return self.error("There is currently no trade offer")
        active = self.status.active[0]
        if (name!=self.players[active].name):
            return self.error(name + " is not the active player")
        # check if player is the opponent (who got the offer)
        opponent =       self.players[self.status.tradeOffer.opponentIndex];
        offeringPlayer = self.players[self.status.tradeOffer.offeringPlayerIndex];
        tile =                        self.status.tradeOffer.tile
        money =                       self.status.tradeOffer.money
        if (name!=opponent.name):
            return self.error(name + " is not the active player")
        if opponent.money < money:
            return self.error(name + " has not enough money for this trade")
        #self.log.add("=> " + name + " counter-offers the trade.")
        logtxt = offeringPlayer.name + \
                     " <= $ [<span <counteroffertag>>counter-offered</span>] " + \
                     self.tileName(tile)  + " => " + name
        log2txt = offeringPlayer.name + \
                     " <= $" + str(money) + \
                     " [<span <counteroffertag>>counter-offered</span>] " + \
                     self.tileName(tile)  + " => " + name
        self.log.replace(logtxt, log2txt, [name, offeringPlayer.name])
        self.finance.trade(opponent.name, offeringPlayer.name, money)
        offeringPlayer.sell(tile, money)
        opponent.buy(tile, money)
        self.status.phase2RemoveTrade()
        self.status.next()
        self.autoFlow()
        return None

    def offerTrade(self, money, tile, opponentName, name):
        # TODO: check phase
        # check if player is active player
        if (name is None):
            return self.error("Not a player")
        active = self.status.active[0]
        if (name!=self.players[active].name):
            return self.error(name + " is not the active player")
        opponent = None
        for index, player in enumerate(self.players):
            if player.name==opponentName:
                opponentIndex = index
                opponent = player
        if opponent is None:
            return self.error(opponentName + "is not a player")
        if opponentName==name:
            return self.error("Opponent must be a different player")
        if self.players[active].industryTiles[tile]<=0:
            return self.error(name + " has no tile " + str(tile))
        if opponent.industryTiles[tile]<=0:
            return self.error(opponentName + " has no tile " + str(tile))
        if self.players[active].money < money:
            return self.error(name + " has not enough money for this trade")
        #self.log.add(name + " offers a trade to " + opponentName + \
        #             " involving a " + self.tileName(tile) + " tile.")
        logtxt = name + " <= " + self.tileName(tile) + \
                    " [<span <tradeoffertag>>trade offer</span>] $ => " + \
                     opponentName
        log2txt = name + " <= " + self.tileName(tile) + \
                    " [<span <tradeoffertag>>trade offer</span>] $" + \
                    str(money) + " => " + \
                     opponentName
        self.log.add(logtxt, log2txt, [name, opponentName])
        self.status.phase2SetTrade(tile, money, active, opponentIndex)
        self.autoFlow()
        return None

    def buyLuxuryTile(self, tileIndex, name):
        # TODO: check phase
        # check if player is active player
        if (name is None):
            return self.error("Not a player")
        active = self.status.active[0]
        if (name!=self.players[active].name):
            return self.error(name + " is not the active player")
        # check if tile is available
        if (len(self.luxuryTiles)-1<tileIndex):
            return self.error("tile " + str(tileIndex) + " is not available")
        tile =  self.luxuryTiles[tileIndex]
        if (self.players[active].money <  tile.value):
            return self.error(name + " has not enough money")
        self.log.add(name + " buys a Luxury Tile (price: " + \
                     str(tile.value) + ", points: " + \
                     str(tile.points) + ")")
        self.finance.change(name, -tile.value)
        self.players[active].buyLuxuryTile(tile)
        del self.luxuryTiles[tileIndex]
        self.status.next()
        self.autoFlow()
        return None

    """
    Phase 3: Pass the Start Player Marker
    """
    def selectCardToDiscard(self, value, name):
        # TODO: check phase
        # check if player is active player
        if (name is None):
            return self.error("Not a player")
        active = self.status.active[0]
        if (name!=self.players[active].name):
            return self.error(name + " is not the active player")
        card = self.removeCardFromBoard(value)
        if (card is None):
            return self.error("There is no card with value " + str(value) + \
                              " on the board")
        if (card.fundtype != "Starting Fund Card"):
            self.discardPile.append(card)
        self.log.add(name + " removes Funding Card " \
                     + card.name() + " from the board.")
        self.addCardFromDeckToBoard()
        self.status.next()
        self.autoFlow()
        return None

    """
    Phase 4: Market Crash
    """

    def discardTile(self, tile, name):
        # TODO: check phase
        # check if player is active player
        if (name is None):
            return self.error("Not a player")
        active = self.status.active[0]
        if (name!=self.players[active].name):
            return self.error(name + " is not the active player")
        # check if player is allowed to discard this tile 
        discardableTiles = self.players[active].discardableTiles()
        if (tile not in discardableTiles):
            return(self.error("You cannot discard that tile"))
        self.log.add(name + " discards a " + self.tileName(tile) + \
                     " tile.")
        self.players[active].discardTile(tile)
        self.industryTiles[tile]+=1
        self.status.next()
        self.autoFlow()
        return None

    def marketCrash(self):
        """
        """
        numBearCards = self.fundingBoard.numBearCards()
        if numBearCards < self.numPlayers:
            self.log.add("No market crash.")
            self.status.next()
        else:
            """
            remove bear cards from board
            new fund deck  is old fund deck + discards + removed bear cards
            shuffle deck
            add cards to board
            """
            bearCards = self.fundingBoard.removeBearCards()
            logstr = "All Bear Funding Cards ("
            for card in bearCards[:-1]:
                logstr = logstr + card.shortName() + ", "
            logstr = logstr + bearCards[-1].shortName() + ") are removed " + \
                    "from the board."
            self.log.add("Market crash!")
            self.log.add(logstr)
            self.fundDeck = self.fundDeck + self.discardPile + bearCards
            shuffle(self.fundDeck)
            self.discardPile = []
            for i in range(numBearCards):
                card = self.fundDeck.pop(0)
                self.log.add("Funding Card " + card.name() + " enters the board.")
                self.fundingBoard.addCard(card)
            # empty deck cannot happen, if it does then discard pile is empty
            # anyway
            self.status.phase4SetMarketCrash()

    def autoDiscard(self):
        """
        if possible auto-discard a tile for the active player
        """
        active = self.status.active[0]
        discardableTiles = self.players[active].discardableTiles()
        if len(discardableTiles) > 1:
            return False
        else:
            if len(discardableTiles) == 1:
                self.log.add( self.players[active].name + " auto-discards a " \
                             + self.tileName(discardableTiles[0]) + " tile.")
                self.players[active].discardTile(discardableTiles[0])
                self.industryTiles[discardableTiles[0]]+=1
            else:
                # no discardableTiles
                self.log.add( self.players[active].name + \
                             " has no tiles to discard.")

            self.status.next()
            return True

    def calculateFinalScoring(self):
        self.bankruptPlayers = []
        self.standings = []
        for player in self.players:
            player.calculatePoints(self.advanced)
            if player.bankrupt:
                self.bankruptPlayers.append(player)
            else:
                self.standings.append(player)
        self.standings.sort(reverse=True)
        self.bankruptPlayers.sort(reverse=True)
        if len(self.standings)==0:
            self.log.add("There is no winner.")
        else:
            self.log.add("The winner is: " + self.standings[0].name)
        for place, player in enumerate(self.standings, start=1):
            self.log.add(str(place) + ": " + player.name + \
                         " (points: {:3.0f}".format(player.points) + \
                         "; most valuable card: $" + \
                         str(player.maxCardValue) + ")")
        for index, player in enumerate(self.bankruptPlayers, ):
            self.log.add(str(len(self.standings) + index + 1) + \
                         ": " + player.name + \
                         " BANKRUPT " + \
                         "(points: {:3.0f}".format(player.points) + \
                         "; most valuable card: $" + \
                         str(player.maxCardValue) + ")")

    def autoFlow(self):
        """
        auto-execute actions:
            - if there is no decision at all (like in the phases turn the wheel
              and pay interest)
            - if there is no decision to make because of the game situation
              (like in the phase market crash and there is a single tile type
              with the most tiles)
            - if there is an order given (to be implemented...)
        The loop will continue while there are still actions to be
        auto-executed, and will exit with a return when there is no
        auto-execute action left.
        """
        while True:
            if (self.status.phase==1):
                return
            elif (self.status.phase==2):
                if not self.autoPassTrading():
                    return
            elif (self.status.phase==3):
                return
            elif (self.status.phase==4):
                if self.status.marketCrash:
                    if not self.autoDiscard():
                        return
                else:
                    self.marketCrash()
            elif (self.status.phase==5):
                self.turnWheel()
                self.status.next()
            elif (self.status.phase==6):
                self.payInterest()
                if self.gameEnded():
                    self.log.add("<span style='font-style:italic'>End of Game</span>")
                    self.calculateFinalScoring()
                    self.log.revealHiddenInfo()
                    return
                self.moveFundCards()
                self.status.next()
            else:
                #should never happen
                return self.error("Unknown phase")

    @staticmethod
    def tileName(tile):
        # convert numbers to names to be used in log
        # the tags are replaced by styles in Log.vue
        if tile==0:
            return "<span <transporttag>>transportation</span>"
        elif tile==1:
            return "<span <graintag>>grain</span>"
        elif tile==2:
            return "<span <mediatag>>media</span>"
        elif tile==3:
            return "<span <realestatetag>>real estate</span>"
        else:
            return "unknown"

    @staticmethod
    def error(txt):
        # returns an error text 
        data = {}
        data['error'] = txt
        return data

    @staticmethod
    def fundCards():
        return [
         FundCard(9, 5, 8, "Starting Fund Card"),
         FundCard(10, 5, 9, "Starting Fund Card"),
         FundCard(11, 5, 10, "Starting Fund Card"),
         FundCard(12, 5, 11, "Starting Fund Card"),
         FundCard(13, 4, 10, "Starting Fund Card"),
         FundCard(14, 4, 11, "Starting Fund Card"),
         FundCard(15, 4, 12, "Starting Fund Card"),
         FundCard(16, 4, 13, "Starting Fund Card"),
         FundCard(17, 3, 11, "Starting Fund Card"),
         FundCard(18, 3, 12, "Fund Card"),
         FundCard(19, 3, 13, "Fund Card"),
         FundCard(20, 3, 14, "Fund Card"),
         FundCard(21, 5, 26, "Fund Card"),
         FundCard(22, 5, 28, "Fund Card"),
         FundCard(23, 5, 30, "Fund Card"),
         FundCard(24, 5, 32, "Fund Card"),
         FundCard(25, 4, 27, "Fund Card"),
         FundCard(26, 4, 29, "Fund Card"),
         FundCard(27, 4, 31, "Fund Card"),
         FundCard(28, 4, 33, "Fund Card"),
         FundCard(29, 3, 26, "Fund Card"),
         FundCard(30, 3, 27, "Fund Card"),
         FundCard(31, 3, 28, "Fund Card"),
         FundCard(32, 3, 29, "Fund Card"),
         FundCard(33, 5, 57, "Fund Card"),
         FundCard(34, 5, 59, "Fund Card"),
         FundCard(35, 5, 61, "Fund Card"),
         FundCard(36, 5, 63, "Fund Card"),
         FundCard(37, 4, 53, "Fund Card"),
         FundCard(38, 4, 55, "Fund Card"),
         FundCard(39, 4, 57, "Fund Card"),
         FundCard(40, 4, 59, "Fund Card"),
         FundCard(41, 3, 46, "Fund Card"),
         FundCard(42, 3, 48, "Fund Card"),
         FundCard(43, 3, 50, "Fund Card"),
         FundCard(44, 3, 52, "Fund Card"),
         FundCard(45, 5, 102, "Fund Card"),
         FundCard(46, 5, 105, "Fund Card"),
         FundCard(47, 5, 108, "Fund Card"),
         FundCard(48, 5, 111, "Fund Card"),
         FundCard(49, 4, 91, "Fund Card"),
         FundCard(50, 4, 93, "Fund Card"),
         FundCard(51, 4, 95, "Fund Card"),
         FundCard(52, 4, 98, "Fund Card"),
         FundCard(53, 3, 75, "Fund Card"),
         FundCard(54, 3, 77, "Fund Card"),
         FundCard(55, 3, 79, "Fund Card"),
         FundCard(56, 3, 81, "Fund Card"),
         FundCard(57, 5, 162, "Fund Card"),
         FundCard(58, 5, 165, "Fund Card"),
         FundCard(59, 5, 168, "Fund Card"),
         FundCard(60, 5, 171, "Fund Card"),
         FundCard(61, 4, 140, "Fund Card"),
         FundCard(62, 4, 143, "Fund Card"),
         FundCard(63, 4, 146, "Fund Card"),
         FundCard(64, 4, 149, "Fund Card"),
         FundCard(65, 3, 114, "Bear Fund Card"),
         FundCard(66, 3, 116, "Bear Fund Card"),
         FundCard(67, 3, 118, "Bear Fund Card"),
         FundCard(68, 3, 120, "Bear Fund Card"),
         FundCard(69, 3, 122, "Bear Fund Card"),
         FundCard(70, 3, 124, "Bear Fund Card"),
         FundCard(71, 3, 126, "Bear Fund Card"),
         FundCard(72, 3, 128, "Bear Fund Card"),
         FundCard(73, 3, 130, "Bear Fund Card"),
         FundCard(74, 3, 132, "Bear Fund Card"),
         FundCard(75, 3, 134, "Bear Fund Card"),
         FundCard(76, 3, 136, "Bear Fund Card"),
         FundCard(77, 3, 138, "Bear Fund Card"),
         FundCard(78, 3, 140, "Bear Fund Card"),
         FundCard(79, 3, 142, "Bear Fund Card"),
         FundCard(80, 3, 144, "Bear Fund Card")
        ]

    @staticmethod
    def fundCardsTest():
        return [
         FundCard(9, 5, 8, "Starting Fund Card"),
         FundCard(10, 5, 9, "Starting Fund Card"),
         FundCard(11, 5, 10, "Starting Fund Card"),
         FundCard(17, 3, 11, "Starting Fund Card"),
         FundCard(18, 3, 12, "Fund Card"),
         FundCard(24, 5, 32, "Fund Card"),
         FundCard(30, 3, 27, "Fund Card"),
         FundCard(36, 5, 63, "Fund Card"),
         FundCard(42, 3, 48, "Fund Card"),
         FundCard(48, 5, 111, "Fund Card"),
         FundCard(54, 3, 77, "Fund Card"),
         FundCard(60, 5, 171, "Fund Card"),
         FundCard(66, 3, 116, "Bear Fund Card"),
         FundCard(72, 3, 128, "Bear Fund Card"),
         FundCard(78, 3, 140, "Bear Fund Card"),
         FundCard(79, 3, 142, "Bear Fund Card"),
         FundCard(80, 3, 144, "Bear Fund Card")
        ]

    @staticmethod
    def luxuryTiles():
        return [
         LuxuryTile(30, 1),
         LuxuryTile(56, 2),
         LuxuryTile(78, 3),
         LuxuryTile(96, 4)
        ]

