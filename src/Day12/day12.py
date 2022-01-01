from typing import Callable


def day12():
    print('Running Day 12 - Part 1')

    caves: Caves = dict()

    with open('Day12/input.txt', 'r') as f:
        for line in f.readlines():
            a, b = line.strip().split('-')
            caves = {**{a: set(), b: set()}, **caves}
            caves[a].add(b)
            caves[b].add(a)

    print(f'Number of Paths = {traverse(caves, visit_1)}')
    print('Running Day 12 - Part 2')
    print(f'Number of Paths = {traverse(caves, visit_2)}')
    print("Day 12 Complete")


Caves = dict[str, set[str]]
Path = list[str]
State = tuple[Path, str]


def traverse(caves: Caves, visitpred: Callable[[Path, str], bool]) -> int:
    pathcount = 0
    queue: list[State] = [(['start'], 'start')]

    while queue:
        path, cave = queue.pop(0)
        for adj in caves[cave]:
            if adj == 'end':
                pathcount += 1
            elif visitpred(path, adj):
                queue.append((path + [adj], adj))

    return pathcount


def visit_1(path: Path, cave: str) -> bool:
    return cave.isupper() or cave not in path


def visit_2(path: Path, cave: str) -> bool:
    match cave:
        case 'start': return False
        case 'end': return True
        case _ if cave.isupper(): return True
        case _ if cave not in path: return True
        case _:
            smallcaves = [c for c in path if c.islower()]
            return len(smallcaves) == len(set(smallcaves))
