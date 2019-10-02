def parse_ranges(ranges_str):
    """
    Parse the input ranges_str to a list of all items in that range
    :param ranges_str:
    :return: parsed ranges list
    """
    ranges = ranges_str.split(',')
    ranges = [r.split('-') for r in ranges]
    parsed_ranges = []
    for r1, r2 in ranges:
        r1 = int(r1)
        r2 = int(r2)
        parsed_ranges += list(range(r1, r2+1))

    return parsed_ranges
