import math, csv
import sys


def is_csv(filename):
    return '.csv' in filename


def open_file(file_name):
    return open(file_name)


def extract_header(reader):
    header = next(reader)
    return header


def extract_rows(reader):
    rows = []
    for row in reader:
        rows.append(row)
    return rows


def count_of(list_in):
    count_x = len(list_in)
    count_y = len(list_in)
    return count_x, count_y

# file = open('dataOne.csv')
# csvreader = csv.reader(file)
# header = []
# header = next(csvreader)
# print(header)

file_name = 'dataZero.csv'
csv_file = open_file(file_name)
csvreader = csv.reader(csv_file)
header = extract_header(csvreader)
# print(header)
rows = extract_rows(csvreader)
print(rows)
print(header)


#extraction complete
csv_file.close()



# if __name__ == '__main__':
    # if len(sys.argv) != 2:
    #     print("missing file name")
    #     exit()
    # file_name = sys.argv[1]

    # file_name = 'dataThree.csv'
    # if is_csv(file_name):
    #     csvreader = csv.reader(file_name)
    #     csv_header = extract_header(csvreader)
    #     print(csv_header)
    # else:
    #     print("needs .csv at the end!")
    #     exit()