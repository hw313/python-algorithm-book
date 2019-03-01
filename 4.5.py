# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     4.5
   Description :
   Author :       huang wei
   date：          2019/1/11
-------------------------------------------------
   Change Activity:
                   2019/1/11:
-------------------------------------------------
"""
__author__ = 'huang wei'


def get2num(arr):
    map = {}
    for xx in arr:
        if xx not in map:
            map[xx] = 1
        elif map[xx] == 1:
            map[xx] -= 1
        elif map[xx] == 0 :
            map[xx] += 1

    for key, values in map.items():
        if values % 2 == 1:
            print(key)

arr = [3,5,6,6,5,7,2,2,]
get2num(arr)