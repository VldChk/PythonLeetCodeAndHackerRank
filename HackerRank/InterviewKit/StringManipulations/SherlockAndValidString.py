#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the isValid function below.
def isValid(s):
    d = dict()
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

    r = dict()

    for i in d.values():
        if i in r:
            r[i] += 1
        else:
            r[i] = 1

        if len(r) > 2:
            return 'NO'

    if len(r) == 1:
        return 'YES'

    if list(r.values())[0] > 1 and list(r.values())[1] > 1:
        return 'NO'
    elif abs(list(r.keys())[0] - list(r.keys())[1]) > 1 and (1,1) not in r.items():
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':

    s = input()

    result = isValid(s)

    print(result)