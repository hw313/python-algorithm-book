# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     3.2
   Description :
   Author :       huang wei
   date：          2018/12/21
-------------------------------------------------
   Change Activity:
                   2018/12/21:
-------------------------------------------------
"""
__author__ = 'huang wei'
import math


class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None





def arraytotree(arr, start, end):
    if end >= start:
        root = BiTNode()
        mid = math.ceil(start + (end - start)/2)
        root.data = arr[mid]
        root.lchild = arraytotree(arr, start, mid-1)
        root.rchild = arraytotree(arr, mid+1, end)
    else:
        root = None
    return root

def printTree(root):
    if root is None:
        return -1
    if root.lchild is not None:
        printTree(root.lchild)

    if root.rchild is not None:
        printTree(root.rchild)
    print(root.data)


if __name__ =="__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr=[1,2,3]

    root = arraytotree(arr, 0, 2)
    print(printTree(root))

