# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     3.3
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
from collections import deque

class BitNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


class queue:
    def __init__(self):
        self.nums = []
        self.length = len(self.nums)

    def push(self, data):
        self.nums.append(data)

    def pop(self):
        item = self.nums[0]
        self.nums = self.nums[1:]
        return item


def array2tree(array, left, right):
    if left > right:
        return
    mid = math.ceil((left+right)/2)
    root = BitNode()
    root.data = array[mid]
    root.left = array2tree(array, left, mid-1)
    root.right = array2tree(array, mid+1, right)
    return root


def printMidorder(root):
    if root.left is not None:
        printMidorder(root.left)
    print(root.data)
    if root.right is not None:
        printMidorder(root.right)

def printfloororder(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    while len(q) > 0:
        item = q.popleft()
        print(item.data)
        if item.left is not None:
            q.append(item.left)
        if item.right is not None:
            q.append(item.right)


if __name__=="__main__":
    arr = [i + 1 for i in range(10)]
    root = array2tree(arr, 0, len(arr)-1)
    printfloororder(root)