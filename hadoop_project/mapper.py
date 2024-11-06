#!/usr/bin/python3

import sys
import csv

# Read from standard input
reader = csv.reader(sys.stdin,delimiter=',')
counter = 0
completed_ids = []
for line in reader:
    # Strip whitespace and split the line into fields
    # line = line.strip()

    try:
        # Extract the fields from the CSV
        id, company, totalyearlycompensation = line[0], line[1], line[3]
        if id not in completed_ids:
            # Print the output in the required format
            print(f"{id}\t{company},{totalyearlycompensation}")
            completed_ids.append(id)
            counter += 1

    except IndexError:
        # if line does not have correct fields
        print("missing field")
        # continue
    # there are thousands of entries, we don't need to print all
    if counter > 30: break
