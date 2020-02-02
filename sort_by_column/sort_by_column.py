import argparse
import csv
import sys


def sort_by_column(input_csv, sort_cols, with_header=None):
    sort_cols = [int(i) for i in sort_cols]
    csv_writer = csv.writer(sys.stdout)

    with open(input_csv, 'r') as f:
        csv_reader = csv.reader(f)
        csv_rows = []
        if with_header:
            header_row = next(csv_reader)
            csv_writer.writerow(header_row)

        for row in csv_reader:
            csv_rows.append(row)

    csv_rows = sorted(csv_rows, key=lambda x: [x[i] for i in sort_cols])
    for row in csv_rows:
        csv_writer.writerow(row)


if __name__ == '__main__':
    # set up arg parser
    parser = argparse.ArgumentParser(description='Sort input csv by specified column number')
    parser.add_argument(dest='input_csv', metavar='input_csv')
    parser.add_argument(dest='sort_cols', metavar='sort_cols', nargs='+')
    parser.add_argument('--with-header', dest='with_header', action="store_true", default=False)
    #parser.add_argument('--in-quote', dest='in_quote', metavar='quote character', default=None)

    args = parser.parse_args()
    sort_by_column(args.input_csv, args.sort_cols, args.with_header)

