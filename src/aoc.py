import time
from Day1.day1 import *
from Day2.day2 import *
from Day3.day3 import *
from Day4.day4 import *
from Day5.day5 import *

def timeday(day, method):
    t = time.time()
    method()
    t = time.time() - t

    print(f'Elapsed Time for Day {day}: {t:.3f} ms')

if __name__ == "__main__":
    print("\n🎅🎅🎅🎅🎅 ADVENT OF CODE 2021 🎅🎅🎅🎅🎅\n")

    t = time.time()

    timeday(1, day1)
    timeday(2, day2)
    timeday(3, day3)
    timeday(4, day4)
    timeday(5, day5)

    t = time.time() - t

    print(f'Total Elapsed Time: {t:.3f} ms')
