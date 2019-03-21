class FundCard(object):
    def __init__(self, value, time, interest, fundtype):
        self.value = value
        self.time = time
        self.interest = interest
        self.fundtype = fundtype
        self.averageInterestPerc = self.averageInterest()

    def averageInterest(self):
        return 100*(((self.interest)/self.time)/self.value)

    def name(self):
        return "$" + str(self.value) + "&nbsp;(<" + str(self.time) + ">&nbsp;$" + \
                str(self.interest) + ")"

    def shortName(self):
        return "$" + str(self.value)

    def __eq__(self, other):
        if isinstance(other, FundCard):
            return self.value == other.value
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, FundCard):
            return self.value < other.value
        return NotImplemented
