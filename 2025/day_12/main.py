#Presents come in weird shapes
#Measured in standard units
#Placed in 2-d unit grid, cannot be stacked
#Input has list of present shapes and size of egion under tree with list of # of presents of each shape
#Can be rotated and flipped

#Approach
#Parse input into data structure
#Generate orientations of shapes (rotations and flips, 8 total)
#Represent the grid of the xmas tree
#Track which cells are filled
#Check if a placement is valid
#Go back one step if necsesary

#Looks like this problem was easier than thought
#Admittedly,I went to reddit for hints


with open('input', 'r') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

shape_lines = []
region_lines = []

for line in lines:
    if 'x' in line:
        region_lines.append(line)
    else:
        shape_lines.append(line)

#Parse the shape into a list of coordinates where # occurs

shapes = {}
current_shape_id = None
current_rows = []


for line in shape_lines:
    if ':' in line and len(line) <= 3:
        if current_shape_id is not None:
            shapes[current_shape_id] = current_rows
        current_shape_id = int(line.replace(':', ''))
        current_rows = []
    elif line != '':
        current_rows.append(line)

if current_shape_id is not None:
    shapes[current_shape_id] = current_rows

def count_shape_cells(rows):
    return sum(row.count('#') for row in rows)

shape_cells = {shape_id: count_shape_cells(rows) for shape_id, rows in shapes.items()}


regions = []
for line in region_lines:
    parts = line.split('x')
    width = int(parts[0])
    rest = parts[1].split(': ')
    height = int(rest[0])
    counts = [int(x) for x in rest[1].split()]
    regions.append((width, height, counts))

def can_fit_region(width, height, counts):
    grid_area = width * height
    total_piece_area = sum(count * shape_cells[shape_id]
                          for shape_id, count in enumerate(counts))
    return total_piece_area <= grid_area

total = sum(1 for width, height, counts in regions
            if can_fit_region(width, height, counts))

print(total)
