#Worksheet has a list of problems
#Each problem has a group of numbers that need to be added or multiplied
#Numbers are vertical

import math

lines = []
with open('input.txt', 'r') as f:
    for line in f:
        line = line.rstrip("\n")
        if line:
            lines.append(line)

#Find max length
max_length = len(max(lines, key=len))

input = []
for line in lines:
    normalized_lines = line.rstrip(" ")
    input.append(normalized_lines)


#Pad the data, we need to maintain the white space in between problems
padded_input = []
for row in input:
    if len(row) < max_length:
        padded_row = row + " " * (max_length - len(row))
    else:
        padded_row = row
    padded_input.append(padded_row)


#Shape our data into a grid of characters
grid = []
for row in padded_input:
    grid.append(list(row))


#Let's find the problem separators
num_cols = len(grid[0])
num_rows = len(grid)

for col in range(num_cols):
    if all(grid[row][col] == " " for row in range(num_rows)):
        print(f"Column {col} is EMPTY")
    else:
        print(f"Column {col} is NOT empty")



#Locate the column blocks where problems are present
#List of tuples
problem_blocks = []
in_block = False
start = None

for col in range(num_cols):
    if all(grid[row][col] == " " for row in range(num_rows)):
        problem_blocks.append((start, col - 1))
        in_block = False
    else:
        if not in_block:
            start = col
            in_block = True
if in_block:
    problem_blocks.append((start, num_cols - 1))

#Extract operator
operators = []
for start, end in problem_blocks:
    op = None
    for col in range(start, end+1):
        char = grid[num_rows -1][col]
        if char in "+*":
            op = char
            break
    operators.append(op)

#Get numbers from each block finally
numbers_per_block = []

for start, end in problem_blocks:
    nums = []
    for row in range(num_rows - 1):
        segment = ''.join(grid[row][col] for col in range(start, end+1))
        cleaned = segment.strip()
        if cleaned.isdigit():
            nums.append(int(cleaned))
    numbers_per_block.append(nums)

print(numbers_per_block)

#Let's do the math now
total = 0

for nums, op in zip(numbers_per_block, operators):
    if op == "+":
        result = sum(nums)
    else:
        result = math.prod(nums)
    total += result

print(total)