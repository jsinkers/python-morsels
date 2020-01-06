def interleave(*iter):
    for its in zip(*iter):
        for i in its:
            yield i
