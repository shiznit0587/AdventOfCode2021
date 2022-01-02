def day10():
    print('Running Day 10 - Part 1')

    with open('Day10/input.txt', 'r') as f:
        lines = [s.strip() for s in f.readlines()]

    c_score = 0
    ac_scores = []
    for line in lines:
        ops, i, corrupted, = '', 0, False
        while not corrupted and i < len(line):
            c = line[i]
            op = ops[0] if len(ops) > 0 else ''
            match (op, line[i]):
                case (_, '(' | '[' | '{' | '<'):
                    ops = c + ops
                case ('(', ')') | ('[', ']') | ('{', '}') | ('<', '>'):
                    ops = ops[1:]
                case _:
                    corrupted = True
                    match c:
                        case ')': c_score += 3
                        case ']': c_score += 57
                        case '}': c_score += 1197
                        case '>': c_score += 25137
            i += 1
        if not corrupted:
            score = 0
            for c in ops:
                match c:
                    case '(': score = score * 5 + 1
                    case '[': score = score * 5 + 2
                    case '{': score = score * 5 + 3
                    case '<': score = score * 5 + 4
            ac_scores.append(score)

    print(f'Corruption Score = {c_score}')
    print('Running Day 10 - Part 2')
    print(f'Autocomplete Score = {sorted(ac_scores)[len(ac_scores)//2]}')
    print("Day 10 Complete")
