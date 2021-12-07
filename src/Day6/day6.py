def day6():
    print('Running Day 6 - Part 1')

    with open('Day6/input.txt', 'r') as f:
        fish = [int(s) for s in f.readline().strip().split(',')]

    for _ in range(80):
        numfish = len(fish)
        for i in range(numfish):
            if fish[i] == 0:
                fish.append(8)
                fish[i] = 6
            else:
                fish[i] -= 1

    print(f'Total fish = {len(fish)}')

    print('Running Day 6 - Part 2')

    print("Day 6 Complete")
