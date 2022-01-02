import itertools

def day14():
    print('Running Day 14 - Part 1')

    rules = dict()
    with open('Day14/input.txt', 'r') as f:
        lines = f.readlines()
        template = lines[0].strip()
        for l in lines[2:]:
            (a, b), insert = l.strip().split(' -> ')
            rules[(a, b)] = insert
            
    polymer = template
    for _ in range(10):
        prev = polymer
        polymer = ''
        for pair in itertools.pairwise(prev):
            polymer += pair[0] + rules[pair]
        polymer += prev[-1:]

    counts = [polymer.count(c) for c in set(polymer)]
    print(f'{max(counts) - min(counts)}')

    print('Running Day 14 - Part 2')

    print("Day 14 Complete")
