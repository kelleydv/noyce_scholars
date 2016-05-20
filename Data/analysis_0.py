"""
Reads in a .csv file and outputs each case.
To run this: `python analysis_0.py yourfile.csv`
"""

import csv
import sys

filename = sys.argv[1]
with open(filename, 'r') as f:
    data = csv.reader(f)

    for case in data:
        print(case)
