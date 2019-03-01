# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     4.13
   Description :
   Author :       huang wei
   date：          2019/2/24
-------------------------------------------------
   Change Activity:
                   2019/2/24:
-------------------------------------------------
"""
__author__ = 'huang wei'


def qucik_sort(array, left, right):
    # if left >= right:
    #     return array
    key = array[left]
    low = left
    high = right
    while low < high:
        while low < high and array[high] >= key:
            high -= 1

        array[low] = array[high]
        while low < high and array[low] <= key:
            low += 1

        array[high] = array[low]
    array[low] = key
    # qucik_sort(array, left, low-1)
    # qucik_sort(array, low+1, right)

    return low

array = [5,7,4,6,8]
mid = 2
xx = qucik_sort(array, 0, len(array) - 1)
while True:

    if xx == mid:
        print(array[mid])
        break
    elif xx < mid:
        xx= qucik_sort(array,xx+1,len(array)-1)
    elif xx >mid:
        xx = qucik_sort(array,0,xx-1)






