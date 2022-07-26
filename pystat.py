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


def return_mean(list_in):
    mean = sum(list_in) / len(list_in)
    return mean


def return_mode(list_in):
    highest_occurrence = 0
    mode = None
    if_multiple_modes = ()
    for num in list_in:
        temp_count = 0
        if list_in.count(num) > highest_occurrence:
            highest_occurrence = list_in.count(num)
            mode = num
            if_multiple_modes = []
        if list_in.count(num) == highest_occurrence and num not in if_multiple_modes:
            if_multiple_modes.append(num)
    if len(if_multiple_modes) > 1 and highest_occurrence > 1:
        return set(if_multiple_modes)
    elif len(if_multiple_modes) > 1 and highest_occurrence == 1:
        return None
    else:
        return mode


def return_median(list_in):
    mid = len(list_in) // 2
    if len(list_in) % 2 == 0:
        return (list_in[mid-1], list_in[mid])
    else:
        return list_in[mid]


def return_variance(list_in):
    n = len(list_in)
    mean = sum(list_in) / n
    deviations = [(x - mean) ** 2 for x in list_in]
    return sum(deviations) / n


def return_covariance(list_in1, list_in2):
    mean1 = return_mean(list_in1)
    mean2 = return_mean(list_in2)
    n = len(list_in1) + len(list_in2)
    sigma = [(x - mean1)*(y - mean2) for x, y in zip(list_in1, list_in2)]
    return sum(sigma) / n


def return_stddev(list_in):
    return math.sqrt(return_variance(list_in))


def return_stderr(list_in):
    return  return_stderr(list_in) / math.sqrt(len(list_in))


def return_correlation(list_in1, list_in2):
    # covariance(l1, l2) / (stddev(l1) * stddev(l2))
    covariance = return_covariance(list_in1, list_in2)
    dev1 = return_stddev(list_in1)
    dev2 = return_stddev(list_in2)
    return covariance / (dev1 * dev2)



test_list = [1, 2,  3,  4,  5, 8]
test_list2 = [3, 5, 7, 9, 13, 17]
mode = return_median(test_list)
print(f"{mode}")
variance = return_variance(test_list)
print(variance)
print(return_mean(test_list))
print(return_stddev(test_list))
print(return_covariance(test_list, test_list2))
print('correlation')
print(return_correlation(test_list, test_list2))
# file = open('dataOne.csv')
# csvreader = csv.reader(file)
# header = []
# header = next(csvreader)
# print(header)

# file_name = 'dataZero.csv'
# csv_file = open_file(file_name)
# csvreader = csv.reader(csv_file)
# header = extract_header(csvreader)
# ## print(header)
# rows = extract_rows(csvreader)
# ## print(rows)
# ## print(header)





## extraction complete
# csv_file.close()



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("missing file name")
        exit()
    file_name = sys.argv[1]

   ## file_name = 'dataThree.csv'
    if is_csv(file_name):
        csvreader = csv.reader(file_name)
        csv_header = extract_header(csvreader)
        print(csv_header)
    else:
        print("needs .csv at the end!")
        exit()
    rows = extract_rows(csvreader)
    ## this is sloppy, but it works for a list of lists, where each nested list has 2 elements.
    conversion = list(map(list, zip(*rows)))
    x_list_string, y_list_string = conversion
    x_list = []
    y_list = []
    ## converting strings to floats for calculations. **Find the better way to do this**
    for num in range(0, len(x_list_string)):
        x_list.append(float(x_list_string[num]))
    for num in range(0, len(y_list_string)):
        y_list.append(float(y_list_string[num]))
    mean_x = return_mean(x_list)
    mean_y = return_mean(y_list)
    print(f"The mean of x's is {mean_x}")
    print(f"The mean of y's is {mean_y}")
    mode_x = return_mode(x_list)
    mode_y = return_mode(y_list)
    print(f"The mode of x's is {mode_x}")  #may need a loop here to print out multiple modes if they occur.
    print(f"The mode of y's is {mode_y}")
    median_x = return_median(x_list)
    median_y = return_median(y_list)
    print(f"The median of x's is {median_x}")
    print(f"The median of y's is {median_y}")

    # print(x_list)
    # print(y_list)