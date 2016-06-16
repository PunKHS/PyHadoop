#!/usr/bin/python
import sys, re

pattern = re.compile(r"([\w|.]+)\s+(\d+)")
dic = dict()
avg_dic = dict()

for line in open('4.3.txt', 'r'):
# for line in sys.stdin:
    m = re.search(pattern, line)
    key = m.group(1)
    value = int(m.group(2))
    if key in dic:
        dic[key].append(value)
    else:
        dic[key] = [value]
# print (dic)
for k in dic:
    avg_dic[k] = sum(dic[k]) / int(len(dic[k]))
# print(avg_dic)
for i in avg_dic:
    print(i + '\t' + str(int(avg_dic[i])))
