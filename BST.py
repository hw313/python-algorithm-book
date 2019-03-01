import copy
class TreeNode:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        # copy = self.get_newroot(pRoot)
        # self.mirror(pRoot)
        # return self.equal(copy, pRoot)
        a = pRoot
        b = pRoot
        self.mirror(b)
        return self.equal(a,b)

    def get_newroot(self,pRoot):
        if pRoot is None:
            return
        else:
            root = TreeNode()
            root.val = pRoot.val
            root.left = self.get_newroot(pRoot.left)
            root.right = self.get_newroot(pRoot.right)
            return root


    def mirror(self, pRoot):
        if pRoot is None:
            return
        pRoot.left, pRoot.right = pRoot.right, pRoot.left
        self.mirror(pRoot.left)
        self.mirror(pRoot.right)
        # return pRoot

    def equal(self, a, b):
        if a is None and b is None:
            return True
        elif a is None and b is not None:
            return False
        elif a is not None and b is None:
            return False
        elif a.val != b.val:
            return False
        else:
            return self.equal(a.left, b.left) and self.equal(a.right, b.right)



import numpy as np


class dfs:
    def movingCount(self, threshold, rows, cols):
        # write code here
        flag = np.zeros((rows, cols))
        return self.count(0, 0, threshold, rows, cols, flag)

    def count(self, i, j, threshold, rows, cols, flag):
        if i < 0 or i >= rows or j < 0 or j >= cols or self.num_count(i) + self.num_count(j) > threshold or flag[i][
            j] == 1:
            return 0
        flag[i][j] = 1
        # print(i,j)
        return 1 + self.count(i + 1, j, threshold, rows, cols, flag) + self.count(i - 1, j, threshold, rows, cols, flag)\
               + self.count(i, j + 1, threshold, rows, cols, flag) + self.count(i, j - 1, threshold, rows, cols, flag)

    def num_count(self, cnt):
        sum = 0
        # if cnt < 10:
        #     return cnt
        while cnt > 0:
            sum += cnt % 10
            cnt = int(cnt / 10)
        return sum

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


class Order:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        q=[]
        if pRoot is None:
            return None
        res=[]
        q.append(pRoot)
        while len(q)>0:
            item_count=len(q)
            ans = []
            for _ in range(item_count):
                xx = q[0]
                q = q[1:]
                ans.append(xx.val)
                if xx.left:
                    q.append(xx.left)
                if xx.right:
                    q.append(xx.right)
            res.append(ans)
        return ans
# xx =dfs()
# print(xx.movingCount(7,10,10))
# print(xx.num_count(4))

root= ab=constructTree()

root.left.val =100
print(root.left.val)
print(ab.left.val)

