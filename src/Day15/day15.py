import sys


def day15():
    print('Running Day 15 - Part 1')

    with open('Day15/input.txt', 'r') as f:
        ocean = [[int(c) for c in s.strip()] for s in f.readlines()]

    xmax, ymax = len(ocean), len(ocean[0])

    risks: list[list[int]] = [[sys.maxsize for _ in range(ymax)] for _ in range(xmax)]
    risks[0][0] = 0
    visited: list[list[bool]] = [[False for _ in range(ymax)] for _ in range(xmax)]

    # Good 'ol Dijkstra
    while not all(map(all, visited)):
        # This was clever, but slow.
        # x, y = min({(x, y) for x, y in itertools.product(range(xmax), range(ymax)) if not visited[x][y]}, key=lambda p: risks[p[0]][p[1]])

        x, y = None, None
        for i in range(xmax):
            for j in range(ymax):
                if not visited[i][j]:
                    if x == None or risks[i][j] < risks[x][y]:
                        x, y = i, j

        for i, j in getadjacent(x, y, xmax, ymax):
            risk = risks[x][y] + ocean[i][j]
            if risk < risks[i][j]:
                risks[i][j] = risk

        visited[x][y] = True

    print(f'Lowest Risk = {risks[xmax - 1][ymax - 1]}')

    print('Running Day 15 - Part 2')

    print("Day 15 Complete")


def getadjacent(x: int, y: int, xmax: int, ymax: int):
    # Changed to generator for performance
    # return [p for p in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    # if p[0] in range(xmax) and p[1] in range(ymax)]

    if 0 <= x - 1:
        yield (x-1, y)
    if x + 1 < xmax:
        yield (x+1, y)
    if 0 <= y - 1:
        yield (x, y-1)
    if y + 1 < ymax:
        yield (x, y+1)
