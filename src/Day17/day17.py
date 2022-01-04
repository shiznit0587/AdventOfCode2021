import re


def day17():
    print('Running Day 17 - Part 1')

    p = re.compile('^target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)$')

    with open('Day17/input.txt', 'r') as f:
        match = re.compile('^target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)$').match(f.readline().strip())
        xmin, xmax, ymin, ymax = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))

    n = -ymin - 1
    height = (n * (n + 1)) // 2

    print(f'Max height = {height}')

    print('Running Day 17 - Part 2')

    print("Day 17 Complete")
