#!/bin/python3

import math
import os
import random
import re
import sys

def combinations(n, k):
    if n < 3:
        return 0
    else:
        return int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))


# Complete the countTriplets function below.
def countTriplets(arr, r):
    res = 0
    d = dict((x, 0) for x in arr)
    for i in arr:
        d[i] += 1

    for i in d.keys():
        if r == 1:
            res += combinations(d[i], 3)
        elif i*r in d and i * (r**2) in d:
            res += d[i] * d[i*r] * d[i*(r**2)]

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
