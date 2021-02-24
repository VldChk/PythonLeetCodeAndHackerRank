if __name__ == '__main__':
    num_of_steps = int(input())
    steps = str(input())

    tracker = ['-']
    count_of_valleys = 0

    for step in steps:
        if tracker[-1] == step or tracker[-1] == '-':
            tracker.append(step)
        else:
            tracker.pop()

        if step == 'U' and tracker[-1] == '-':
            count_of_valleys += 1

    print(count_of_valleys)