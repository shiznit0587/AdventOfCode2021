import itertools


def day14():
    print('Running Day 14 - Part 1')

    rules = dict()
    with open('Day14/input.txt', 'r') as f:
        lines = f.readlines()
        template = lines[0].strip()
        for l in lines[2:]:
            (a, b), c = l.strip().split(' -> ')
            rules[(a, b)] = c

    polymer = template
    for _ in range(10):
        prev = polymer
        polymer = ''
        for pair in itertools.pairwise(prev):
            polymer += pair[0] + rules[pair]
        polymer += prev[-1:]

    counts = [polymer.count(c) for c in set(polymer)]
    print(f'Element Range Delta = {max(counts) - min(counts)}')

    print('Running Day 14 - Part 2')

    char_counts = {c: template.count(c) for c in set(template)}
    pair_counts = {}
    for pair in itertools.pairwise(template):
        if pair in pair_counts:
            pair_counts[pair] += 1
        else:
            pair_counts[pair] = 1

    for _ in range(40):
        prev_pair_counts = pair_counts.copy()
        for (a, b), c in rules.items():
            if (a, b) in prev_pair_counts:
                count = prev_pair_counts[a, b]
                pair_counts[a, b] -= count
                if c in char_counts:
                    char_counts[c] += count
                else:
                    char_counts[c] = count
                if (a, c) in pair_counts:
                    pair_counts[a, c] += count
                else:
                    pair_counts[a, c] = count
                if (c, b) in pair_counts:
                    pair_counts[c, b] += count
                else:
                    pair_counts[c, b] = prev_pair_counts[a, b]

    print(f'Element Range Delta = {max(char_counts.values()) - min(char_counts.values())}')

    print("Day 14 Complete")
