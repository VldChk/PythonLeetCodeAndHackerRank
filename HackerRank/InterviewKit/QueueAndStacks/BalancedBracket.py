#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s:str):
    if len(s) % 2 == 1:
        return 'NO'
    stack = list()
    for i in range(len(s)):
        if s[i] in ('(', '{', '['):
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return 'NO'
            else:
                tmp = str(stack.pop())
                tmp = tmp + s[i]
                if tmp in ('()', '{}', '[]'):
                    continue
                else:
                    return 'NO'
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open('BalancedBrackets.txt', 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
