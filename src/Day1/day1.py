def day1():
    print("Running Day 1 - a")

    with open("Day1/input.txt","r") as f:
        depths = list(map(int, f.readlines()))

    count = 0
    prev = depths[0]
    for depth in depths[1:]:
        next = depth
        if next > prev:
            count += 1
        prev = next

    print(f'Count = {count}')

    print("Running Day 1 - b")

    count = 0
    prev = sum(depths[0:3])
    for idx in range(1, len(depths) - 2):
        next = sum(depths[idx:idx+3])
        if next > prev:
            count += 1
        prev = next

    print(f'Count = {count}')

    print("Day 1 Complete")