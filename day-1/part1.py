# Useful imports
import math
import numpy as np
from functools import cache

# Placeholders to be filled when copying the template
PART = 1
DAY = 1
YEAR = 2016

# The expected result from the test input, if using a test input
TEST_RESULT = 12

def add(a, b, c):
    return [a[0] + c * b[0], a[1] + c * b[1]]

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip().split(', ') for line in f.readlines()][0]
    
    pos = [0, 0]
    d = 0
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    for instruction in lines:
        if instruction[0] == 'R':
            d += 1
        else:
            d -= 1
        d = d % 4
        pos = add(pos, directions[d], int(instruction[1:]))

    # --- SOLUTION CODE ---
    return abs(pos[0]) + abs(pos[1])

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
