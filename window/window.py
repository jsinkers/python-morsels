from collections import deque


def window(items, n):
    if n == 0:
        return []

    d = deque([], maxlen=n)
    windows = []
    for ind, item in enumerate(items):
        d.append(item)
        if len(d) == n:
            yield tuple(d)

