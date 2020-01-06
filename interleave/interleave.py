def interleave(*iters):
    # make everything an iterator
    iters = [iter(it) for it in iters]
    num_exhausted = 0
    # stop once all iterators are exhausted
    while num_exhausted < len(iters):
        num_exhausted = 0
        for its in iters:
            try:
                rv = next(its)
                yield rv
            except StopIteration:
                # count the number of exhausted iterators
                num_exhausted += 1

