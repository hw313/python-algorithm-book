# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     04
   Description :
   Author :       huang wei
   date：          2018/11/23
-------------------------------------------------
   Change Activity:
                   2018/11/23:
-------------------------------------------------
"""
__author__ = 'huang wei'

"""找到单链表倒数第k个结点
对链表进行左旋
"""


class LNode:
    def __init__(self):
        self.data = None
        self.next = None


def find_k(head, k):
    p = head
    q = head
    while k > 1:
        k -= 1
        if p is not None:
            p = p.next
        else:
            return None

    while p.data and p.next is not None:
        p = p.next
        q = q.next

    print(q.data)
    return p, q


def left_reverse(head, k):
    new_head = LNode()
    p, q = find_k(head, k)
    p, xx = find_k(head, k + 1)
    new_head.next = q
    p.next = head
    xx.next = None

    return new_head


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
find_k(a, 1)
new_head = left_reverse(a, 1)
start = new_head.next

while start is not None:
    print(start.data, end='')
    start = start.next


  



