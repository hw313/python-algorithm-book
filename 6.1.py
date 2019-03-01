# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     6.1
   Description :
   Author :       huang wei
   date：          2019/1/11
-------------------------------------------------
   Change Activity:
                   2019/1/11:
-------------------------------------------------
"""
__author__ = 'huang wei'


def ispower(n):
    low = 0
    high = n
    while low <= high:
        mid = (low+high)//2
        if mid**2 < n :
            low = mid + 1
        elif mid**2 == n:
            return 1
        else:
            high = mid - 1
    return -1
print(ispower(28))