def float_range2(start, stop=None, step=1):
    def is_in_range(val):
        if step < 0:
            return val > stop
        elif step > 0:
            return val < stop

    if stop is None:
        start, stop = 0, start

    if step == 0:
        raise ValueError

    val = start
    while is_in_range(val):
        yield val
        val += step


def test(*args):
    print(len(args))
    for arg in args:
        print(arg)
