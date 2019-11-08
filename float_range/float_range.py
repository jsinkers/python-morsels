import math


class float_range2:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start

        if step == 0:
            raise ValueError

        self.start = start
        self.stop = stop
        self.step = step
        self.val = start

    def __iter__(self):
        while self.is_in_range():
            yield self.val
            self.val += self.step

    def __len__(self):
        delta = self.stop - self.start
        if delta*self.step < 0:
            return 0

        if delta % self.step == 0:
            return math.floor(delta/self.step)
        else:
            return math.floor(delta/self.step) + 1

    def __reversed__(self):
        self.val = (len(self)-1)*self.step + self.start
        if self.step > 0:
            while self.val >= self.start:
                yield self.val
                self.val -= self.step
        elif self.step < 0:
            while self.val <= self.stop:
                yield self.val
                self.val -= self.step

    def is_in_range(self):
        if self.step < 0:
            return self.val > self.stop
        elif self.step > 0:
            return self.val < self.stop

    def __eq__(self, other):
        if isinstance(other, (float_range2, range)):
            try:
                if len(self) != len(other):
                    return False
            except TypeError:
                return False

            for item_self, item_other in zip(self, other):
                if item_self != item_other:
                    return False

            return True
        else:
            return NotImplemented

    def __ne__(self, other):
        return not (self == other)
