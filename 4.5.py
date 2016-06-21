#!/usr/bin/python
import sys


# for line in open('4.5.txt', 'r'):
for line in sys.stdin:
    words = line.strip().split('\t')
    for line2 in words[1].split(','):
        print (words[0] + ',' + line2 + '\t1')