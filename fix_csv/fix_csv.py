import csv
import sys


# python cookbook: 6.1 read/write csv
# python cookbook: 13.3 parsing command-line options
def fix_csv(in_filename, out_filename):
    """
    fix a csv delimited by pipes (|) to be delimited by commas (,)
        in_filename: name of input file
        out_filename: name of output file

    """
    delim = '|'
    with open(in_filename) as in_csv, open(out_filename, 'w') as out_csv:
        csv_reader = csv.reader(in_csv, delimiter=delim)
        csv_writer = csv.writer(out_csv, delimiter=',', lineterminator='\n')
        for row in csv_reader:
            csv_writer.writerow(row)


if __name__ == "__main__":
    print(sys.argv)
    _, in_filename, out_filename, *additional_args = sys.argv
    fix_csv(in_filename, out_filename)
