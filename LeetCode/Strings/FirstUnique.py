class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] = len(s) + 1
            else:
                d[s[i]] = i
        if len(d) == 0:
            return -1
        else:
            r= min(x for x in d.values())
            if r == len(s) + 1:
                return -1
            else:
                return r