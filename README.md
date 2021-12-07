# AdventOfCode2021

**[Advent of Code 2021](https://adventofcode.com/2021)**

You're minding your own business on a ship at sea when the overboard alarm goes off! You rush to see if you can help. Apparently, one of the Elves tripped and accidentally sent the sleigh keys flying into the ocean!

Before you know it, you're inside a submarine the Elves keep ready for situations like this. It's covered in Christmas lights (because of course it is), and it even has an experimental antenna that should be able to track the keys if you can boost its signal strength high enough; there's a little meter that indicates the antenna's signal strength by displaying 0-50 **stars**.

Your instincts tell you that in order to save Christmas, you'll need to get all **fifty stars** by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants **one star**. Good luck!

## Resources

- [Python Cheat Sheet](https://www.pythoncheatsheet.org/)
- [W3 Schools - Python](https://www.w3schools.com/python/)
- [Python Package Index](https://pypi.org/)
- [Python 3.9 Documentation](https://docs.python.org/3.9/)

## Journal

For this year, I decided to try my hand at **Python**. Rachel's been learning it in one of her PHD courses, so I thought it'd be fun with her able to follow along this year.

### Day 5

- *Finally* utilizing regular expressions for parsing the input.
- I hit a hurdle for a bit for lines with *de*scending x or y values.
- I used type aliases for cleaner type hinting throughout my code.
- I got tripped up on diagonals in part 2 by initially always traversing from the minimum of each axis to the max of each axis defined by the line, basically traversing a different line entirely, when the line was at a decreasing angle.

### Day 4

- First use of a class. I don't like that every method requires specific use of `self` to access instance attributes.
- Started using type hinting more, really helps assist both the language server and the programmer.
- Finally used `map` and `all` successfully.
- I tried using list duplication with `*` as a shorthand for construction, but learned the hard was that the list's contents are not deep-copied, even when trivially copyable.

### Day 3

- Bit shifting operations are pretty standard in python, unlike F# last year.
- Ternary syntax is going to take some getting used to.
- List comprehension supports an `if` clause for filtering, that's cool.
- Utilized partial functions and named arguments to commonize the O2 and CO2 code paths as much as possible.
- Radix-based string to int conversion was super helpful at the end.
- Python doesn't require a specific `def` declaration order like c or rust, good to know!

### Day 2

- List comprehension seems easier to work with that the `map()` function.
- I really wanted to use the new `match` patterns from python 3.10, but it was taking a long time to get my dev environment configured to use it by default. Between the system installs, brew installs, and pyenv installs, I gave up trying to get them all to play nicely and not keep overriding the default to 3.9.

### Day 1

- I modeled this year's project after last year's. The structure with a README.md per day is nice, and code-wise, I'm starting with timing support already implemented.
- I somehow have four installs of python on my computer. Getting vscode using the correct one was simple once I tried for myself instead of trusting google.
- I didn't think I'd have to learn i/o just yet. I had a pathing issue when debugging, fixed by adding `cwd` to my `launch.json`.
- I feel right at home with list slicing, which is a weird statement given two of the languages I primarily use at work, Java and Haxe, don't have it, and C# does (ala Ranges) but we're stuck on an old version.
- Python has string interpolation, which made my happier than it had any right to.