#!/usr/bin/python3

import sys
import csv

# Read from standard input
for line in sys.stdin:
    reader = csv.reader([line])
    # Strip whitespace and split the line into fields
    line = line.strip()

    try:
        # Extract the fields from the CSV
        id, company, totalyearlycompensation = next(reader)

        # Print the output in the required format
        print(f"{id}\t{company},{totalyearlycompensation}")
    except ValueError:
        # if line does not have enough fields
        print("something failed")
        continue
