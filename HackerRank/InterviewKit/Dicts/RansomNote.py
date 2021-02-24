#!/bin/python3

import math
import os
import random
import re
import sys


def to_dict(arr):
    d = dict((word, 0) for word in arr)
    for i in arr:
        d[i] += 1
    return d


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    for word in note:
        if word in magazine:
            if note[word] <= magazine[word]:
                continue
            else:
                return 'No'
        else:
            return 'No'

    return 'Yes'


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(to_dict(magazine), to_dict(note)))
