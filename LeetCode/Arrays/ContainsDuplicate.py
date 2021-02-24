class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for i in nums:
            if i in d:
                return True
            else:
                d[i] = 0
        return False