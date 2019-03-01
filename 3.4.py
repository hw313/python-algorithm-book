# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     3.4
   Description :
   Author :       huang wei
   date：          2019/2/22
-------------------------------------------------
   Change Activity:
                   2019/2/22:
-------------------------------------------------
"""
__author__ = 'huang wei'
import math

class BitNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


def find_max_tree(root):
    max_sum = -100
    if root is None:
        return 0
    l_sum = find_max_tree(root.lchild)
    r_sum = find_max_tree(root.rchild)
    if l_sum+r_sum+root.data > max_sum:
        max_sum = l_sum+r_sum+root.data
        print(l_sum, r_sum, root.data)
    return l_sum+r_sum+root.data


def array2tree(array, left, right):
    if left > right:
        return
    mid = math.ceil((left+right)/2)
    root = BitNode()
    root.data = array[mid]
    root.lchild = array2tree(array, left, mid-1)
    root.rchild = array2tree(array, mid+1, right)
    return root


if __name__ == "__main__":
    arr = [-1, 3, 9, 6, -7]
    root = array2tree(arr, 0, len(arr)-1)
    res = find_max_tree(root)
    print(res)