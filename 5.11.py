# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     5.11
   Description :
   Author :       huang wei
   date：          2019/2/23
-------------------------------------------------
   Change Activity:
                   2019/2/23:
-------------------------------------------------
"""
__author__ = 'huang wei'
# import math


def str2int(strs):
    order = ['d', 'g', 'e', 'c', 'f', 'b', 'o', 'a']
    map1 = {}
    for xx in order:
        map1[xx] = order.index(xx) + 1

    value = 0
    for i in range(len(strs)):
        if strs[i] in order:
            value = 10 * value + map1[strs[i]]
        else:
            map1[strs[i]] = 0
            value = 10 * value + map1[strs[i]]
    return value


if __name__ == "__main__":
    input = ['bed', 'dog', 'dear', 'eye']
    maxlen = max([len(xx) for xx in input])

    map = {}
    for xx in input:
        map[xx] = str2int(xx)
    for xx in input:
        map[xx] = map[xx] * pow(10, maxlen-len(xx))
    print(str2int('eye'))
    res = sorted(map.items(), key=lambda x: x[1])
    print(res)
    res = [item[0] for item in res]
    print(res)
