from fundCard import FundCard
from fundingBoard import FundingBoard
import random
import sys

class Game(object):
    def __init__(self, players=("Alice", "Bob", "Charlie"), advanced=False,
                 id=None):
        self.id = id
        self.numPlayers = len(players)
        self.players = players
        self.advanced2 = advanced
        #self.advanced = advanced
        self.fundCards = self.fundCardsTest()
        #self.fundCards = self.fundCards()
        self.fundingBoard = FundingBoard(self.fundCards[0:9])
        self.fundDeck = self.fundCards[9:]
        random.shuffle(self.fundDeck)
        self.discards =  []

    def addCardFromDeck(self):
        if len(self.fundDeck)==0:
            # empty deck should never happen
            sys.exit("empty deck")
        card = self.fundDeck.pop(0)
        self.fundingBoard.addCard(card)


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

