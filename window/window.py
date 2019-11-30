from collections import deque


def window(items, n):
    if n == 0:
      return []

    d = deque([], maxlen=n)
    windows = []
    for ind, item in enumerate(items):
        d.append(item)
        if len(d) == n:
            windows.append(tuple(d))

    return windows
