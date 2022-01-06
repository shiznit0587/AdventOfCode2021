def day19():
    print('Running Day 19 - Part 1')

    with open('Day19/input.txt', 'r') as f:
        lines = f.readlines()

    # Hmm, okay.
    # I think two scanners will match up if they have a set of 12 points that are positioned relative to each other the same way.
    # The best I can think to check for this is via manhattan distances.
    # 12 points => 12*11 / 2 => 66 manhattan distances.
    # It's... quite an assumption though. And once I think two scanners will match up, how do I pick out which points were used?
    # Do I have to recalculate the distances between points? (Do I just store them, and ID the beacons somehow?)

    print('Running Day 19 - Part 2')

    print("Day 19 Complete")
