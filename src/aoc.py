import time
from Day1.day1 import *
from Day2.day2 import *
from Day3.day3 import *
from Day4.day4 import *
from Day5.day5 import *
from Day6.day6 import *
from Day7.day7 import *
from Day8.day8 import *
from Day9.day9 import *
from Day10.day10 import *
from Day11.day11 import *
from Day12.day12 import *
from Day13.day13 import *
from Day14.day14 import *
from Day15.day15 import *
from Day16.day16 import *
from Day17.day17 import *


def timeday(day, method):
    t = time.time()
    method()
    t = time.time() - t

    print(f'Elapsed Time for Day {day}: {t:.3f} secs\n')


if __name__ == "__main__":
    print("\n🎅🎅🎅🎅🎅 ADVENT OF CODE 2021 🎅🎅🎅🎅🎅\n")

    t = time.time()

    timeday(1, day1)
    timeday(2, day2)
    timeday(3, day3)
    timeday(4, day4)
    timeday(5, day5)
    timeday(6, day6)
    timeday(7, day7)
    timeday(8, day8)
    timeday(9, day9)
    timeday(10, day10)
    timeday(11, day11)
    timeday(12, day12)
    timeday(13, day13)
    timeday(14, day14)
    timeday(15, day15)
    timeday(16, day16)
    timeday(17, day17)

    t = time.time() - t

    print(f'Total Elapsed Time: {t:.3f} secs\n')
