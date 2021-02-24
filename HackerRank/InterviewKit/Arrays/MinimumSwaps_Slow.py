#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr, n):
    position_list = list()
    max_diff_ind = 0
    min_diff_ind = 0
    max_diff = 0
    min_diff = 0
    swaps_cnt = 0

    for i in range(n):
        diff = arr[i]-i-1
        position_list.append(diff)
        if diff > max_diff:
            max_diff_ind = i
            max_diff = diff

    while max_diff > 0:
        min_diff = 0
        for i in range(max_diff_ind, n):
            diff = arr[i] - i - 1
            if diff < min_diff:
                min_diff_ind = i
                min_diff = diff

        tmp = arr[max_diff_ind]
        arr[max_diff_ind] = arr[min_diff_ind]
        arr[min_diff_ind] = tmp
        swaps_cnt += 1

        min_diff = 0
        max_diff = 0

        for i in range(n):
            diff = arr[i] - i - 1
            position_list[i] = diff
            if diff > max_diff:
                max_diff_ind = i
                max_diff = diff
            elif diff < min_diff:
                min_diff_ind = i
                min_diff = diff

    return swaps_cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr, n)

    fptr.write(str(res) + '\n')

    fptr.close()
