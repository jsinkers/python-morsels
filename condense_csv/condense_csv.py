from collections import defaultdict
import csv
import io


def condense_csv(text, id_name="id"):
    textio = io.StringIO(text)
    reader = csv.reader(textio)
    # reshape input text using defaultdict
    d = defaultdict(dict)
    for id, attr, val in reader:
        d[id][id_name] = id
        d[id][attr] = val

    # turn defaultdict into output csv
    ret_textio = io.StringIO()
    keys = list(next(iter(d.values())).keys())
    writer = csv.DictWriter(ret_textio, fieldnames=keys)
    writer.writeheader()
    for entry in d:
        writer.writerow(d[entry])

    return ret_textio.getvalue()

