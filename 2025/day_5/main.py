#Approach
#Separate file into two: ranges and actual ingredients
#Match ints in both lists
#Count matches

#Open file
with open('input.txt', 'r') as f:
    input = f.readlines()

input = [line.strip() for line in input]

#Create a list of fresh ingredient ranges and ingredients
ing_range, ing = [], []
split_point = False

for item in input:
    if item == '':
        split_point = True
        continue
    if not split_point:
        ing_range.append(item)
    else:
        ing.append(item)

#Store the ranges
fresh_ing_range = []
for i in ing_range:
    start, end = map(int, i.split("-"))
    fresh_ing_range.append((start, end))

def in_any_range(n, ranges):
    for start, end in ranges:
        if start <= n <= end:
            return True
    return False

#Turn the ingredient list into integers
ing_list = [int(x) for x in ing]

count = sum(in_any_range(n, fresh_ing_range) for n in ing_list)

print(f"The number of fresh ingredients is {count}")