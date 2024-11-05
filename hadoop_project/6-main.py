#!/usr/bin/python3


download = __import__('6-download').download


l = ["/holbies/input/lao.txt"]
download(l)
lao =  open("/tmp/lao.txt", "r")
print(lao.read())
lao.close()
