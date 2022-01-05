import itertools
import math
import re


def day17():
    print('Running Day 17 - Part 1')

    with open('Day17/input.txt', 'r') as f:
        match = re.compile('^target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)$').match(f.readline().strip())
        xmin_t, xmax_t, ymin_t, ymax_t = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))

    # The puzzle example and the input target both have a negative y range, which makes sense given the puzzle.
    # Shooting straight up, the highest velocity we can shoot and still hit the target in the 1st negative step on the way down is -ymin_t.
    # Since the height degrades by 1 each step, the solution is simply `sum([1..n])`, or `(n * (n-1)) / 2`
    ymax_v = -ymin_t

    print(f'Max height = {(ymax_v * (ymax_v - 1)) // 2}')

    print('Running Day 17 - Part 2')

    # This minumum x velocity in the first whole number that would degrade to the target's min x.
    # This is the same `sum([1..n])` as above, except we need to solve for n knowing the answer.
    # `(n * (n-1)) / 2 >= xmin_t` which in quadratic form is `.5n² +.5n - xmin_t >= 0`
    # We use the quadratic formula `n = (-b ± √(b² - 4ac)) / 2a`, simplified further after substituting a and b for .5
    xmin_v = math.ceil(-.5 + math.sqrt(abs(.25 - 2 * xmin_t)))

    hits = 0
    xmax_v = xmax_t # as the highest x velocity we can shoot and still reach the target would be to hit the right edge of the target in the first step.
    ymin_v = ymin_t # as the lowest y velocity we can shoot and still reach the target would be to hit the bottom edge of the target in the first step.
    for xv_c, yv_c in itertools.product(range(xmin_v, xmax_v + 1), range(ymin_v, ymax_v + 1)):
        # Simulate each shot and see if it hits the target.
        x, y, xv, yv = 0, 0, xv_c, yv_c
        while x <= xmax_t and y >= ymin_t:
            x, y = x + xv, y + yv
            xv, yv = max(xv - 1, 0), yv - 1
            if xmin_t <= x <= xmax_t and ymin_t <= y <= ymax_t:
                hits += 1
                break

    print(f'Velocities hitting target = {hits}')

    print("Day 17 Complete")
