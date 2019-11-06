def float_range(*args):
    def is_in_range(val):
        if step < 0:
            return val > start
        elif step > 0:
            return val < stop


    if len(args) == 0 or len(args) > 3:
        raise TypeError
    elif len(args) == 1:
        start = 0.0
        step = 1
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
        step = 1
    elif len(args) == 3:
        start, stop, step = args


    if step == 0:
        raise ValueError
    elif step < 0:
        temp = start
        start = stop
        stop = temp

    val = start
    while is_in_range(val):
        yield val
        val += step


