# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     02
   Description :
   Author :       huang wei
   date：          2018/11/19
-------------------------------------------------
   Change Activity:
                   2018/11/19:
-------------------------------------------------
"""
__author__ = 'huang wei'


class LNode:
    def __init__(self):
        self.data = None
        self.next = None

    def __str__(self):
        return "self.data={},self.next={}".format(self.data, self.next)


def delete(head):
    if head is None or head.next is None:
        return
    temp = [head.data]

    cur = head.next
    pre = head

    while cur.next is not None:

        if cur.data not in temp:
            temp.append(cur.data)
            pre = cur
            cur = cur.next
        else:
            pre.next = cur.next
            cur = cur.next
    if cur.data in temp:
        pre.next = None




def init():
    a, b, c, d, e, f = LNode(), LNode(), LNode(), LNode(), LNode(), LNode()
    a.data, a.next = 1, b
    b.data, b.next = 3, c
    c.data, c.next = 4, d
    d.data, d.next = 5, e
    e.data, e.next = 5, f
    f.data, f.next = 7, None
    return a, b, c, d, e, f


a, b, c, d, e, f = init()
print(a.data, b.data, c.data, d.data, e.data, f.data)

delete(a)
cur = a

while cur is not None:
    print(cur.data, end=' ')
    cur = cur.next







