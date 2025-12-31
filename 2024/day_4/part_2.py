with open('input', 'r') as file:
    input = file.read().splitlines()

rows = len(input)
cols = len(input[0])

counter = 0

for row in range(rows):
    for col in range(cols):
        if input[row][col] == "A":
            if row-1 < 0 or col-1 < 0 or col+1 >= cols or row+1 >= rows:
                continue
            top_left = input[row - 1][col - 1]
            top_right = input[row - 1][col + 1]
            bottom_left = input[row + 1][col - 1]
            bottom_right = input[row + 1][col + 1]
            if top_left == "M" and bottom_right == "S" and top_right == "M" and bottom_left == "S":
                counter+=1
            elif top_left == "M" and bottom_right == "S" and top_right == "S" and bottom_left == "M":
                counter+=1
            elif top_left == "S" and bottom_right == "M" and top_right == "M" and bottom_left == "S":
                counter+=1
            elif top_left == "S" and bottom_right == "M" and top_right == "S" and bottom_left == "M":
                counter+=1
        else:
            continue

print(counter)
