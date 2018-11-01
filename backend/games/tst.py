from game import Game
from fundCard import FundCard
from fundingBoard import FundingBoard

def printFundcard(fundCard):
    print(("Value: {:4d},   Time: {:3d},   "
           "Interest: {:4d},   Average: {:6.2f}%   "
           "Type: {:20s}").format(fundCard.value,
                                  fundCard.time,
                                  fundCard.interest,
                                  fundCard.averageInterestPerc,
                                  fundCard.fundtype))

def printFundingBoard(game):
    print("Board:")
    for fundCard in game.fundingBoard.board:
        printFundcard(fundCard)

def printCards(cards):
    print("len: ", len(cards))
    for card in cards:
        printFundcard(card)

def printDeckBoard():
    print("deck:")
    printCards(gamex.fundDeck)
    print("board:")
    printCards(gamex.fundingBoard.board)

def printGame(game):
    print(game.id)
    print(game.players)
    print(game.numPlayers)
    print(game.advanced)
    print(len(game.fundCards))
    print("All fundCards:")
    for fundCard in game.fundCards:
        printFundcard(fundCard)
    printDeckBoard()    

def tstEqualities():

    print("test  fundCard equalities")
    x1 = FundCard(9, 5, 8, "Starting Fund Card")
    x2 = FundCard(9, 6, 9, "other txt")
    x3 = FundCard(10, 5, 8, "Starting Fund Card")
    first = gamex.fundCards[0]
    printFundcard(x1)
    printFundcard(x2)
    printFundcard(x3)
    printFundcard(first)
    print("True", x1==first)
    print("True", x2==first)
    print("False", x3==first)
    print("True", x1==x2)
    print("False", x1==x3)
    print("True", x1!=first)
    print("True", x2!=first)
    print("False", x3!=first)
    print("True", x1!=x2)
    print("False", x1!=x3)

def tstRemoveAdd():
    x1 = FundCard(9, 5, 8, "Starting Fund Card")
    printFundingBoard(gamex)
    print("remove card")
    printFundcard(x1)
    gamex.fundingBoard.removeCard(x1)
    printFundingBoard(gamex)

    y1 = FundCard(19, 6, 9, "other txt")
    print("remove card")
    printFundcard(y1)
    gamex.fundingBoard.removeCard(y1)
    printFundingBoard(gamex)

    print("add card")
    printFundcard(y1)
    gamex.fundingBoard.addCard(y1)
    printFundingBoard(gamex)

    y2 = FundCard(14, 6, 9, "other txt")
    print("remove card")
    printFundcard(y2)
    gamex.fundingBoard.removeCard(y2)
    printFundingBoard(gamex)

    print("add card")
    printFundcard(y2)
    gamex.fundingBoard.addCard(y2)
    printFundingBoard(gamex)

def tstPickCard(n):
    card = gamex.fundingBoard.board[n]
    gamex.fundingBoard.removeCard(card)
    gamex.addCardFromDeck()

def tstPickCards():
    for i in range(9):
        print("****", i)
        tstPickCard(4)
        printDeckBoard()


gamex = Game()
printGame(gamex)

#tstEqualities()
#tstRemoveAdd()

tstPickCards()
