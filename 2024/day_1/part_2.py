#Figure out how often each number from left list appears in right list
#Calculate similarity score
##Add each number in left after multiplying it by the number of times it appears in right

with open('input', 'r') as file:
    input = list(file)

input = [line.strip() for line in input]

left = []
right = []

for i in input:
    left.append(i.split("   ")[0])
    right.append(i.split("   ")[1])

left = sorted(list(map(int, left)))
right = sorted(list(map(int, right)))

total = 0
for i in left:
    if i not in right:
        continue
    elif i in right:
        count = right.count(i)
        to_add = i*count
        total += to_add

print(total)

