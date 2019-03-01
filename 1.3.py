# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     03
   Description :
   Author :       huang wei
   date：          2018/11/20
-------------------------------------------------
   Change Activity:
                   2018/11/20:
-------------------------------------------------
"""
__author__ = 'huang wei'


class LNode:
    def __init__(self):
        self.data = None
        self.next = None

    def __str__(self):
        return "self.next = {}, self.data= {}".format(self.next, self.data)


def add(n1, n2):
    if n1 is None or n1.next is None:
        return n2
    if n2 is None or n2.next is None:
        return n1

    p1, p2 = n1.next, n2.next
    head = LNode()
    new = head
    c = 0
    while p1 is not None and p2 is not None:
        temp = p1.data + p2.data + c
        c = int(temp/10)
        p3 = LNode()
        p3.data = temp % 10
        new.next = p3
        new = p3
        p1 = p1.next
        p2 = p2.next

    if p1 is None:
        while p2 is not None:
            temp = p2.data + c
            c = int(temp / 10)
            p3 = LNode()
            p3.data = temp % 10
            new.next = p3
            new = p3
            p2 = p2.next

    if p2 is None:
        while p1 is not None:
            temp = p1.data + c
            c = int(temp / 10)
            p3 = LNode()
            p3.data = temp % 10
            new.next = p3
            new = p3
            p1 = p1.next

    if c == 1:
        tmp = LNode()
        tmp.data = 1
        tmp.next = None
        new.next = tmp

    return head


def init():
    a, b, c, d, e, f = LNode(), LNode(), LNode(), LNode(), LNode(), LNode()
    a.data, a.next = 1, b
    b.data, b.next = 3, c
    c.data, c.next = 4, d
    d.data, d.next = 5, e
    e.data, e.next = 5, f
    f.data, f.next = 7, None
    return a, b, c, d, e, f


def resort(n1, n2):
    if n1 is None or n1.next is None:
        return n2
    if n2 is None or n2.next is None:
        return n1
    head = LNode()
    new = head
    while n1 is not None and n2 is not None:
        if n1.data <= n2.data:
            cur = LNode()
            cur.data = n1.data
            new.next = cur
            new = cur
            n1 = n1.next
        else:
            cur = LNode()
            cur.data = n2.data
            new.next = cur
            new = cur
            n2 = n2.next
    while n1:
        cur = LNode()
        cur.data = n1.data
        new.next = cur
        new = cur
        n1 = n1.next
    while n2:
        cur = LNode()
        cur.data = n2.data
        new.next = cur
        new = cur
        n2 = n2.next
    return head




if __name__ == "__main__":
    i = 1
    head1 = LNode()
    head2 = LNode()
    tmp = None
    cur = head1
    while i < 7:
        tmp = LNode()
        tmp.data = i+2
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    # while head1 is not None:
    #     print(head1.data,end="")
    #     head1 = head1.next
    cur = head2
    i = 4
    while i < 9:
        temp = LNode()
        temp.data = i
        cur.next = temp
        cur = temp
        i += 1
    print("")
    # while head2 is not None:
    #     print(head2.data,end="")
    #     head2 = head2.next

    print("resort")
    new_head = resort(head1.next, head2.next)
    while new_head is not None:
        print(new_head.data)
        new_head = new_head.next











