#!/usr/bin/env python3
"""function that creates requested directories
    within Hadoop filesystem
"""


from snakebite.client import Client


client = Client('localhost',9000)



def createdir(l):
    """
    creates directories listed in l

    l = list of directory names
        list of strings
    """
    # treating the generator client makes "consumes" the generator
    results = list(client.mkdir(l,True))
    # we could have also just printed each item via for loop
    print(results)
    return results


def old_createdir(l):
    """
    creates directories listed in l

    l = list of directory names
        list of strings
    """
    any_failures = False
    for name in l:
        response = client.mkdir([name])
        print("making", name)
        if response['status'] != 0:
            any_failures = True
            print("failed this make")
            print("response: ", response['status'])
