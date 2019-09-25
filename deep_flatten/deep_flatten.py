from collections.abc import Iterable


def deep_flatten(inp):
    ret_list = []
    for i in inp:
        if isinstance(i, Iterable):
            for x in deep_flatten(i):
                yield x
        else:
            yield i

    #yield ret_list
