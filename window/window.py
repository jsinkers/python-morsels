from collections import deque


def window(items, n):
    if n == 0:
        return []

    d = deque([], maxlen=n)

    for ind, item in enumerate(items):
        d.append(item)
        if len(d) == n:
            yield tuple(d)

    if n > len(d):
        for i in range(n-len(d)):
            d.append(None)

        yield tuple(d)
