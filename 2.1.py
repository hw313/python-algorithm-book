# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     2.1
   Description :
   Author :       huang wei
   date：          2018/11/25
-------------------------------------------------
   Change Activity:
                   2018/11/25:
-------------------------------------------------
"""
__author__ = 'huang wei'


class StackByList:
    def __init__(self):
        self.nums = []

    def size(self):
        return len(self.nums)

    def is_empty(self):
        return len(self.nums) == 0

    def get_top(self):
        # if len(self.nums) == 0:
        if self.is_empty() is True:
            print("没有元素")
            return None
        print("最上面的元素是{}".format(self.nums[-1]))
        return self.nums[-1]

    def pop(self):
        if len(self.nums) == 0:
            print("没有元素")
            return None
        return self.nums.pop()

    def push(self,item):
        self.nums.append(item)

    def __str__(self):
        return "该堆栈中含有的元素为{}".format(self.nums)


class LNode:
    def __init__(self):
        self.data = None
        self.next = None


class StackByLinkList:
    def __init__(self):
        self.LNode = LNode()
        self.tail = None
        self.pre_tail = None
        self.length = 0

    def is_empty(self):
        return self.LNode.next is None

    def size(self):

        return self.length

    def get_top(self):
        if self.is_empty() is True:
            print("没有元素")
            return None
        cur = self.LNode.next
        while cur.next is not None:
            cur = cur.next
        print(cur.data)

    def pop(self):
        if self.is_empty() is True:
            print("没有元素")
            return None
        cur = self.LNode.next
        self.pre_tail = self.LNode
        self.tail = cur
        while cur.next is not None:
            cur = cur.next
            self.pre_tail = self.pre_tail.next
            self.tail = self.tail.next
        self.pre_tail.next = None
        self.length -= 1
        return self.tail.data

    def push(self, item):
        self.length += 1
        new_node = LNode()
        new_node.data = item
        new_node.next = None
        if self.is_empty() is True:
            self.LNode.next = new_node

        else:
            cur = self.LNode.next
            self.pre_tail = self.LNode
            self.tail = cur
            while cur.next is not None:
                cur = cur.next
                self.pre_tail = self.pre_tail.next
                self.tail = self.tail.next
            self.tail.next = new_node


    def __str__(self):
        if self.is_empty() is True:
            return "没有元素"
        cur = self.LNode.next
        self.res = []
        while cur.next is not None:
            self.res.append(str(cur.data))
            self.res.append("<")
            cur = cur.next
        self.res.append(str(cur.data))
        return ''.join(self.res)










def moveBottomToTops(s):
    if s.is_empty():
        return
    top1 = s.get_top()
    s.pop()
    if not s.is_empty():
        moveBottomToTops(s)
        top2 = s.get_top()
        s.pop()
        s.push(top1)
        s.push(top2)
    else:
        s.push(top1)

S=StackByList()
S.push(3)
S.push(2)
S.push(1)
moveBottomToTops(S)



def jiechen(x):
    if x==1:
        return 1
    return x*jiechen(x-1)

print(jiechen(6))