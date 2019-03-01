# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     05
   Description :
   Author :       huang wei
   date：          2018/11/25
-------------------------------------------------
   Change Activity:
                   2018/11/25:
-------------------------------------------------
"""
__author__ = 'huang wei'


class LNode:
    def __init__(self):
        self.data = None
        self.next = None


def find_middle(head):

    slow = head
    quick = head
    while True:
        if quick.next is not None and quick.next.next is not None:
            quick = quick.next.next
            slow = slow.next
        else:
            last = slow
            slow = slow.next
            last.next = None
            break

    return slow


def reverse(xx):
    """对没有头结点的单链表就地逆序"""
    if xx.next is None:
        return xx
    if xx.next.next is None:
        first = xx
        last = xx.next
        last.next = first
        first.next = None
        return last

    pre = xx

    cur = xx.next
    pre.next = None
    while True:

        Next = cur.next

        cur.next = pre
        pre = cur
        cur = Next
        if cur.next is None:
            cur.next = pre
            break
    return cur


def add(head, mid):
    p = head.next

    while p.next is not None:
        p_next = p.next
        q_next = mid.next
        p.next = mid
        mid.next = p_next
        p = p_next
        mid = q_next
    if mid:
        p.next = mid
    return head


def init():
    head = LNode()
    a, b, c, d, e, f, g = LNode(), LNode(), LNode(), LNode(), LNode(), LNode(), LNode()
    head.next = a
    a.data, a.next = 1, b
    b.data, b.next = 3, c
    c.data, c.next = 4, d
    d.data, d.next = 5, e
    e.data, e.next = 6, f
    f.data, f.next = 7, g
    g.data, g.next = 8, None
    return head, a, b, c, d, e, f, g


head, a, b, c, d, e, f , g= init()
print(a.data, b.data, c.data, d.data, e.data, f.data, g.data)

mid = find_middle(head)
rev_mid = reverse(mid)

# print(rev_mid.data)

new_head = add(head, rev_mid)
while new_head is not None:
    print(new_head.data)
    new_head = new_head.next














