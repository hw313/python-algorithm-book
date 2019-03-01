# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     4.12
   Description :
   Author :       huang wei
   date：          2019/2/24
-------------------------------------------------
   Change Activity:
                   2019/2/24:
-------------------------------------------------
"""
__author__ = 'huang wei'
import numpy as np


def rotate(array):
    n = array.shape[0]
    new_array = np.zeros(shape=array.shape)
    for i in range(n):
        new_array[i] = array[i][::-1]
    for index_sum in range(2*n-1):

        for i in range(n):
            j = index_sum - i
            if j >= 0 and j <n:
                print(new_array[i][j],end =" ")
            elif j < 0:
                break
        print("")

array = np.arange(9) +1
array = array.reshape(3,3)
rotate(array)

