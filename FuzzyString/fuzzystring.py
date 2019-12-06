class FuzzyString:
    def __init__(self, string):
        self.string = string

    def __eq__(self, other):
        return self.lstring == other.lower()

    def __le__(self, other):
        return self.lstring <= other.lower()

    def __ge__(self, other):
        return self.lstring >= other.lower()

    def __lt__(self, other):
        return self.lstring < other.lower()

    def __gt__(self, other):
        return self.lstring > other.lower()

    def __repr__(self):
        return repr(self.string)

    def __str__(self):
        return str(self.string)
    
    def __contains__(self, item):
        return item.lower() in self.lstring

    def __add__(self, item):
        self.string += item
        return self

    @property
    def lstring(self):
        return self.string.lower()
