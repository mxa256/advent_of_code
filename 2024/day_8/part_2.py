
#Antennas at a specific frequency - lower or upper case letter, or digit
#Signal only applies at antinodes based on frequencies of antenna
#In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same frequency -
#but only when one of the antennas is twice as far away as the other.
#antinodes can occur at locations that contain antennas

import itertools
from collections import defaultdict

with open('input', 'r') as file:
    input = file.read().splitlines()


rows = len(input)
cols = len(input[0])

antinode_locations = set()

antennas = defaultdict(list)

for row in range(rows):
    for col in range(cols):
        if input[row][col] != ".":
            antennas[input[row][col]].append((row, col))

for key, value in antennas.items():
    poss_combo = itertools.combinations(value, 2)
    for i, j in poss_combo:
        antinode_locations.add(i)
        antinode_locations.add(j)
        row_diff, col_diff = tuple(x - y for x, y in zip(i, j))
        anti_node_1 = (i[0] + row_diff, i[1] + col_diff)
        anti_node_2 = (j[0] - row_diff, j[1] - col_diff)
        while anti_node_1[0] < rows and anti_node_1[0] >= 0 and anti_node_1[1] < cols and anti_node_1[1] >= 0:
            antinode_locations.add(anti_node_1)
            anti_node_1 = (anti_node_1[0] + row_diff, anti_node_1[1] + col_diff)
        while anti_node_2[0] < rows and anti_node_2[0] >= 0 and anti_node_2[1] < cols and anti_node_2[1] >= 0:
            antinode_locations.add(anti_node_2)
            anti_node_2 = (anti_node_2[0] - row_diff, anti_node_2[1] - col_diff)


print(len(antinode_locations))






