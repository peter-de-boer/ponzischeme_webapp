class FundingBoard(object):

    """ represent board as ordered list of 9 cards
        effects of different rows: TBD
    """

    def __init__(self, fundingCards):

        # fundingCards should be list of 9 starting cards

        self.board = [None] * 9
        for i in range(len(fundingCards)):
            self.board[i] = fundingCards[i]


    def removeCard(self, fundingCard):

        # find the fundingCard on the board and if found then remove it

        if fundingCard in self.board:
            self.board.remove(fundingCard)


    def removeCardFromBoard(self, value):
        remove = None
        for card in self.board:
            if card.value == value:
                remove = card
        if remove:
            self.board.remove(remove)
        return remove



    def addCard(self, fundingcard):

        # add the card and then sort

        self.board.append(fundingcard)
        self.board.sort()

    def removeBearCards(self):
        bearCards = [card for card in self.board  \
                     if card.fundtype == "Bear Fund Card"]
        for card in bearCards:
            self.board.remove(card)
        return bearCards

    def numBearCards(self):
        n = 0
        for card in self.board:
            if card.fundtype=="Bear Fund Card":
                n+=1
        return n

    def getRow(self, value):
        """
        return the row (1,2, or 3) of fund card with this value
        if no card with this value on the board, return 0
        """
        for i in range(9):
            if self.board[i].value==value:
                return i//3 + 1
        return None
