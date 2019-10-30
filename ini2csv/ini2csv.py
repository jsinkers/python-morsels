import argparse
import configparser
import csv


def ini2csv(ini_filename, csv_filename, collapsed):
    config = configparser.ConfigParser()
    config.read(ini_filename)

    with open(csv_filename, 'w', newline='') as f:
        if not collapsed:
            csv_writer = csv.writer(f)
            for section in config.sections():
                for (key, value) in config[section].items():
                    csv_writer.writerow([section, key, value])
        elif collapsed:
            section = config.sections()[0]
            field_names = ["header"]
            field_names += list(config[section].keys())

            csv_dictwriter = csv.DictWriter(f, fieldnames=field_names)
            csv_dictwriter.writeheader()
            for section in config.sections():
                row_dict = config[section]
                row_dict["header"] = section
                csv_dictwriter.writerow(row_dict)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert an INI-like file to a CSV-like file')
    parser.add_argument(dest='ini_filename', metavar='ini_filename')
    parser.add_argument(dest='csv_filename', metavar='csv_filename')
    parser.add_argument('--collapsed', action='store_true', dest='collapsed', default=False)
    args = parser.parse_args()
    ini2csv(args.ini_filename, args.csv_filename, args.collapsed)
