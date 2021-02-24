def str_to_int(s):
    if s[0] == '-':
        sign = False
        start_pos = 1
    else:
        sign = True
        start_pos = 0
    res = 0
    for i in range(start_pos, len(s)):
        res += int(s[i]) * 10**(len(s) - i - 1)

    if sign is False:
        res *= -1

    return res


if __name__ == '__main__':

    q = ''
    while q != 'exit':
        q = input().strip()
        print(str_to_int(q))