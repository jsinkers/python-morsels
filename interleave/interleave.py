def interleave(iter1, iter2):
    for (iter1, iter2) in zip(iter1, iter2):
        yield iter1
        yield iter2
