import re


def day5():
    print('Running Day 5 - Part 1')

    p = re.compile('^(\d+),(\d+) -> (\d+),(\d+)$')

    lines = []
    with open('Day5/input.txt', 'r') as f:
        for line in f.readlines():
            match = p.match(line.strip())
            if match is not None:
                lines.append(((int(match.group(1)), int(match.group(2))),
                              (int(match.group(3)), int(match.group(4)))))

    map = dict()
    for line in lines:
        if line[0][0] == line[1][0]:
            # print(f'Vertical line: {line}')
            x = line[0][0]
            y1 = min(line[0][1], line[1][1])
            y2 = max(line[0][1], line[1][1])
            for y in range(y1, y2 + 1):
                markmap(map, (x, y))
        elif line[0][1] == line[1][1]:
            # print(f'Horizontal line: {line}')
            y = line[0][1]
            x1 = min(line[0][0], line[1][0])
            x2 = max(line[0][0], line[1][0])
            for x in range(x1, x2 + 1):
                markmap(map, (x, y))

    print(f'Overlap points = {countoverlaps(map)}')

    print('Running Day 5 - Part 2')

    for line in lines:
        if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
            # print(f'Diagonal line: {line}')
            dx = 1 if line[1][0] > line[0][0] else -1
            dy = 1 if line[1][1] > line[0][1] else -1
            for x, y in zip(range(line[0][0], line[1][0] + dx, dx),
                            range(line[0][1], line[1][1] + dy, dy)):
                markmap(map, (x, y))

    print(f'Overlap points = {countoverlaps(map)}')


Point = tuple[int, int]
Line = tuple[Point, Point]
Map = dict[Point, int]


def markmap(map: Map, point: Point) -> None:
    if point in map:
        map[point] = map[point] + 1
    else:
        map[point] = 1


def countoverlaps(map: Map) -> int:
    overlaps = 0
    for x, y in map:
        if map[x, y] >= 2:
            overlaps += 1
    return overlaps
