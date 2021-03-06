import itertools
import math


def day18():
    print('Running Day 18 - Part 1')

    with open('Day18/input.txt', 'r') as f:
        numbers = [SFNumber.parse(l) for l in f.readlines()]

    print(f'Magnitude of sum = {sum(numbers).magnitude()}')

    print('Running Day 18 - Part 2')

    print(f'Maximum Magnitude of any sum = {max(map(lambda p: (p[0] + p[1]).magnitude(), itertools.permutations(numbers, 2)))}')

    print("Day 18 Complete")


class SFDigit:
    def __init__(self, value: int, depth: int) -> None:
        self.value = value
        self.depth = depth

    def __repr__(self) -> str:
        return f'SFDigit(value={self.value}, depth={self.depth})'


class SFNumber(list[SFDigit]):
    pass


class SFNumber(list[SFDigit]):
    def __new__(self):
        return list.__new__(SFNumber)

    @staticmethod
    def parse(input: str) -> SFNumber:
        number: SFNumber = SFNumber()
        depth = 0
        for p in range(0, len(input)):
            match input[p]:
                case '[':
                    depth += 1
                case ']':
                    depth -= 1
                case d if d.isdigit():
                    number.append(SFDigit(int(d), depth))
        return number

    def reduce(self) -> None:
        while True:
            i = self.find_explode()
            if i is not None:
                self.explode(i)
                continue
            i = self.find_split()
            if i is not None:
                self.split(i)
                continue
            return

    def find_explode(self) -> int | None:
        for i in range(len(self)):
            if self[i].depth >= 5:
                return i
        return None

    def explode(self, i: int) -> None:
        if i > 0:
            self[i-1].value += self[i].value
        # assume self[i+1] is the other half of this exploding pair
        if i + 2 < len(self):
            self[i+2].value += self[i+1].value
        self.pop(i+1)
        self[i].depth -= 1
        self[i].value = 0

    def find_split(self) -> int | None:
        for i in range(len(self)):
            if self[i].value >= 10:
                return i
        return None

    def split(self, i: int) -> None:
        v, d = self[i].value, self[i].depth
        lv, rv = math.floor(v / 2), math.ceil(v/2)
        rd, _ = self[i], self.insert(i, SFDigit(lv, d + 1))
        rd.depth, rd.value = rd.depth + 1, rv

    def magnitude(self) -> int:
        mag = SFNumber()
        for d in self:
            mag.append(SFDigit(d.value, d.depth))

        while len(mag) > 1:
            for i in range(len(mag)):
                if mag[i].depth == mag[i+1].depth:
                    rd = mag.pop(i+1)
                    mag[i].value = 3 * mag[i].value + 2 * rd.value
                    mag[i].depth -= 1
                    break

        return mag[0].value

    def __add__(self, other: SFNumber) -> SFNumber:
        sum = SFNumber()
        for d in itertools.chain(self, other):
            sum.append(SFDigit(d.value, d.depth + 1))
        sum.reduce()
        return sum

    def __radd__(self, other: SFNumber) -> SFNumber:
        # Sometimes this gets called with int 0, quirk of the sum folding algorithm.
        if not isinstance(self, SFNumber):
            return other
        elif not isinstance(other, SFNumber):
            return self
        else:
            return SFNumber.__add__(other, self)
