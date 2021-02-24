def removeDuplicates(nums: list) -> int:
    ln = len(nums)
    if ln < 2:
        return ln
    prev = nums[0]
    i = 1
    while i < ln:
        if nums[i] == prev:
            nums.pop(i)
            ln -= 1
        else:
            prev = nums[i]
            i += 1
    return len(nums)

print(removeDuplicates([]))