def compact(seq):
    first_item = True
    compact_seq = []
    for item in seq:
        if first_item:
            first_item = False
            yield item
            compact_seq.append(item)
        else:
            if item is not last_item:
                yield item
                compact_seq.append(item)

        last_item = item

    return iter(compact_seq)

