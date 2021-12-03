def day3():
    print('Running Day 3 - a')

    with open('Day3/input.txt','r') as f:
        lines = f.readlines()

    NUM_BITS = 12

    counts = [[0,0] for _ in range(NUM_BITS)]

    for line in lines:
        for i in range(len(line.strip())): # skip line ending?
            if line[i] == '0':
                counts[i][0] += 1
            else:
                counts[i][1] += 1

    gamma, epsilon = 0, 0
    # gammabits = [0 for _ in range(NUM_BITS)]
    # epsilonbits = [0 for _ in range(NUM_BITS)]

    for i in range(len(counts)):
        if counts[i][1] > counts[i][0]:
            # gammabits[i] = 1
            gamma += 1 << (NUM_BITS - 1 - i)
        else:
            # epsilonbits[i] = 1
            epsilon += 1 << (NUM_BITS - 1 - i)

    print(f'gamma = {gamma}, epsilon = {epsilon}, product = {gamma * epsilon}')

    print('Running Day 3 - b')

    print('Day 3 Complete')