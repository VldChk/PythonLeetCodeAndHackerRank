if __name__ == '__main__':
    num_of_clouds = int(input())
    list_of_clouds = list(map(int, input().rstrip().split(' ')))

    number_of_jumps = 0

    curr_position = 0

    while curr_position < num_of_clouds - 1:
        if (curr_position+2) < num_of_clouds and list_of_clouds[curr_position + 2] == 0:
            curr_position += 2
        else:
            curr_position += 1
        number_of_jumps += 1

    print(number_of_jumps)