#!/usr/bin/env python3
"""recieves a file list and saves it
    within Hadoop filesystem
"""


# import requests
from snakebite.client import Client


# response = (requests.get("https://raw.githubusercontent.com/Jabulani-N/atlas-hadoop/refs/heads/main/hadoop_project/assignment_files/lao.txt"))
client = Client('localhost',9000)

def download(l):
    """
    saves files listed in l

    l = list of file names
        list of strings
    """
    results = list(client.copyToLocal(l, "/tmp"))
    for item in results: print(item)
    return results
