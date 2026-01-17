
#The ^ is current guard position
#The # is an obstruction
#If something in front, turn 90 degrees
#Otherwise, take a step forward
#Find all distinct positions of the guard

#Test answer is 41

with open('input.txt', 'r') as file:
    input = file.read().splitlines()

rows = len(input)
cols = len(input[0])


visited = set()

#Get starting point
for row in range(rows):
    for col in range(cols):
        if input[row][col] == "^":
            current_position = (row, col)
            visited.add(current_position)
            direction = (-1, 0) #Moving up
            while True:
                next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
                if next_position[0] >= rows or next_position[0] < 0 or next_position[1] >= cols or next_position[1] < 0:
                    break
                if input[next_position[0]][next_position[1]] == "#":
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
                    visited.add(next_position)

print(len(visited))
