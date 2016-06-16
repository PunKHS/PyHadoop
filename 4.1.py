#!/usr/bin/python
import sys

for line in open('4.1.txt', 'r'):
# for line in sys.stdin:
    dic = {}
    words = line.strip().split()
    for word in words:
        (key, value) = (word, word.count(word))
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = value
    for i in dic:
        print(i + '\t' + str(dic[i]))