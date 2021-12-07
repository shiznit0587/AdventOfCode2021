def day7():
    print('Running Day 7 - Part 1')

    with open('Day7/input.txt', 'r') as f:
        crabs = [int(s) for s in f.readline().strip().split(',')]

    distances = dict()
    calcdistances(crabs, distances, getfuelamount_1)
    target = min(distances, key=distances.get)

    print(f'Target = {target}, Fuel = {distances[target]}')

    print('Running Day 7 - Part 2')

    distances = dict()
    calcdistances(crabs, distances, getfuelamount_2)
    target = min(distances, key=distances.get)

    print(f'Target = {target}, Fuel = {distances[target]}')

    print("Day 7 Complete")


def calcdistances(crabs, distances, fuelcalcmethod):
    mincrab = min(crabs)
    maxcrab = max(crabs)

    for c in crabs:
        for pos in range(mincrab, maxcrab + 1):
            fuel = fuelcalcmethod(abs(c - pos))
            if pos in distances:
                distances[pos] += fuel
            else:
                distances[pos] = fuel


def getfuelamount_1(distance):
    return distance


fuelamounts = [0]


def getfuelamount_2(distance):
    if len(fuelamounts) < distance + 1:
        for i in range(len(fuelamounts), distance + 1):
            fuelamounts.append(fuelamounts[i-1] + i)
    return fuelamounts[distance]
