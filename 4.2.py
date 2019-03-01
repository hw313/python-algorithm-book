# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     4.2
   Description :
   Author :       huang wei
   date：          2018/12/3
-------------------------------------------------
   Change Activity:
                   2018/12/3:
-------------------------------------------------
"""
__author__ = 'huang wei'
import math

def find_minmax(array):
    if len(array) == 0:
        return 0, 0
    if len(array) == 1:
        Min, Max = array[0], array[0]
        return Min, Max
    elif len(array) == 2:
        Min, Max = min(array[0], array[1]), max(array[0], array[1])
        return Min, Max
    Min_l ,Max_l = find_minmax(array[:math.ceil(len(array)/2)])
    Min_r, Max_r = find_minmax(array[math.ceil(len(array) / 2):])
    return min(Min_l,Min_r), max(Max_l,Max_r)







array = [7, 3, 19, 40, 4, 7, 1]

a, b =find_minmax(array)
print(a, b)

