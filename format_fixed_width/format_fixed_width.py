def format_fixed_width(cols, padding=2, widths=None, alignments=None):
    ret_text = ""
    if cols:
        [*x] = zip(*cols)
        # get column widths based on width of maximum entry. exclude last column
        if widths is None:
            widths = [len(max(y, key=len)) for y in x]

        if alignments is None:
            alignments = ["L"] * len(x)

        ret_text = []
        for row in cols:
            new_row = [justify(e, a, w) for e, w, a in zip(row, widths, alignments)]
            pad = ' ' * padding
            new_row = pad.join(new_row)
            new_row = new_row.rstrip()
            ret_text.append(new_row)

        ret_text = '\n'.join(ret_text)

    return ret_text


def justify(text, align, width):
    if align == "L":
        ret_text = text.ljust(width)
    elif align == "R":
        ret_text = text.rjust(width)
    else:
        raise ValueError

    return ret_text