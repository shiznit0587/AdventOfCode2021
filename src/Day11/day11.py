import itertools

def day11():
    print('Running Day 11 - Part 1')

    with open('Day11/input.txt', 'r') as f:
        ocean = [[int(c) for c in s.strip()] for s in f.readlines()]

    flashes = 0
    for _ in range(100):
        flashes += step_ocean(ocean)

    print(f'Total flashes after 100 steps = {flashes}')

    print('Running Day 11 - Part 2')

    flashes, step = 0, 100
    while flashes != 100:
        flashes, step = step_ocean(ocean), step + 1
    
    print(f'First step with 100 flashes = {step}')

    print("Day 11 Complete")


def step_ocean(ocean:list[list[int]]) -> int:
    # First, the energy level of each octopus increases by 1.
    flashes = set()
    for p in itertools.product(range(10), range(10)):
        tick(ocean, flashes, *p)

    # Then, any octopus with an energy level greater than 9 flashes. 
    # This increases the energy level of all adjacent octopuses by 1, 
    # including octopuses that are diagonally adjacent. If this causes 
    # an octopus to have an energy level greater than 9, it also flashes. 
    # This process continues as long as new octopuses keep having their 
    # energy level increased beyond 9. (An octopus can only flash 
    # at most once per step.)
    visited = set()
    while flashes:
        flash = flashes.pop()
        visited.add(flash)
        for p in [p for p in getadjacent(*flash) if p not in visited and p not in flashes]:
            tick(ocean, flashes, *p)

    # Finally, any octopus that flashed during this step has its energy 
    # level set to 0, as it used all of its energy to flash.
    for x, y in visited:
        ocean[x][y] = 0
    
    return len(visited)


def tick(ocean:list[list[int]], flashes:set[tuple[int,int]], x:int, y:int) -> None:
    ocean[x][y] += 1
    if ocean[x][y] > 9:
        flashes.add((x,y))


def getadjacent(x:int, y:int) -> list[tuple[int, int]]:
    return [p for p in 
        [(x + p[0] - 1, y + p[1] - 1) for p in itertools.product(range(3), range(3)) 
        if p != (1, 1)]
    if p[0] in range(10) and p[1] in range(10)]