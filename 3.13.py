# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     3.13
   Description :
   Author :       huang wei
   date：          2019/2/23
-------------------------------------------------
   Change Activity:
                   2019/2/23:
-------------------------------------------------
"""
__author__ = 'huang wei'
class BiTnode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


def findamax(root, Sum):
    global pre
    if root is None:
        return
    Sum += root.data
    if root.lchild is None and root.rchild is None:
        print("该路径的sum 为：{} ".format(Sum))
        if Sum > pre:
            pre = Sum
    findamax(root.lchild, Sum)
    findamax(root.rchild, Sum)
    Sum -= root.data
    return pre

class TreeNode:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None

def constructTree():
    root = TreeNode()
    node1 = TreeNode()
    node2 = TreeNode()
    node3 = TreeNode()
    node4 = TreeNode()

    root.val = 10
    node1.val = 5
    node2.val = 12
    node3.val = 4
    node4.val = 7

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = None
    node2.right = None
    node3.left = node3.right = node4.left = node4.right = None

    return root


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.sum = 0
        self.path = []
        self.res = []
    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return
        self.sum += root.val
        self.path.append(root.val)
        if self.sum == expectNumber and root.left is None and root.right is None:
            self.res.append(self.path)
            print(self.res)
        self.FindPath(root.left,expectNumber)
        self.FindPath(root.right,expectNumber)
        self.path = self.path[:-1]
        self.sum -= root.val

from collections import deque
class hh:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        q = deque()
        if root is None:
            return
        q.append(root)
        while (len(q)) > 0:
            tmp = q.popleft()
            print(tmp.val)
            if tmp.left is not None:
                q.append(tmp.left)
            if tmp.right is not None:
                q.append(tmp.right)


class wori:
    def FindContinuousSequence(self, tsum):
        # write code here
        max = int(tsum / 2) + 1
        start = 1

        res = []
        for i in range(start, max):
            for j in range(i + 1, max + 1):
                if sum(list(range(i, j + 1))) < tsum:
                    continue
                elif sum(list(range(i, j + 1)) == tsum):
                    res.append(list(range(i, j+1)))
                else:
                    break
        return res

if  __name__ == "__main__":
    root = constructTree()
    xx=hh()
    xx.PrintFromTopToBottom(root)

    made=wori()
    made.FindContinuousSequence(100)

