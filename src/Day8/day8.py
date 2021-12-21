def day8():
    print('Running Day 8 - Part 1')

    with open('Day8/input.txt', 'r') as f:
        entries = [Entry(l) for l in f.readlines()]

    count = 0
    for p in map(lambda e : e.output, entries):
        for s in p:
            match len(s):
                case (2|3|4|7):
                    count += 1

    print(f'Unique digit appearances = {count}')

    print('Running Day 8 - Part 2')

    e = Entry(
        'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |\
         cdfeb fcadb cdfeb cdbaf')
    deduce(e)
    decode(e)

    print('Day 8 Complete')

class Entry:
    def __init__(self, line:str) -> None:
        parts = [s.strip() for s in line.split('|')]
        self.patterns = parts[0].split()
        self.output = parts[1].split()

def decode(entry:Entry) -> None:
    entry.value = 0

def deduce(entry:Entry) -> None:
    pipmap = dict()
    entry.pipmap = pipmap

    all_pips = 'abcdefg'

    # - 1 has 2 pips, so those must map to `cf`.
    pips_of_1 = [p for p in entry.patterns if len(p) == 2][0]

    # - 7 has 3 pips, so those must map to `acf`.
    #   whichever pip is in 7 and not in 1 must map to *`a`*.
    pips_of_7 = [p for p in entry.patterns if len(p) == 3][0]
    pipmap[[p for p in pips_of_7 if p not in pips_of_1][0]] = 'a'

    # - Of the 3 numbers with 6 pips (0,6,9),
    #     3 of the pips are _not_ duplicated and must map to `cde`.
    #       One of those existed in 1. That overlap maps to *`c`*.
    #         We can then also deduce *`f`*.
    patterns_with_6 = [p for p in entry.patterns if len(p) == 6]
    unshared = [c for c in all_pips if len([p for p in patterns_with_6 if c in p]) in range(1,3)]
    pipmap[[c for c in unshared if c in pips_of_1][0]] = 'c'
    pipmap[[c for c in pips_of_1 if c not in pipmap][0]] = 'f'
    
    # - Of the 3 numbers with 5 pips (2,3,5),
    #   3 pips will exist in 3 numbers, those must map to `adg`.
    #     We already know `a`. We'll deduce `d` from `g` later.
    patterns_with_5 = [p for p in entry.patterns if len(p) == 5]
    duplicated_in_5s = [c for c in all_pips if len([p for p in patterns_with_5 if c in p]) == 3]

    # - 4 has 4 pips, so those must map to `bcdf`.
    #   Whichever 2 pips don't overlap 1 map to `bd`,
    #     *`d`* is whichever was in all 3 numbers with 5 pips.
    #       We can then deduce *`g`*.
    #     *`b`* is the other one.
    pips_of_4 = [p for p in entry.patterns if len(p) == 4][0]
    b_or_d = [c for c in pips_of_4 if c not in pips_of_1]
    pipmap[[c for c in b_or_d if c in duplicated_in_5s][0]] = 'd'
    pipmap[[c for c in duplicated_in_5s if c not in pipmap][0]] = 'g'
    pipmap[[c for c in b_or_d if c not in pipmap][0]] = 'b'

    # At this point we've deduced all but *`e`*.
    pipmap[[c for c in all_pips if c not in pipmap][0]] = 'e'

    # Set entry.digits
    
