# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     3.11
   Description :
   Author :       huang wei
   date：          2019/2/23
-------------------------------------------------
   Change Activity:
                   2019/2/23:
-------------------------------------------------
"""
__author__ = 'huang wei'

from collections import deque
class BiTnode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


def reverse(root):
    if root is None:
        return
    root.lchild, root.rchild = root.rchild, root.lchild
    reverse(root.lchild)
    reverse(root.rchild)



def Reverse(root):
    q = deque()
    q.append(root)
    while len(q) > 0:
        res = q.popleft()
        res.lchild, res.rchild = res.rchild, res.lchild
        if res.lchild:
            q.append(res.lchild)
        if res.rchild:
            q.append(res.rchild)

def printOrder(root):
    q = deque()
    q.append(root)
    while len(q) > 0:
        res = q.popleft()
        print(res.data)
        if res.lchild:
            q.append(res.lchild)
        if res.rchild:
            q.append(res.rchild)


def constructTree():
    root = BiTnode()
    node1 = BiTnode()
    node2 = BiTnode()
    node3 = BiTnode()
    node4 = BiTnode()
    node5 = BiTnode()
    node6 = BiTnode()
    root.data = 4
    node1.data = 2
    node2.data = 6
    node3.data = 1
    node4.data = 3
    node5.data = 5
    node6.data = 7
    root.lchild = node1
    root.rchild = node2
    node1.lchild = node3
    node1.rchild = node4
    node2.lchild = node5
    node2.rchild = node6
    node6.lchild = node6.rchild = node5.lchild = node5.rchild = node3.lchild = node3.rchild = node4.lchild = node4.rchild = None
    return root



if  __name__ == "__main__":
    root = constructTree()
    printOrder(root)
    reverse(root)
    printOrder(root)


