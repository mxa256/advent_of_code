#Word search
#Start with X:
#M needs to be in the square around the X
#Depending on where M is, you need A and S to be in specific spots
#Need to check if in bounds

with open('input', 'r') as file:
    input = file.read().splitlines()

rows = len(input)
cols = len(input[0])


directions = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

counter = 0

for row in range(rows):
    for col in range(cols):
        if input[row][col] == "X":
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                if new_row >= rows or new_row < 0 or new_col >= cols or new_col < 0:
                    continue
                if input[new_row][new_col] == "M":
                    new_row = new_row + d[0]
                    new_col = new_col + d[1]
                    if new_row >= rows or new_row < 0 or new_col >= cols or new_col < 0:
                        continue
                    if input[new_row][new_col] == "A":
                        new_row = new_row + d[0]
                        new_col = new_col + d[1]
                        if new_row >= rows or new_row < 0 or new_col >= cols or new_col < 0:
                            continue
                        if input[new_row][new_col] == "S":
                            counter += 1

print(counter)

