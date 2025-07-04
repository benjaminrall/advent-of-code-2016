# Useful imports
import math
import numpy as np
from functools import cache

# Placeholders to be filled when copying the template
PART = 2
DAY = 1
YEAR = 2016

# The expected result from the test input, if using a test input
TEST_RESULT = 4

def add(a, b, c):
    return (a[0] + c * b[0], a[1] + c * b[1])

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip().split(', ') for line in f.readlines()][0]
    
    visited = set([(0, 0)])
    pos = (0, 0)
    d = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    i = 0
    while True:
        instruction = lines[i]
        if instruction[0] == 'R':
            d += 1
        else:
            d -= 1
        d = d % 4

        for _ in range(int(instruction[1:])):
            pos = add(pos, directions[d], 1)
            if pos in visited:
                return abs(pos[0]) + abs(pos[1])
            visited.add(pos)
        i = (i + 1) % len(lines)


if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
