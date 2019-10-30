import argparse
import configparser
import csv


def ini2csv(ini_filename, csv_filename):
    config = configparser.ConfigParser()
    config.read(ini_filename)

    with open(csv_filename, 'w', newline='') as f:
        csv_writer = csv.writer(f)
        for section in config.sections():
            for (key, value) in config[section].items():
                csv_writer.writerow([section, key, value])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert an INI-like file to a CSV-like file')
    parser.add_argument(dest='ini_filename', metavar='ini_filename')
    parser.add_argument(dest='csv_filename', metavar='csv_filename')
    #parser.add_argument('--in-delimiter', dest='in_delim', metavar='input delimiter', default=None)

    args = parser.parse_args()
    ini2csv(args.ini_filename, args.csv_filename)
