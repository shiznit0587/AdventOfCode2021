import re

def day5():
    print('Running Day 5 - a')

    p = re.compile('^(\d+),(\d+) -> (\d+),(\d+)$')

    lines = []
    with open('Day5/input.txt','r') as f:
        for line in f.readlines():
            match = p.match(line.strip())
            if match is not None:
                lines.append(((int(match.group(1)), int(match.group(2))),
                    (int(match.group(3)), int(match.group(4)))))

    map = dict()
    for line in lines:
        if line[0][0] == line[1][0]:
            # print(f'Line passed: {line}')
            x = line[0][0]
            y1 = min(line[0][1], line[1][1])
            y2 = max(line[0][1], line[1][1])
            for y in range(y1, y2 + 1):
                markmap(map, (x,y))
        elif line[0][1] == line[1][1]:
            # print(f'Line passed: {line}')
            y = line[0][1]
            x1 = min(line[0][0], line[1][0])
            x2 = max(line[0][0], line[1][0])
            for x in range(x1, x2 + 1):
                markmap(map, (x,y))

    overlaps = 0
    for x,y in map:
        if map[x,y] >= 2:
            overlaps += 1

    print(f'Overlap points = {overlaps}')

    print('Running Day 5 - b')

Point = tuple[int, int]
Line = tuple[Point, Point]
Map = dict[Point, int]

def markmap(map:Map, point:Point) -> None:
    if point in map:
        map[point] = map[point] + 1
    else:
        map[point] = 1