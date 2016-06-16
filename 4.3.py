#!/usr/bin/python
import sys, re

pattern = re.compile(r"([\w|.]+)\s+(\d+)")
dic = {}
avg_dic = {}

for line in open('text_4.3.txt', 'r'):
# for line in sys.stdin:
#     value= []
    m = re.search(pattern, line)
    # (key, value) = (m.group(1), m.group(2))
    key = m.group(1)
    if key in dic:
        # dic[key] = value
        dic[key].append(m.group(2))


    print (dic)
# for k,v in dic:
#     avg_dic[k] = sum(v) / float(len(k))
# print(avg_dic)



    # if key in dic:
    #     dic[key] = dic.values() + value
    # else:
    #     dic[key] = value

# for i in dic:
#     print(i + '\t' + str(dic[i]))