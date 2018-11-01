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

        removeIndex = None
        for i in range(len(self.board)):
            if self.board[i] == fundingCard:
                removeIndex = i
        if removeIndex is not None:
            del self.board[removeIndex]



    def addCard(self, fundingcard):

        # add the card and then sort

        self.board.append(fundingcard)
        self.board.sort()
