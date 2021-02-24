class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # bruteforce
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] + nums[i] == target:
                    return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # not much brute force but extra space
        d = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in d:
                return [i, d[target - nums[i]]]
            else:
                d[nums[i]] = i