# Complete the minimumSwaps function below.
def minimumSwaps(arr, n):

    swaps_cnt = 0

    for i in range(n):
        while arr[i] != i + 1:
            tmp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = tmp
            swaps_cnt += 1

    print(swaps_cnt)
    return swaps_cnt


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr, n)
