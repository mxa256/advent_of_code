#Pages printed in a specific order
#X must be printed before Y
#Find which updates are correctly ordered
#Find the middle page of each correctly ordered update and total

with open('input', 'r') as file:
    input = file.read().splitlines()

#Approach
#Parse X|Y pairs into a list of tuples
#Parse updates into a list
#Check each update's index against rules
#Filter valid updates
#Add middle number from valid updates

pairs = []
for i in input:
    if "|" in i:
        result = tuple(int(x) for x in i.split("|"))
        pairs.append(result)

updates = []
for i in input:
    if "|" not in i and i != "":
        result = [int(x) for x in i.split(',')]
        updates.append(result)

valid_updates = []


for i in updates:
    is_valid = True
    for j in pairs:
        first_num = j[0]
        second_num = j[1]
        if first_num in i and second_num in i:
            if i.index(first_num) > i.index(second_num):
                is_valid = False
                break
        else:
            continue
    if is_valid:
        valid_updates.append(i)

total_mid_num = 0
for i in valid_updates:
    mid_index = (len(i) -1)//2
    result = i[mid_index]
    total_mid_num += result

print(total_mid_num)