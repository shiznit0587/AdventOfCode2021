import itertools
import math


def day18():
    print('Running Day 18 - Part 1')

    with open('Day18/input.txt', 'r') as f:
        numbers = [SFNumber.parse(l) for l in f.readlines()]

    print(f'Magnitude of sum = {sum(numbers).magnitude()}')

    print('Running Day 18 - Part 2')

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
            d.depth += 1
            sum.append(d)
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


'''
Here there be dragons (dead code)
'''


class SnailfishNumber:
    pass


class SnailfishNumber:
    depth: int = 0
    left: SnailfishNumber | int = None
    right: SnailfishNumber | int = None
    parent: SnailfishNumber

    @staticmethod
    def parse(input: str) -> SnailfishNumber:
        root = SnailfishNumber()
        stack = [root]
        for p in range(1, len(input)):
            match input[p]:
                case '[':
                    num = SnailfishNumber()
                    num.parent = stack[-1]
                    num.depth = len(stack)
                    if stack[-1].left is None:
                        stack[-1].left = num
                    else:
                        stack[-1].right = num
                    stack += [num]
                case ']':
                    stack.pop()
                case d if d.isdigit():
                    if stack[-1].left is None:
                        stack[-1].left = int(d)
                    else:
                        stack[-1].right = int(d)
        return root

    def __str__(self):
        return f'[{self.left},{self.right}]'

    def __add__(self, other: SnailfishNumber) -> SnailfishNumber:
        self.increasedepth()
        other.increasedepth()
        sum = SnailfishNumber()
        self.parent, other.parent = sum, sum
        sum.left, sum.right = self, other
        sum.reduce()
        return sum

    def __radd__(self, other: SnailfishNumber) -> SnailfishNumber:
        # Sometimes this gets called with int 0, quirk of the sum folding algorithm.
        if not isinstance(self, SnailfishNumber):
            return other
        elif not isinstance(other, SnailfishNumber):
            return self
        else:
            return SnailfishNumber.__add__(other, self)

    def increasedepth(self) -> None:
        self.depth += 1
        if isinstance(self.left, SnailfishNumber):
            self.left.increasedepth()
        if isinstance(self.right, SnailfishNumber):
            self.right.increasedepth()

    def reduce(self) -> None:
        while self.explode() or self.split():
            _ = 0  # just keep exploding or splitting

    def explode(self) -> bool:
        exploded = False
        if self.depth >= 4:
            # do explode

            # add left number to number to its left
            # how do I do this?
            # If I'm my parent's right, then I need the right-side of my parent's left
            # If I'm my parent's left, then I need the right-side of my grandparent's ... what?
            # this is a tree-search.
            # But now I'm wondering... should I just use a flat list of some structure instead of a tree?
            # what data would I need in each?
            # I'd need to know its depth.
            # would I need to know if it's a left or right?
            # I may... a 'pair' explodes, and adjacent pairs could have the same depth.
            # but, I could always assume when searching left-to-right that when I hit a number
            # that needs to explode, the next number is part of the same pair.

            # add right number to number to its right
            # how do I do this?

            # replace pair with 0
            if self.parent.left is self:
                self.parent.left = 0
            elif self.parent.right is self:
                self.parent.right = 0

            exploded = True
        if not exploded and isinstance(self.left, SnailfishNumber):
            exploded = self.left.explode()
        if not exploded and isinstance(self.right, SnailfishNumber):
            exploded = self.right.explode()
        return exploded

    def split(self) -> bool:
        return False
