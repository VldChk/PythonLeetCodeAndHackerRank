class Solution:
    def reverse(self, x: int) -> int:
        def strToInt(s):
            res = 0
            for i in range(len(s)):
                res += int(s[i]) * 10 ** (len(s) - i - 1)
            return res

        def intToStr(n):
            res = ''
            while n > 10:
                res = str(n % 10) + res
                n = (n - (n % 10)) // 10
            res = str(n) + res
            return res

        def reverseList(s):
            n = len(s)
            for i in range(n // 2):
                s[i], s[n - i - 1] = s[n - i - 1], s[i]
            return s

        if x < 0:
            minus = -1
        else:
            minus = 1

        r = strToInt(''.join(reverseList(list(intToStr(abs(x)))))) * minus

        return r if abs(r) < 2 ** 31 - 1 else 0