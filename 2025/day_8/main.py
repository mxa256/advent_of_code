#Junction boxes
#Which boxes connect so that electricity can reach every junction box
#When two junction boxes are connected by a string of lights, electricity can pass between those two junction boxes
#List of boxes positions in 3D space (input)
#x, y, z coordinates of each junction box
#Connect pairs that are as close together as possible according to Euclidean distance
#Connect the 1000 pairs of junction boxes that are closest together
#Multipley the sizes of the three largest circuits formed by these connections

import math

with open('test', 'r') as f:
    input = f.readlines()


input = [line.strip() for line in input]

input = [list(map(int, line.split(','))) for line in input]

def euclidean_distance(point1, point2):
    squared_differences_sum = 0
    for i in range(len(point1)):
        squared_differences_sum += (point1[i] - point2[i]) ** 2
    return math.sqrt(squared_differences_sum)

#Calculate distances for all points
distances = []

for i in range(len(input)):
    for j in range(i + 1, len(input)):
        dist = euclidean_distance(input[i], input[j])
        distances.append((dist, i, j))

#Sort the distances
distances_sorted = sorted(distances, key=lambda x: x[0])
print(distances_sorted)

#Create the boxes, we'll use a dictionary
#We only need the first 1000 smallest distances
box = {i: i for i in range(len(input))}

#Dict that counts how many boxes belong in each group
counts = {}

for k in range(1000):
    dist, i, j = distances_sorted[k]
    boxi = box[i]
    boxj = box[j]
    if boxi != boxj:
        for k in box:
            if box[k] != boxj:
                box[k] = boxi
            g = box[k]
            if g in counts:
                counts[g] += 1
            else:
                counts[g] = 1


sizes = list(counts.values())
sizes_sorted = sorted(sizes, key=lambda x: x[0])
top_3_sizes = sizes_sorted[0]*sizes_sorted[1]*sizes_sorted[2]
print(top_3_sizes)

