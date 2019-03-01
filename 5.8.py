# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     5.8
   Description :
   Author :       huang wei
   date：          2019/2/22
-------------------------------------------------
   Change Activity:
                   2019/2/22:
-------------------------------------------------
"""
__author__ = 'huang wei'


def if_number(str):
    flag = 1
    if str[0] == "+":
        str = str[1:]
    elif str[0] == "-":
        flag = -1
        str = str[1:]
    res = 0
    List = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(str)):
        if str[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("不合格")
            return
        else:
            res = res*10 + List.index(str[i])
    print(res * flag)


if __name__ == "__main__":
    if_number("-543")
    if_number("+543")
    if_number("23")
    if_number("++543")
    if_number("-5-43")
    if_number("-5x43")

