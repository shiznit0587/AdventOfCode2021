def day6():
    print('Running Day 6 - Part 1')

    with open('Day6/input.txt', 'r') as f:
        input = [int(s) for s in f.readline().strip().split(',')]

    fish = input.copy()

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

    fish = [0 for _ in range(7)]
    nursery = [0, 0]
    for f in input:
        fish[f] += 1

    for day in range(256):
        matured = nursery[0]
        nursery[0] = nursery[1]
        spawn = day % 7
        nursery[1] = fish[spawn]
        fish[spawn] += matured

    print(f'Total fish = {sum(fish) + sum(nursery)}')

    print("Day 6 Complete")
