import itertools


def day19():
    print('Running Day 19 - Part 1')

    scanners: list[Scanner] = []

    with open('Day19/input.txt', 'r') as f:
        nextbeaconid = 0
        for line in f.readlines():
            if line.startswith('---'):
                scanner = Scanner(int(line.split()[2]))
                scanners.append(scanner)
            elif line[0] != '\n':
                beacon = Beacon(nextbeaconid, *map(int, line.split(',')))
                scanner.beacons.append(beacon)
                nextbeaconid += 1

    for s in scanners:
        s.calcdistances()

    # Hmm, okay.
    # I think two scanners will match up if they have a set of 12 points that are positioned relative to each other the same way.
    # The best I can think to check for this is via manhattan distances.
    # 12 points => 12*11 / 2 => 66 manhattan distances.
    # It's... quite an assumption though. And once I think two scanners will match up, how do I pick out which points were used?
    # Do I have to recalculate the distances between points? (Do I just store them, and ID the beacons somehow?)

    print('Running Day 19 - Part 2')

    print("Day 19 Complete")


class Scanner:
    pass


class Beacon:
    id: int = None
    scanner: Scanner = None
    x, y, z = None, None, None

    def __init__(self, id, x, y, z) -> None:
        self.id, self.x, self.y, self.z = id, x, y, z

    def __repr__(self) -> str:
        return f'Beacon(id={self.id}, x={self.x}, y={self.y}, z={self.z})'


class Scanner:
    id: int = None
    beacons: list[Beacon] = None
    distances: dict[tuple[int, int], int] = None

    def __init__(self, id: int) -> None:
        self.id = id
        self.beacons = []
        self.distances = dict()

    def __repr__(self) -> str:
        return f'Scanner(id={self.id})'

    def calcdistances(self) -> None:
        distset = set()
        for a, b in itertools.permutations(self.beacons, 2):
            if a.id < b.id:
                dist = abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z)
                self.distances[a.id, b.id] = dist
                if dist in distset:
                    raise
                distset.add(dist)
        # I think for my algorithm to work, no two distances can be the same.
        # verified this is true for sample input. try again for real input.
        # had a typo. This isn't true for either input.
