with open('input.txt', 'r') as file:
    input = file.read().splitlines()

rows = len(input)
cols = len(input[0])


#Get starting point
for row in range(rows):
    for col in range(cols):
        if input[row][col] == "^":
            current_position = (row, col)

#Write a function
def test_grid(grid, start_row, start_col):
    visited = set()
    current_position = (start_row, start_col)
    direction = (-1, 0)
    while True:
        next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
        if next_position[0] >= rows or next_position[0] < 0 or next_position[1] >= cols or next_position[1] < 0:
            return False
        if (next_position, direction) in visited:
            return True
        if grid[next_position[0]][next_position[1]] == "#":
            if direction == (-1, 0):
                direction = (0, 1) #Move right
            elif direction == (0, 1):
                direction = (1, 0) #Move down
            elif direction == (1, 0):
                direction = (0, -1) #Move left
            elif direction == (0, -1):
                direction = (-1, 0) #Move up
        else:
            current_position = next_position
            visited.add((next_position, direction))


loop_count = 0
#Loop through
for row in range(rows):
    for col in range(cols):
        if input[row][col] != "^" and input[row][col] != "#":
            original_row = input[row]
            new_row = original_row[:col] + "#" + original_row[col + 1:]
            modified_grid = input[:row] + [new_row] + input[row+1:]
            if test_grid(modified_grid, current_position[0], current_position[1]):
                loop_count+=1

print(loop_count)
