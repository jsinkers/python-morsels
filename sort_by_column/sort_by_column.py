import argparse
import csv
import sys


def sort_by_column(input_csv, sort_inp, with_header=None):
    sort_cols = []
    # parse column sorting inputs
    for col_type in sort_inp:
        col, *sort_type = col_type.split(":")
        # default behaviour is to sort as strings
        if len(sort_type) == 1 and sort_type[0] == "num":
            sort_type = int
        else:
            sort_type = str

        # store the column number and the type-casting function as a list of dicts
        sort_cols.append({"col": int(col), "type": sort_type})

    csv_writer = csv.writer(sys.stdout)

    with open(input_csv, 'r') as f:
        csv_reader = csv.reader(f)
        csv_rows = []

        if with_header:
            header_row = next(csv_reader)
            csv_writer.writerow(header_row)

        for row in csv_reader:
            csv_rows.append(row)

    # apply a sort for multiple columns, using the specified type-casting
    csv_rows = sorted(csv_rows, key=lambda x: [sort_info["type"](x[sort_info['col']]) for sort_info in sort_cols])
    for row in csv_rows:
        csv_writer.writerow(row)


if __name__ == '__main__':
    # set up arg parser
    parser = argparse.ArgumentParser(description='Sort input csv by specified column number')
    parser.add_argument(dest='input_csv', metavar='input_csv')
    parser.add_argument(dest='sort_cols', metavar='sort_cols', nargs='+')
    parser.add_argument('--with-header', dest='with_header', action="store_true", default=False)
    # parse args and call the function
    args = parser.parse_args()
    sort_by_column(args.input_csv, args.sort_cols, args.with_header)

