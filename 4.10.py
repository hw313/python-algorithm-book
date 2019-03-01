# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     4.10
   Description :
   Author :       huang wei
   date：          2019/2/24
-------------------------------------------------
   Change Activity:
                   2019/2/24:
-------------------------------------------------
"""
__author__ = 'huang wei'

def solve(arr):
    sum = 0
    sumMax = -1000
    for i in range(len(arr)):
        if sum + arr[i] < 0:
            if sum + arr[i] >sumMax:
                sumMax = sum +arr[i]
            sum = 0
        else:
            sum += arr[i]
            if sum > sumMax:
                sumMax = sum
    print(sumMax)


if __name__  == "__main__":
    solve([1,-2,4,8,-4,7,-1,-5])
    solve([-2,1])

