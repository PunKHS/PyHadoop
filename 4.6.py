#!/usr/bin/python
import sys

list = {}

for line in open('4.6.txt', 'r'):
    words = line.strip().split(',')
    # print (words[1])
    for line2 in words[1].split('\s'):
        # print(words[0], line2[0])
        list = {words[0], line2[0]}

    # myset = set(list)
        print(list)

