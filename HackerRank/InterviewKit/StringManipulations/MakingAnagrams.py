#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    d1 = dict()
    for s in a:
        if s in d1:
            d1[s] += 1
        else:
            d1[s] = 1

    for s in b:
        if s in d1:
            d1[s] -= -1
        else:
            d1[s] = 1

    cnt = sum(abs(x) for x in d1.values())

    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
