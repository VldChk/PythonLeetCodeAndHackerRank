# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0 for x in range(n)]
    max_value = 0
    for i in queries:
        arr[i[0] - 1] += i[2]
        if i[1] <= n - 1:
            arr[i[1]] -= i[2]

    x = 0
    for j in arr:
        x += j
        if x > max_value:
            max_value = x

    return max_value


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)
