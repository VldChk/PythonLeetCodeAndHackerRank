if __name__ == '__main__':
    s = input()
    n = int(input().strip().rstrip())

    big_s = str()

    for i in (range(int(n/s.__len__()) + 1)):
        big_s += s

    num_of_a = 0

    for ch in big_s[0:n]:
        if ch == 'a':
            num_of_a += 1

    print(num_of_a)