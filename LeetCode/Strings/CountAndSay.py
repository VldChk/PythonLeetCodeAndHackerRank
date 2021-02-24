def countAndSay(n: int) -> str:
    def _cntAndSay(s: str) -> str:
        st = s[0]
        i = 1
        tmp = 1
        res = str()
        while i < len(s):
            if s[i] == st:
                tmp += 1
                i += 1
            else:
                res = res + str(tmp) + str(st)
                st = s[i]
                tmp = 1
                i += 1
        res = res + str(tmp) + str(st)
        return res

    t = '1'
    if n == 1:
        return t

    k = 2
    while k <= n:
        t = _cntAndSay(t)
        k += 1
    return t


print(countAndSay(22))