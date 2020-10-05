import csv
import glob
import os

input_path = './cart/data/'

file_counter = 0
for input_file in glob.glob(os.path.join(input_path, '*.csv')):
    row_counter = 1
    with open(input_file, 'rt', encoding='UTF8', newline='') as csv_in_file:
        freader = csv.reader(csv_in_file)
        header = next(freader)
        for row in freader:
            row_counter += 1
    print('{0!s}: \t{1:d} rows \t{2:d} columns'.format(os.path.basename(input_file),row_counter,len(header)))
    file_counter += 1

print('Number of files: {0:d}'.format(file_counter))