#!/bin/python3

import math
import os
import random
import re
import sys


# O Y D F R M Y M A W
# A W H Y F Y C M Q A
# Complete the commonChild function below.
def commonChild(s1, s2):
    c = [[0 for x in range(len(s2)+1)] for x in range(len(s1)+1)]
    for i in range(s1):
        for j in range(s2):
            if s1[i] == s2[j]:
                c[i+1][j+1] = c[i][j] + 1
            else:
                c[i + 1][j + 1] = max(c[i+1][j], c[i][j+1])
    return c[-1][-1]


if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    print(result)
