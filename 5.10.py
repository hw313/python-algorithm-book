# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     5.10
   Description :
   Author :       huang wei
   date：          2019/2/22
-------------------------------------------------
   Change Activity:
                   2019/2/22:
-------------------------------------------------
"""
__author__ = 'huang wei'
import numpy as np

def find_max(str):
    if len(str) < 1:
        print("None")
    elif len(str) == 1:
        print(str)
    elif len(str) == 2:
        if str[0] == str[1]:
            print(str)
        else:
            print(str[0])
    else:
        dp = np.zeros(shape=(len(str), len(str)))
        res, max = 0, -1
        for i in range(len(str)):
            dp[i][i] = 1
            res = 1
        for i in range(len(str)-1):
            if str[i] == str[i+1]:
                dp[i][i+1] = 1
                res = 2
            else:
                dp[i][i+1] = 0
        for l in range(3, len(str)+1):
            for i in range(0, len(str) - l + 1):
                j = i + l - 1
                if str[i] == str[j]:
                    dp[i][j] = dp[i+1][j-1]
                    if dp[i][j] == 1:
                        res = l
                    if res > max:
                        max = res
                        print(str[i:j+1])
                else:
                    dp[i][j] = 0
        print(res)


if __name__ =="__main__":
    str = "abcdefgfedxyz"
    find_max(str)

