def myAtoi_general(s: str) -> int:
    s = ''.join(filter(lambda x: x.isnumeric() or x in ('+', '-'), s))
    current_pos = 0
    n = len(s)
    tmp = 0
    res = 0
    for i in s[::-1]:
        if i == '+':
            res += tmp
            current_pos = 0
            tmp = 0
        elif i == '-':
            res -= tmp
            current_pos = 0
            tmp = 0
        else:
            tmp += int(i) * 10 ** current_pos
            current_pos += 1
    res += tmp
    return min(max(res, -1 * 2 ** 31), 2 * 31 - 1)


def myAtoi( s: str) -> int:
    s = s.lstrip()
    tmp = 0
    if len(s) == 0 or (not s[0].isnumeric() and s[0] not in ('+', '-', ' ')):
        return 0
    i = 0
    if s[i] == '-':
        minus = -1
        i += 1
    elif s[i] == '+':
        minus = 1
        i += 1
    else:
        minus = 1
    res = 0
    while i < len(s) and s[i].isnumeric():
        res = tmp * 10 + int(s[i])
        tmp = res
        i += 1
    return min(max(res * minus, -1 * 2 ** 31), 2 ** 31 - 1)


print(myAtoi("   -42"))
