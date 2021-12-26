def day9():
    print('Running Day 9 - Part 1')

    with open('Day9/input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    lowpoints = []

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if all(map(
                lambda p : int(lines[i][j]) < int(lines[p[0]][p[1]]), 
                [p for p in getadjacent(i,j) if p[0] in range(len(lines)) and p[1] in range(len(lines[i]))])):
                lowpoints.append((i,j))
    
    print(f'Risk Level = {sum([int(lines[x][y]) + 1 for x,y in lowpoints])}')

    print('Running Day 9 - Part 2')

    print('Day 9 Complete')


Point = tuple[int, int]


def getadjacent(x,y) -> list[Point]:
    return [(x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1)]