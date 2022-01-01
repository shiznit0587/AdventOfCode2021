import re


def day13():
    print('Running Day 13 - Part 1')

    dots: set[tuple[int, int]] = {}
    folds: list[tuple[str, int]] = []

    with open('Day13/input.txt', 'r') as f:
        dot_re = re.compile('^(\d+),(\d+)$')
        fold_re = re.compile('^fold along (x|y)=(\d+)$')

        for line in f.readlines():
            dot_match = dot_re.match(line.strip())
            fold_match = fold_re.match(line.strip())
            if dot_match is not None:
                dots.add((int(dot_match.group(1)), int(dot_match.group(2))))
            elif fold_match is not None:
                folds.append((fold_match.group(1), int(fold_match.group(2))))

    part1_complete = False

    for fold in folds:
        match fold:
            case ('x', x):
                for d in {d for d in dots if d[0] > x}:
                    dots.remove(d)
                    dots.add((x - (d[0] - x), d[1]))
            case ('y', y):
                for d in {d for d in dots if d[1] > y}:
                    dots.remove(d)
                    dots.add((d[0], y - (d[1] - y)))
        if not part1_complete:
            print(f'Number of Dots = {len(dots)}')
            part1_complete = True

    print('Running Day 13 - Part 2')

    print('Activation Code:')

    xmax, ymax = max(x for x, _ in dots), max(y for _, y in dots)
    for y in range(ymax + 1):
        print(''.join('#' if (x, y) in dots else ' ' for x in range(xmax + 1)))

    print("Day 13 Complete")
