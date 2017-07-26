import csv
import re

SOURCE = './dw-nominate/S{}_members.csv'
OUT_DIR = './queries/namelist_S{}.txt'

# The first 4 vectors are used to define the projection axes, in the order of:
# [positive_x_axis, negative_x_axis, positive_y_axis, negative_y_axis]
names = ['conservative', 'liberal', 'good', 'bad']

for cgrs_sess in range(95, 115):
    with open(SOURCE.format(cgrs_sess)) as f:
        reader = csv.DictReader(f)
        for row in reader:
            names.append(row['bioname'])
    with open(OUT_DIR.format(cgrs_sess), 'w') as f:
        for name in names:
            name = re.sub(',.*', '', name)
            name = re.sub(' ', '-', name)
            f.write(name.lower() + '\n')
    names = ['conservative', 'liberal', 'good', 'bad']