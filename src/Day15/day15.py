from functools import partial
import itertools
import sys
from heapq import *


def day15():
    print('Running Day 15 - Part 1')

    with open('Day15/input.txt', 'r') as f:
        ocean = [[int(c) for c in s.strip()] for s in f.readlines()]

    xmax, ymax = len(ocean), len(ocean[0])
    print(f'Lowest Risk = {calcrisk(xmax, ymax, partial(getrisk_1, ocean))}')
    print('Running Day 15 - Part 2')
    print(f'Lowest Risk = {calcrisk(xmax * 5, ymax * 5, partial(getrisk_2, ocean, xmax, ymax))}')
    print("Day 15 Complete")


def calcrisk(xmax, ymax, riskpred):
    ''' 
    This version uses a priority queue instead of re-searching for the unvisited position of lowest risk.
    It also returns once it reaches the bottom-right corner, and doesn't reevaluate risks for visited positions.
    '''
    visited: list[list[bool]] = [[False for _ in range(ymax)] for _ in range(xmax)]
    risks: list[list[int]] = [[sys.maxsize for _ in range(ymax)] for _ in range(xmax)]
    risks[0][0] = 0
    queue:list[tuple[int, tuple[int, int]]] = [(0, (0, 0))]

    while queue:
        risk, (x, y) = heappop(queue)
        if not visited[x][y]:
            visited[x][y] = True
            if (x, y) == (xmax - 1, ymax - 1):
                return risk
            for i, j in getadjacent(x, y, xmax, ymax):
                if not visited[i][j]:
                    adjrisk = risk + riskpred(i, j)
                    if adjrisk < risks[i][j]:
                        risks[i][j] = adjrisk
                        heappush(queue, (adjrisk, (i, j)))


def getrisk_1(ocean, x, y):
    return ocean[x][y]


def getrisk_2(ocean, xmax, ymax, x, y):
    return (ocean[x % xmax][y % ymax] - 1 + x // xmax + y // ymax) % 9 + 1


def getadjacent(x: int, y: int, xmax: int, ymax: int):
    return [p for p in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            if p[0] in range(xmax) and p[1] in range(ymax)]


def calcrisk_orig(xmax, ymax, riskpred):
    '''
    Dead code. This took 10 seconds to execute just for part 1.
    This was likely because I was re-searching for the unvisited position with the lowest risk each loop.
    Or because I was not early-outing when reaching the bottom-right corner.
    Or because I was reevaluating risks for visited positions.
    Likely all of the above.
    '''
    visited: list[list[bool]] = [[False for _ in range(ymax)] for _ in range(xmax)]
    risks: list[list[int]] = [[sys.maxsize for _ in range(ymax)] for _ in range(xmax)]
    risks[0][0] = 0

    # Good 'ol Dijkstra
    while not all(map(all, visited)):
        # This was clever, but oh so slow.
        x, y = min({(x, y) for x, y in itertools.product(range(xmax), range(ymax)) if not visited[x][y]}, key=lambda p: risks[p[0]][p[1]])

        for i, j in getadjacent(x, y, xmax, ymax):
            risk = risks[x][y] + riskpred(i, j)
            if risk < risks[i][j]:
                risks[i][j] = risk

        visited[x][y] = True

    return risks[xmax - 1][ymax - 1]
