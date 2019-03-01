# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     3.10
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


Sum = 0
res = []


def solve(root):
    if root is None:
        return
    global Sum
    global res
    Sum += root.data
    res.append(root.data)
    if root.lchild is None and root.rchild is None and Sum == ans:
        print(res)
        return
    solve(root.lchild)
    solve(root.rchild)
    res = res[: -1]
    Sum -= root.data

def constructTree():
    root = BiTnode()
    node1 = BiTnode()
    node2 = BiTnode()
    node3 = BiTnode()
    node4 = BiTnode()
    root.data = 6
    node1.data = 3
    node2.data = -7
    node3.data = -1
    node4.data = 9
    root.lchild = node1
    root.rchild = node2
    node1.lchild = node3
    node1.rchild = node4
    node2.lchild = node2.rchild = node3.lchild = node3.rchild = node4.lchild = node4.rchild = None
    return root


if __name__ == "__main__":
    root = constructTree()
    ans = input("请输入你要的值")
    # ans = -1
    solve(root)
    print(ans)


