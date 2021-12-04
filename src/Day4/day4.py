def day4():
    print('Running Day 4 - a')

    with open('Day4/input.txt','r') as f:
        lines = [l.strip() for l in f.readlines()]

    calls = [int(s) for s in lines[0].split(',')]

    boards = []
    i = 2
    while i < len(lines):
        boards.append(BingoBoard(len(boards) +1, lines[i:i+5]))
        i += 6

    winner = None

    i = 0
    while winner is None:
        for board in boards:
            board.mark(calls[i])
            if board.check():
                winner = board
        i += 1

    print(f'Winner! Board {winner.id}, sum={winner.sum()}, last call={calls[i]}, score={winner.sum() * calls[i - 1]}')

    print('Running Day 4 - b')

class BingoBoard:
    id : int = 0
    spaces : list[list[int]] = None
    marks : list[list[bool]] = None

    def __init__(self, id:int, lines:list[str]) -> None:
        self.id = id
        self.spaces = [[int(s) for s in l.split()] for l in lines]
        self.marks = [[False for _ in range(5)] for _ in range(5)]

    def mark(self, call:int) -> None:
        for i in range(5):
            for j in range(5):
                if self.spaces[i][j] == call:
                    self.marks[i][j] = True

    def check(self) -> bool:
        def checkrow(i) -> bool:
            for j in range(5):
                if not self.marks[i][j]:
                    return False
            return True

        def checkcol(j) -> bool:
            for i in range(5):
                if not self.marks[i][j]:
                    return False
            return True

        for i in range(5):
            if checkrow(i) or checkcol(i):
                return True

        return False

    def sum(self) -> int:
        sum = 0
        for i in range(5):
            for j in range(5):
                if not self.marks[i][j]:
                    sum += self.spaces[i][j]
        return sum