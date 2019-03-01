# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     5.7
   Description :
   Author :       huang wei
   date：          2019/2/22
-------------------------------------------------
   Change Activity:
                   2019/2/22:
-------------------------------------------------
"""
__author__ = 'huang wei'


def removeNestedPare(strs):
    if strs is None:
        return strs
    cnt = 1
    if strs[0] != '(' or strs[-1] != ')':
        print("None")
    sb = "("
    i = 1
    length = len(strs)
    while i < length:
        if strs[i] == "(":
            cnt += 1
        elif strs[i] == ")":
            cnt -= 1
            if cnt < 0:
                print("表达式不靠谱")
                return None
        else:
            sb += strs[i]
        i += 1
    if cnt != 0:
        print("不合格")
    else:
        sb += ")"
        print(sb)


if __name__ == "__main__":
    xx = "(1,(2,3),(4,(5,6),7))"
    removeNestedPare(xx)


