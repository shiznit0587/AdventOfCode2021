def day12():
    print('Running Day 12 - Part 1')

    caves: dict[str, set[str]] = dict()

    with open('Day12/input.txt', 'r') as f:
        for line in f.readlines():
            a, b = line.strip().split('-')
            caves = {**{a: set(), b: set()}, **caves}
            caves[a].add(b)
            caves[b].add(a)

    paths: list[Path] = []
    queue: list[State] = [(['start'], 'start')]

    while queue:
        path, cave = queue.pop(0)
        for adj in caves[cave]:
            if adj == 'end':
                paths.append(path + [adj])
            elif adj.isupper() or adj not in path:
                queue.append((path + [adj], adj))

    print(f'Number of Paths = {len(paths)}')

    print('Running Day 12 - Part 2')

    print("Day 12 Complete")


Path = list[str]
State = tuple[Path, str]
