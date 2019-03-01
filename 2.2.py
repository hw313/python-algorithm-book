# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     06
   Description :
   Author :       huang wei
   date：          2018/11/26
-------------------------------------------------
   Change Activity:
                   2018/11/26:
-------------------------------------------------
"""
__author__ = 'huang wei'


class EZ_queue:
    def __init__(self):
        self.nums = []

    def get_size(self):
        return len(self.nums)

    def is_empty(self):
        return self.get_size() == 0

    def see_front(self):
        if self.is_empty() is True:
            print("no items")
            return
        return self.nums[0]

    def see_rear(self):
        if self.is_empty() is True:
            print("no items")
            return
        return self.nums[-1]

    def push(self, item):
        self.nums.append(item)

    def pop(self):
        tmp = self.nums[0]
        self.nums = self.nums[1:]
        return tmp

    def __str__(self):
        return "队列中的元素有{}".format(self.nums)


class LNode:
    def __init__(self):
        self.data = None
        self.next = None


class Queue:
    def __init__(self):
        self.head = LNode()
        self.front = None
        self.rear = None
        self.length = 0

    def get_size(self):
        return self.length

    def is_empty(self):
        return self.get_size() == 0

    def see_front(self):
        if self.is_empty() is True:
            print("no items")
        else:
            print(self.front.data)


    def see_rear(self):
        if self.is_empty() is True:
            print("no items")
        else:
            print(self.rear.data)

    def push(self, item):

        if self.is_empty() is True:
            new_node = LNode()
            new_node.data = item
            self.head.next = new_node
            self.front = new_node
            self.rear = new_node
            self.length += 1
        else:
            new_node = LNode()
            new_node.data = item
            self.rear.next = new_node
            self.rear = new_node
            self.length += 1

    def pop(self):
        if self.is_empty() is True:
            print("no items,can not pop")
            return None
        self.length -= 1
        tmp = self.front.data
        self.front = self.front.next
        self.head.next = self.front
        return tmp


    def __str__(self):
        res = []
        if self.is_empty() is True:
            return "没有元素"
        cur = self.head.next
        while cur.next:
            res.append(str(cur.data))
            res.append("->")
            cur = cur.next
        res.append(str(cur.data))
        return ''.join(res)


class Solution:
    def jumpFloor(self, number):
        # write code here
        if number==0:
            return 0
        elif number==1:
            return 1
        elif number==2:
            return 2
        else:
            return self.jumpFloor(number-1)+self.jumpFloor(number-2)

aa=Solution()
print(aa.jumpFloor(100))