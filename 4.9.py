# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     4.9
   Description :
   Author :       huang wei
   date：          2019/1/11
-------------------------------------------------
   Change Activity:
                   2019/1/11:
-------------------------------------------------
"""
__author__ = 'huang wei'


def find_minabs(array):
    if not array:
        return None
    if array[0] > 0:
        return array[0]
    if array[-1] < 0:
        return array[-1]
    mid = int(len(array)/2)
    if array[mid] < 0 and array[mid+1] > 0:
        return array[mid] if abs(array[mid])<abs(array[mid+1]) else array[mid+1]
    elif array[mid] < 0 and array[mid+1] < 0:
        return find_minabs(array[mid+1:])
    elif array[mid] > 0:
        return find_minabs(array[:mid])
    elif array[mid] ==0 or array[mid+1] == 0:
        return 0
array=[-10,-5,-2,0,7,15,20]
print(find_minabs(array))
