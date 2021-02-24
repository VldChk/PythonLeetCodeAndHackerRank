# Complete the minimumSwaps function below.
def minimumSwaps(arr, n):
    position_list = list()
    max_diff_ind = 0
    min_diff_ind = 0
    max_diff = 0
    min_diff = 0
    swaps_cnt = 0

    for i in range(n):
        diff = arr[i] - i - 1
        position_list.append(diff)
        if diff > max_diff:
            max_diff_ind = i
            max_diff = diff
        elif diff < min_diff:
            min_diff_ind = i
            min_diff = diff

    while max_diff > 0:

        position_list[max_diff_ind] = min_diff + (min_diff_ind - max_diff_ind)
        position_list[min_diff_ind] = max_diff - (min_diff_ind - max_diff_ind)
        swaps_cnt += 1

        min_diff = 0
        max_diff = 0

        for i in range(n):
            diff = position_list[i]
            if diff > max_diff:
                max_diff_ind = i
                max_diff = diff

        if max_diff == 1 and position_list[max_diff_ind + 1] == -1:
            min_diff_ind = max_diff_ind + 1
            min_diff = -1
            continue

        for i in range(max_diff_ind + 1, n):
            diff = position_list[i]
            if diff < min_diff:
                min_diff_ind = i
                min_diff = diff

    # print(swaps_cnt)
    return swaps_cnt


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr, n)
