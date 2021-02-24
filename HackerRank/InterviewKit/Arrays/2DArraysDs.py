#!/bin/python3

import math
import os
import random
import re
import sys

def hourglassSum(arr):
    n = len(arr) - 2
    m = len(arr[0]) - 2
    biggest_sum = -1 * 2 ** 31

    for i in range(n):
        for j in range(m):
            tmp_sum = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            if tmp_sum > biggest_sum:
                biggest_sum = tmp_sum

    return biggest_sum


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)
