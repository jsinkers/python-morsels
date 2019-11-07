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

    def is_in_range(self):
        if self.step < 0:
            return self.val > self.stop
        elif self.step > 0:
            return self.val < self.stop
