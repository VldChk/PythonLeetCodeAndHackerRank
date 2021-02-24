class Solution_BruteForce:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for j in d:
            if d[j] == 1:
                return j

class Solution_SlightlyBetter:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            if i in d:
                del d[i]
            else:
                d[i] = 1
        return list(d.keys())[0]

