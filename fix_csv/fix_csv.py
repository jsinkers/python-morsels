import argparse
import csv


# python cookbook: 6.1 read/write csv
# python cookbook: 13.3 parsing command-line options
def fix_csv(in_filename, out_filename, delim=None, quote_char=None):
    """
    fix a csv delimited by pipes (|) to be delimited by commas (,)
        in_filename: name of input file
        out_filename: name of output file

    """
    if quote_char is None:
        quote_char = '"'

    with open(in_filename) as in_csv, open(out_filename, 'w') as out_csv:
        if delim is None:
            dialect = csv.Sniffer().sniff(in_csv.read(1024))
            in_csv.seek(0)
            csv_reader = csv.reader(in_csv, dialect=dialect)
        else:
            csv_reader = csv.reader(in_csv, delimiter=delim, quotechar=quote_char)

        csv_writer = csv.writer(out_csv, delimiter=',', lineterminator='\n')
        for row in csv_reader:
            csv_writer.writerow(row)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Correct CSV delimiters of input_csv to the output fixed_csv')
    parser.add_argument(dest='input_csv', metavar='input_csv')
    parser.add_argument(dest='fixed_csv', metavar='fixed_csv')
    parser.add_argument('--in-delimiter', dest='in_delim', metavar='input delimiter', default=None)
    parser.add_argument('--in-quote', dest='in_quote', metavar='quote character', default=None)

    args = parser.parse_args()
    fix_csv(args.input_csv, args.fixed_csv, delim=args.in_delim, quote_char=args.in_quote)
