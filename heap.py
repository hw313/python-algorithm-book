# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     heap
   Description :
   Author :       huang wei
   date：          2019/2/27
-------------------------------------------------
   Change Activity:
                   2019/2/27:
-------------------------------------------------
"""
__author__ = 'huang wei'

# 实现最大堆
class maxheap:
    def __init__(self):
        self.nums = []

    def insert_heap(self, num):
        self.nums.append(num)
        i = len(self.nums)-1
        while i > 0:
            if self.nums[i] > self.nums[int((i-1)/2)]:
                self.nums[i], self.nums[int((i-1)/2)] = self.nums[int((i-1)/2)], self.nums[i]
                i = int((i-1)/2)
            else:
                break

    def pop_heap(self):
        if len(self.nums) > 0:
            self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
            xx = self.nums.pop()
            start = 0
            next = 2 * start + 1
            while next < len(self.nums):
                if next + 1 < len(self.nums) and self.nums[next + 1] > self.nums[next]:
                    next = next + 1
                if self.nums[next] < self.nums[start]:
                    break
                else:
                    self.nums[next], self.nums[start] = self.nums[start], self.nums[next]
                    next = 2 * next +1
            return xx

    def __str__(self):
        return "该最大堆的元素依次为：{}".format(self.nums)

    def get_length(self):
        return len(self.nums)


# 实现最小堆
class minheap:
    def __init__(self):
        self.nums = []

    def __str__(self):
        return "该最小堆的元素依次为: {}".format(self.nums)

    def insert_heap(self, num):
        self.nums.append(num)
        length = len(self.nums)
        idx = length - 1
        while idx > 0:
            if self.nums[idx] > self.nums[int((idx - 1)/2)]:
                break
            self.nums[idx], self.nums[int((idx - 1)/2)] = self.nums[int((idx - 1)/2)], self.nums[idx]
            idx = int((idx - 1) / 2)

    def pop_heap(self):
        if len(self.nums) > 0:
            self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
            xx = self.nums.pop()
            start = 0
            next = 2 * start + 1
            while next < len(self.nums):
                if next + 1 < len(self.nums) and self.nums[next + 1] < self.nums[next]:
                    next = next + 1
                if self.nums[start] < self.nums[next]:
                    break
                self.nums[start], self.nums[next] = self.nums[next], self.nums[start]
                next = 2 * next + 1
            return xx

    def get_length(self):
        return len(self.nums)

# 快速找到中位数
class Solution:
    def __init__(self):
        self.max_heap = maxheap()
        self.min_heap = minheap()
        self.count = 0

    def insert(self, item):
        if self.count % 2 == 0:
            self.max_heap.insert_heap(item)
            tmp = self.max_heap.pop_heap()
            self.min_heap.insert_heap(tmp)
            self.count += 1
        else:
            self.min_heap.insert_heap(item)
            tmp = self.min_heap.pop_heap()
            self.max_heap.insert_heap(tmp)
            self.count += 1

    def find_mid(self):
        if self.count % 2 == 1:
            return self.min_heap.nums[0]
        else:
            return (self.max_heap.nums[0] + self.min_heap.nums[0]) / 2


solve = Solution()
solve.insert(1)
solve.insert(5)
solve.insert(7)
solve.insert(3)
solve.insert(4)
solve.insert(8)
solve.insert(9)


print(solve.find_mid())