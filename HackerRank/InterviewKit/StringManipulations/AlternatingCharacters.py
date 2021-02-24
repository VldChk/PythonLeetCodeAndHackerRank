#!/bin/python3

import math
import os
import random
import re
import sys

count = 0


def nextPos(s, startPos):
    for i in range(startPos + 1, len(s)):
        if s[startPos] != s[i]:
            return i
        else:
            global count
            count += 1
    return len(s)


# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    global count
    count = 0
    startPos = 0
    while startPos < len(s):
        startPos = nextPos(s, startPos)

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
