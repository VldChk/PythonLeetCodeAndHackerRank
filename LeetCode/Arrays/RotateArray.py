def rotate_bruteforce(nums:list, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    res = list()
    for i in range(k):
        res.append(nums[len(nums) - (k - i)])
    for i in range(len(nums) - k):
        res.append(nums[i])
    for i in range(len(nums)):
        nums[i] = res[i]


def rotate_noExtraSpace(nums:list, k: int) -> None:
    current_pos = -9999
    start = True
    tmp = nums[0]
    cnt = 0
    cycle_pos = 0
    while cnt != len(nums):
        if start:
            current_pos = 0
            start = False
        tmp, nums[(current_pos + k) % len(nums)] = nums[(current_pos + k) % len(nums)], tmp
        current_pos = (current_pos + k) % len(nums)
        if current_pos == cycle_pos:
            current_pos += 1
            cycle_pos += 1
            tmp = nums[current_pos % len(nums)]
        cnt += 1


n = [1,2,3,4,5,6,7]
rotate_noExtraSpace(n, 3)
print(n)

n = [1,2,3,4]
rotate_smart(n, 2)
print(n)

n = [1,2,3,4,5,6,7]
rotate_smart(n, 3)
print(n)

n = [1,2]
rotate_smart(n, 1)
print(n)

n = [1,2,3,4,5,6]
rotate_smart(n, 2)
print(n)

n = [1,2,3,4,5,6,7,8,9]
rotate_smart(n, 3)
print(n)