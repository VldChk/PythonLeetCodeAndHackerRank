#!/bin/python3
import math
import os
import random
import re
import sys


def combinations(n, k):
    if n < 2:
        return 1
    else:
        return int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    d = dict()
    for i in range(1, len(s)):
        for j in range(0, len(s)-i+1):
            tmp = ''.join(sorted(s[j:j+i]))
            if tmp in d:
                d[tmp] += 1
            else:
                d[tmp] = 1
    return sum(combinations(x, 2) for x in d.values() if x > 1)


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)
