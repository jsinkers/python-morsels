import unicodedata


def normalize(string):
    return unicodedata.normalize("NFD", string.casefold())


class FuzzyString:
    def __init__(self, string):
        self.string = string

    def __eq__(self, other):
        return self.lstring == normalize(other)

    def __le__(self, other):
        return self.lstring <= normalize(other)

    def __ge__(self, other):
        return self.lstring >= normalize(other)

    def __lt__(self, other):
        return self.lstring < normalize(other)

    def __gt__(self, other):
        return self.lstring > normalize(other)

    def __repr__(self):
        return repr(self.string)

    def __str__(self):
        return str(self.string)
    
    def __contains__(self, item):
        return normalize(item) in self.lstring

    def __add__(self, item):
        self.string += item
        return self

    @property
    def lstring(self):
        return normalize(self.string)
