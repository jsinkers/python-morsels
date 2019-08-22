def compact(seq):
    first_item = True
    compact_seq = []
    last_item = object()
    for item in seq:
        if first_item or item != last_item:
            first_item = False
            yield item
            last_item = item
