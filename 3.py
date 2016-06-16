#!/usr/bin/python

import sys

# Maper
for line in sys.stdin:
    for token in line.strip().split(" "):
        if token: print(token + '\t1')

# Reduser
(lastKey, sum) = (None, 0)
for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    if lastKey and lastKey != key:
        print(lastKey + '\t' + lastKey.count())
        (lastKey, sum) = (key, int(value))
    else:
        (lastKey, sum) = (key, sum + int(value))
if lastKey:
    print(lastKey + '\t' + str(sum))
