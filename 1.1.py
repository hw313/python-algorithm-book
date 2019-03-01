# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     01
   Description :
   Author :       huang wei
   date：          2018/11/18
-------------------------------------------------
   Change Activity:
                   2018/11/18:
-------------------------------------------------
"""
__author__ = 'huang wei'
class LNode:
    def __init__(self):
        self.data=None
        self.next=None

def reverse(head):
    if head is None or head.next is None:
        return
    pre=None
    cur=None
    next=None
    cur=head.next
    next=cur.next
    cur.next=None
    pre=cur
    cur=next
    while cur.next is not None:
        next=cur.next
        cur.next=pre
        pre=cur
        cur=next
    cur.next=pre
    head.next=cur

def Reverse(head):
    if head is None or head.next is None:
        return
    cur=head.next.next
    head.next.next=None
    while cur is not None:
        next=cur.next
        cur.next = head.next
        head.next=cur

        cur=next

i=1
head=LNode()
head.next=None
temp=None
cur=head

while i<8:
    temp=LNode()
    temp.data=i
    temp.next=None
    cur.next=temp
    cur=temp
    i+=1

cur=head.next
print("before reverse")
while cur is not None:
    print(cur.data)
    cur=cur.next

Reverse(head)
cur=head.next
print("after reverse")

while cur is not None:
    print(cur.data)
    cur=cur.next