def tail(seq, n):
    """
    Returns the last n elements of sequence seq in original order
    :param seq: sequence
    :param n: number of elements to return
    """
    if n == 0:
        return []

    return list(seq[-n:])
