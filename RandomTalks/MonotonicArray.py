def is_monotonic(arr):
    raising = None
    decreasing = None
    for i in range(1, len(arr)):
        if raising is not False and decreasing is not True and arr[i-1] - arr[i] <= 0:
            raising = True
        elif raising is not True and decreasing is not False and arr[i - 1] - arr[i] >= 0:
            decreasing = True
        else:
            return False

    return True


arr_1 = [1,2,5,5,6]
arr_2 = [9,4,4,2,2]
arr_3 = [1,4,6,3]
arr_4 = [6,5,5,3,2,9]
arr_5 = [2,2,2,2,2,2,2]

print(is_monotonic(arr_1))
print(is_monotonic(arr_2))
print(is_monotonic(arr_3))
print(is_monotonic(arr_4))
print(is_monotonic(arr_5))