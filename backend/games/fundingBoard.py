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
