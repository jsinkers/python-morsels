def format_fixed_width(cols, padding=2):
    ret_text = ""
    if cols:
        [*x] = zip(*cols)
        # get column widths based on width of maximum entry. exclude last column
        col_widths = [len(max(y, key=len)) for y in x[:-1]]
        for ind, row in enumerate(cols):
            *entry, last_entry = row
            for e, w in zip(entry, col_widths):
                # adjust width of column and pad with spaces
                ret_text += e.ljust(w) + ' '*padding

            # append last item of row without padding
            ret_text += last_entry

            # add a newline character, except for last line
            if ind < len(cols) - 1:
                ret_text += "\n"

    return ret_text


