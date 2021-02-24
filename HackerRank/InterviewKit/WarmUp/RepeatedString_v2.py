if __name__ == '__main__':
    s = input()
    n = int(input().strip().rstrip())

    num_of_a_in_s = 0
    num_of_a_in_trail = 0

    for ch in s:
        if ch == 'a':
            num_of_a_in_s += 1

    for ch in s[0:int(n%s.__len__())]:
        if ch == 'a':
            num_of_a_in_trail += 1

    num_of_a = int(n/s.__len__())*num_of_a_in_s + num_of_a_in_trail

    print(num_of_a)