def day10():
    print('Running Day 10 - Part 1')

    with open('Day10/input.txt', 'r') as f:
        lines = [s.strip() for s in f.readlines()]

    score = 0
    for line in lines:
        ops, i, corrupted, = '', 0, False
        while not corrupted and i < len(line):
            c = line[i]
            op = ops[0] if len(ops) > 0 else ''
            match (op, line[i]):
                case (_, '(' | '[' | '{' | '<'):
                    ops = c + ops
                case ('(',')') | ('[',']') | ('{','}') | ('<','>'):
                    ops = ops[1:]
                case _:
                    corrupted = True
                    match c:
                        case ')': score += 3
                        case ']': score += 57
                        case '}': score += 1197
                        case '>': score += 25137
            i += 1

    print(f'Score = {score}')

    print('Running Day 10 - Part 2')

    print("Day 10 Complete")