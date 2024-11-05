#!/usr/bin/env python3
"""function that removes requested directories
    within Hadoop filesystem
"""


from snakebite.client import Client


client = Client('localhost',9000)

def deletedir(l):
    """removes directories listed in l

    l = list of directory names
        list of strings"""
    results = list(client.rmdir(list(reversed(l))))
    for item in results: print(item)
    return results
