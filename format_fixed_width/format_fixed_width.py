def format_fixed_width(cols, padding=2, widths=None, alignments=None):
    ret_text = ""
    if cols:
        [*x] = zip(*cols)
        # get column widths based on width of maximum entry. exclude last column
        if widths is None:
            widths = [len(max(y, key=len)) for y in x]

        if alignments is None:
            alignments = ["L"] * len(x)

        for ind, row in enumerate(cols):
            entry = row
            #*entry, last_entry = row
            for e, w, align in zip(entry, widths, alignments):
                # adjust width of column and pad with spaces
                if align == 'L':
                    ret_text += e.ljust(w) + ' ' * padding
                elif align == 'R':
                    ret_text += e.rjust(w) + ' ' * padding

            # append last item of row without padding
            #ret_text += last_entry
            ret_text = ret_text.rstrip()

            # add a newline character, except for last line
            if ind < len(cols) - 1:
                ret_text += "\n"

    return ret_text


