#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    res = [list() for i in range(n)]
    last_answer = 0
    for i in queries:
        if i[0] == 1:
            idx = (i[1] ^ last_answer) % n
            res[idx].append(i[2])
        elif i[0] == 2:
            idx = (i[1] ^ last_answer) % n
            last_answer = res[idx][i[2] % len(res[idx])]
            print(last_answer)


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    # print(''.join(map(str, result)))

