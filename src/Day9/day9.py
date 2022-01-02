import itertools
import math


def day9():
    print('Running Day 9 - Part 1')

    with open('Day9/input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    xmax, ymax = len(lines), len(lines[0])
    lowpoints = []

    for i, j in itertools.product(range(xmax), range(ymax)):
        if all(map(lambda p: int(lines[i][j]) < int(lines[p[0]][p[1]]), [p for p in getadjacent(i, j, xmax, ymax)])):
            lowpoints.append((i, j))

    print(f'Risk Level = {sum([int(lines[x][y]) + 1 for x,y in lowpoints])}')

    print('Running Day 9 - Part 2')

    sizes = []

    for lowpoint in lowpoints:
        basin = set()
        queue = [lowpoint]
        while len(queue) != 0:
            point = queue.pop()
            if lines[point[0]][point[1]] != '9':
                basin.add(point)
                queue += [p for p in getadjacent(*point, xmax, ymax) if p not in basin]
        sizes.append(len(basin))

    print(f'Basin Size Product = {math.prod(sorted(sizes, reverse=True)[:3])}')

    print('Day 9 Complete')


def getadjacent(x: int, y: int, xmax: int, ymax: int) -> list[tuple[int, int]]:
    return [p for p in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            if p[0] in range(xmax) and p[1] in range(ymax)]
