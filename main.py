import csv
import sys


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def write_csv_file(file_name: str) -> None:
    with open(file_name, 'w', newline = '') as csvfile:
        # prepare the header row
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()

        # write a few data rows to the CSV file
        writer.writerow({'first_name': 'Mark', 'last_name': 'Grohman'})
        writer.writerow({'first_name': 'Fred', 'last_name': 'Morrison'})
        writer.writerow({'first_name': 'John', 'last_name': 'Smith'})


def echo_csv_file(file_name: str) -> None:
    with open(file_name) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['first_name']} {row['last_name'].strip()} ")


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    filename = 'names.csv'
    write_csv_file(filename)
    echo_csv_file(filename)
