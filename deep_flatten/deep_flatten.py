from collections.abc import Iterable


def deep_flatten(inp):
    for i in inp:
        if isinstance(i, Iterable) and type(i) is not str:
            for x in deep_flatten(i):
                yield x
        else:
            yield i
