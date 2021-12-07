from functools import partial


def day3():
    print('Running Day 3 - Part 1')

    with open('Day3/input.txt', 'r') as f:
        numbers = [l.strip() for l in f.readlines()]

    NUM_BITS = 12

    counts = [(0, 0) for _ in range(NUM_BITS)]

    for i in range(NUM_BITS):
        counts[i] = getbitcounts(numbers, i)

    gamma, epsilon = 0, 0
    # gammabits = [0 for _ in range(NUM_BITS)]
    # epsilonbits = [0 for _ in range(NUM_BITS)]

    for i in range(NUM_BITS):
        if counts[i][1] > counts[i][0]:
            # gammabits[i] = 1
            gamma += 1 << (NUM_BITS - 1 - i)
        else:
            # epsilonbits[i] = 1
            epsilon += 1 << (NUM_BITS - 1 - i)

    print(f'gamma = {gamma}, epsilon = {epsilon}, product = {gamma * epsilon}')

    print('Running Day 3 - Part 2')

    o2 = int(findrating(numbers, partial(filternumbers, comp=o2comp)), 2)
    co2 = int(findrating(numbers, partial(filternumbers, comp=co2comp)), 2)

    print(f'o2 = {o2}, co2 = {co2}, product = {o2 * co2}')

    print('Day 3 Complete')


def getbitcounts(numbers, bit):
    zeroes = len([n for n in numbers if n[bit] == '0'])
    return zeroes, len(numbers) - zeroes


def findrating(numbers, bitfilterfunc):
    i = 0
    while len(numbers) > 1:
        numbers = bitfilterfunc(numbers, i)
        i += 1
    return numbers[0]


def filternumbers(numbers, bit, comp):
    counts = getbitcounts(numbers, bit)
    criteria = comp(counts)
    return [n for n in numbers if n[bit] == criteria]


def o2comp(counts):
    return '1' if counts[1] >= counts[0] else '0'


def co2comp(counts):
    return '0' if counts[0] <= counts[1] else '1'
