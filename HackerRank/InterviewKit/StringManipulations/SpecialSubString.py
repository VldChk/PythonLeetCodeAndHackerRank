def substrCount(n, s):
    l = []
    count = 0
    cur = s[0]

    # 1st pass
    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            l.append((cur, count))
            count = 1
            cur = s[i]
    l.append((cur, count))

    ans = 0

    # 2nd pass
    for i in l:
        ans += (i[1] * (i[1] + 1)) // 2

    # 3rd pass
    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])

    return ans


if __name__ == '__main__':

    n = int(input())

    s = input()

    result = substrCount(n, s)
    print(result)