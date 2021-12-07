def day2():
    print('Running Day 2 - Part 1')

    with open('Day2/input.txt', 'r') as f:
        commands = [line.split() for line in f.readlines()]
        commands = [tuple((c[0], int(c[1]))) for c in commands]

    position, depth = 0, 0

    for command in commands:
        if command[0] == 'forward':
            position += command[1]
        elif command[0] == 'down':
            depth += command[1]
        elif command[0] == 'up':
            depth -= command[1]
        # print(f'command = {command}, position = {position}, depth = {depth}')

    print(f'position = {position}, depth = {depth}, product = {position * depth}')

    print('Running Day 2 - Part 2')

    position, depth, aim = 0, 0, 0

    for command in commands:
        if command[0] == 'forward':
            position += command[1]
            depth += aim * command[1]
        elif command[0] == 'down':
            aim += command[1]
        elif command[0] == 'up':
            aim -= command[1]
        # print(f'command = {command}, position = {position}, depth = {depth}, aim = {aim}')

    print(f'position = {position}, depth = {depth}, aim = {aim}, product = {position * depth}')

    print('Day 2 Complete')
