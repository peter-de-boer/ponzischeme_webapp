class LuxuryTile(object):
    def __init__(self, value, points):
        self.value = value
        self.points = points

    def __eq__(self, other):
        if isinstance(other, LuxuryCard):
            return self.value == other.value
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, LuxuryCard):
            return self.value < other.value
        return NotImplemented
