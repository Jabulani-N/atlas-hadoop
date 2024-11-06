#!/usr/bin/python3

import sys
import csv

# Read from standard input
reader = csv.reader(sys.stdin,delimiter=',')
for line in reader:
    # Strip whitespace and split the line into fields
    # line = line.strip()

    try:
        # Extract the fields from the CSV
        # id, company, totalyearlycompensation = line

        # Print the output in the required format
        print(f"{line[0]}\t{line[1]},{line[2]}")
    except ValueError:
        # if line does not have enough fields
        print("something failed")
        continue
