import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    d = dict()
    res = list()
    reverse_d = dict()
    for q in queries:
        if q[0] == 1:
            if q[1] in d:
                d[q[1]] += 1
            else:
                d[q[1]] = 1
            if d[q[1]] in reverse_d:
                reverse_d[d[q[1]]].append(1)
                if d[q[1]] - 1 in reverse_d:
                    reverse_d[d[q[1]] - 1].pop()
            else:
                reverse_d[d[q[1]]] = [1]
                if d[q[1]]-1 in reverse_d:
                    reverse_d[d[q[1]] - 1].pop()
        elif q[0] == 2 and q[1] in d and d[q[1]] > 0:
            if d[q[1]] in reverse_d:
                reverse_d[d[q[1]]].pop()
            d[q[1]] -= 1
            if d[q[1]] in reverse_d:
                reverse_d[d[q[1]]].append(1)
        elif q[0] == 3:
            if q[1] == 5:
                print ('HI')
            if q[1] in reverse_d and len(reverse_d[q[1]]) > 0:
                res.append(1)
            else:
                res.append(0)

    return res


if __name__ == '__main__':

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    for q in queries:
        if q[0] == 3:
            print(q[1])

    print('\n'.join(map(str, ans)))
    print('\n')