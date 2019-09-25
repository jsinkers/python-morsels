from collections.abc import Iterable


def deep_flatten(inp):
    ret_list = []
    for i in inp:
        if isinstance(i, Iterable):
            ret_list += deep_flatten(i)
        else:
            ret_list.append(i)

    return ret_list
