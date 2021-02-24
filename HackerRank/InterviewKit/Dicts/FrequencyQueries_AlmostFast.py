import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    d = dict()
    res = list()
    for q in queries:
        if q[0] == 1:
            if q[1] in d:
                d[q[1]] += 1
            else:
                d[q[1]] = 1
        elif q[0] == 2 and q[1] in d and d[q[1]] > 0:
            d[q[1]] -= 1
        elif q[0] == 3:
            chk = False
            if q[1] == 5:
                print ('HI')
            for v in d.values():
                if v == q[1]:
                    res.append(1)
                    chk = True
                    break
            if chk is False:
                res.append(0)

    return res


if __name__ == '__main__':

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print(ans)