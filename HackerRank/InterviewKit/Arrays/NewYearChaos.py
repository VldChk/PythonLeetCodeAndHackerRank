# Complete the minimumBribes function below.
def getDistance(q, i):
    try:
        return q[i] - i - 1
    except:
        return 0


def minimumBribes(q):
    amount_of_bribes = 0

    ordered_list = [y+1 for y in range(len(q))]

    for i in range(len(q)):
        distance = getDistance(q, i)
        ordered_index = ordered_list.index(q[i])
        if distance > 2:
            print("Too chaotic")
            return True
        elif distance > 0:
            amount_of_bribes += distance
        elif distance <= 0 and ordered_index > 0:
            amount_of_bribes += ordered_index

        ordered_list.pop(ordered_index)

    print(str(amount_of_bribes))


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
