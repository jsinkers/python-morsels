def parse_ranges(ranges_str):
    """
    Parse the input ranges_str to a list of all items in that range
    :param ranges_str:
    :return: parsed ranges list
    """
    ranges = ranges_str.split(',')
    ranges = [r.split('-') for r in ranges]
    for r in ranges:
        r1, *r2 = r
        r1 = int(r1)
        if r2 and '>' not in r2[0]:
            r2 = int(r2[0])
            parsed_ranges = range(r1, r2+1)
        else:
            parsed_ranges = [r1]
        for pr in parsed_ranges:
            yield pr

