"""
Program are checking the most popular crimes from Chicago database
since 2001 to nowadays.
Database got .csv format.
"""

import csv

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

lst = {}
with open("D:\Code\Stepik\example.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[5] not in lst:
            lst[row[5]] = 0
        else:
            lst[row[5]] += 1

print(get_key(lst, max(lst.values())))

