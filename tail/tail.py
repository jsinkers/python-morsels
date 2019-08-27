def tail(seq, n):
    """
    Returns the last n elements of sequence seq in original order
    :param seq: sequence
    :param n: number of elements to return
    """
    if n <= 0:
        return []

    tail_list = []
    for item in seq:
        if len(tail_list) == n:
            tail_list.pop(0)

        tail_list.append(item)

    return tail_list
