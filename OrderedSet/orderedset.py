class OrderedSet:
    def __init__(self, items):
        self.items = []
        self.set_items = set(self.items)
        for item in items:
            if item not in self:
                self.items.append(item)
                self.set_items.add(item)

        #self.items = items
        #self.set_items = set(items)

    def __contains__(self, item):
        return item in self.set_items

    #@property
    #def items(self):
    #    return self._items

    #@items.setter
    #def items(self, item):
    #    self._items.append(self.items)
    #    self.set_items = set(self.items)
    def __len__(self):
        return len(self.items)

    def add(self, item):
        if item not in self.set_items:
            self.items.append(item)
            self.set_items.add(item)

    def discard(self, item):
        if item in self:
            self.items.remove(item)
            self.set_items.discard(item)

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            if self.items == other.items:
                return True
        elif isinstance(other, set):
            if self.set_items == other:
                return True

        return False


    def __repr__(self):
        return str(self.items)

    def __iter__(self):
        for item in self.items:
            yield item
