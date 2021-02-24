class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        for i in s:
            d[i] = d.setdefault(i, 0) + 1

        for j in t:
            if j in d and d[j] >= 0:
                d[j] -= 1
            else:
                return False
        if len(d) > 0:
            if max(x for x in d.values()) == 0:
                return True
            else:
                return False
        else:
            return True