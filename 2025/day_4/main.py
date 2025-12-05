#@ represents a roll of paper, and . is empty space
#There are 8 positions
#We need fewer than four rolls of paper in the 8 adjacent positions
#We need to identify

#Open our input file, comma separate, remove newline characters
with open('input.txt', 'r') as f:
    my_input = f.read().splitlines()

num_rows = len(my_input)
num_cols = len(my_input[0])

output = []
for i in range(num_rows):
    output.append([])
    for j in range(num_cols):
        output[i].append(None)


num_rolls_for_forklift = 0

for row_index in range(num_rows):
    for col_index in range(num_cols):
            paper_counter = 0
            current_char = my_input[row_index][col_index]
            if current_char != "@":
                output[row_index][col_index] = "."
            else:
                list_coords = [(row_index+1, col_index),
                               (row_index-1, col_index),
                               (row_index, col_index-1),
                               (row_index, col_index+1),
                               (row_index+1, col_index+1),
                               (row_index-1, col_index+1),
                               (row_index-1, col_index-1),
                               (row_index+1, col_index-1)]
                for i in list_coords:
                    if (0 <= i[0] < num_rows) and (0 <= i[1] < num_cols):
                        if my_input[i[0]][i[1]] == "@":
                            paper_counter += 1
                if paper_counter < 4:
                    output[row_index][col_index] = "X"
                    num_rolls_for_forklift += 1
                else:
                    output[row_index][col_index] = "@"

print(output)
print(f"The answer is {num_rolls_for_forklift}")



