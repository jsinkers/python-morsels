class FuzzyString:
    def __init__(self, string):
        self.string = string

    def __eq__(self, other):
        return self.string.lower() == other.lower()

    def __repr__(self):
        return repr(self.string)

    def __str__(self):
        return str(self.string)
