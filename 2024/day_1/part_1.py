#List of locations
#Identified by location ID
#Two groups creating a list of location IDs
#Need to reconcile lists
#Pair up smallest number in left list with smallest number in right list, and so on
#Find how far apart the two numbers are, add up all the distances

with open('input_part_1', 'r') as file:
    input = list(file)

input = [line.strip() for line in input]

list_1 = []
list_2 = []

for i in input:
    list_1.append(i.split("   ")[0])
    list_2.append(i.split("   ")[1])

list_1 = sorted(list(map(int, list_1)))
list_2 = sorted(list(map(int, list_2)))

final_list = [abs(i - j) for i, j in zip(list_1, list_2)]

total = sum(final_list)

print(total)
