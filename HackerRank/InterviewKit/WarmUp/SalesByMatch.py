
if __name__ == '__main__':
    num_of_objects = int(input())
    list_of_objects = list(map(int, input().rstrip().split(' ')))

    num_of_pairs = 0
    unpaired_numbers = dict()

    for obj in list_of_objects:
        if obj in unpaired_numbers:
            num_of_pairs += 1
            del unpaired_numbers[obj]
        else:
            unpaired_numbers[obj] = True

    print(num_of_pairs)

