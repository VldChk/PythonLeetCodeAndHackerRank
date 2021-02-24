import math
import os
import random
import re
import sys


def isSpecial(s):
    d = dict()

    if len(s) % 2 == 1:
        s.pop(int(len(s) / 2))

    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

        if len(d) > 1:
            return False

    return True


# Complete the substrCount function below.
def substrCount(n, s):
    cnt = 0
    for j in range(2, n+1):
        for i in range(0, n - j + 1):
            if isSpecial(list(s[i:i + j])):
                cnt += 1
    return cnt + n


if __name__ == '__main__':

    n = int(input())

    s = input()

    result = substrCount(n, s)
    print(result)