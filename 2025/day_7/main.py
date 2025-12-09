#One beam needs current position and direction
#The direction will always be down
#Beam hits splitter
#Direction goes left and right -- need to remove original beam and add two new beams
#Beams disappear when it is off the grid or hits a splitter
#Simulation ends when active_beams is empty
#If beams hit the same cell multiple times, only count it once
#When compute next position, check if out of bounds first

with open('input.txt', 'r') as f:
    grid = f.readlines()

grid = [line.strip() for line in grid]

rows = len(grid)
cols = len(grid[0])

#Find starting point
start_row = None
start_col = None
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == "S":
            start_row = row
            start_col = col
            break
    if start_row is not None:
        break

if start_row + 1 < rows:
    active_beams = [(start_row+1, start_col)]
else:
    active_beams = []

counter = 0

while active_beams:
    next_beams = []
    for beam in active_beams:
        row = beam[0]
        col = beam[1]
        next_row = row+1
        #Check if in bounds
        if next_row >= rows:
            continue
        cell = grid[next_row][col]
        if cell == ".":
            next_beams.append((next_row, col))
        elif cell == "^":
            counter += 1
            if col+1 < cols:
                right_beam = (row+1, col+1)
                next_beams.append(right_beam)
            if col-1 >= 0:
                left_beam = (row + 1, col - 1)
                next_beams.append(left_beam)
    active_beams = list(set(next_beams))


print(f"There are {counter} beams.")