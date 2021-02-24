# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0 for x in range(n)]
    max_value = 0
    for i in queries:
        for j in range(i[1] - i[0] + 1):
            arr[i[0] + j - 1] += i[2]
            if arr[i[0] + j - 1] > max_value:
                max_value = arr[i[0] + j - 1]

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
