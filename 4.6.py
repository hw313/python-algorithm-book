# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     4.6
   Description :
   Author :       huang wei
   date：          2019/1/11
-------------------------------------------------
   Change Activity:
                   2019/1/11:
-------------------------------------------------
"""
__author__ = 'huang wei'


def find_smallest_k(arr, k):
    length = len(arr)
    if length == 1:
        return arr[0]
        # print(arr[0])
    if k > length:
        return -1
    tmp = arr[0]
    left, right = [], []
    for i in range(1, length):
        if arr[i] <= tmp:
            left.append(arr[i])
        else:
            right.append((arr[i]))
    if len(left) == k-1:
        return tmp
        # print(tmp)
    elif len(left) < k-1:
        return find_smallest_k(right, k-1-len(left))
    else:
        return find_smallest_k(left, k)

arr = [4,0,1,0,2,3]
hehe = find_smallest_k(arr, 3)
print(hehe)

