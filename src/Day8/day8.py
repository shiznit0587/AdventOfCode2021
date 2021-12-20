def day8():
    print('Running Day 8 - Part 1')

    with open('Day8/input.txt', 'r') as f:
        entries = [Entry(l) for l in f.readlines()]

    count = 0
    for p in map(lambda e : e.output, entries):
        for s in p.signals:
            match len(s):
                case (2|3|4|7):
                    count += 1

    print(f'Unique digit appearances = {count}')

    print('Running Day 8 - Part 2')

    print('Day 8 Complete')

class Entry:
    def __init__(self, line:str) -> None:
        parts = [s.strip() for s in line.split('|')]
        self.patterns = SignalPatterns(parts[0])
        self.output = SignalPatterns(parts[1])

class SignalPatterns:
    def __init__(self, parts:str) -> None:
        self.signals = parts.split()
