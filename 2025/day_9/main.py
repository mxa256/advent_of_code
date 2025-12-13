#Switching out square tiles
#Some tiles are red
#Want to find largest rectangle that uses red tiles for two of its opposite orners


with open('input', 'r') as f:
    input = f.readlines()

input = [line.strip() for line in input]

input = [list(map(int, line.split(','))) for line in input]

#2D grid
#Red tiles are described by coordinates
#Maximum possible area with red tiles as two opposite corners
##Other corners may or may not be red tiles
#Constraints
##if two tiles have same x = area is 0
##if two tiles have same 7 = area is 0

#Among all point pairs, find the pair that maximizes rectangular area based on x and y

max_area = 0

for i in input:
    for j in input:
        x1 = i[0]
        y1 = i[1]
        x2 = j[0]
        y2 = j[1]
        if x1==x2 or y1==y2:
            continue
        else:
            x_dist = abs(x1 - x2) + 1 #Real length between points
            y_dist = abs(y1 - y2) + 1 #Real length between points
            area = x_dist * y_dist
            if area > max_area:
                max_area = area

print(f"The max area of the rectangle is {max_area}")

