#Need to reorder the incorrect updates
#Add up middle number for the corrected updates only

with open('input', 'r') as file:
    input = file.read().splitlines()

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

non_valid_updates = []

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
    if is_valid == False:
        non_valid_updates.append(i)

corrected_updates = []
for i in non_valid_updates:
    while True:
        found_violation = False
        for j in pairs:
            first_num = j[0]
            second_num = j[1]
            if first_num in i and second_num in i:
                if i.index(first_num) > i.index(second_num):
                    a, b = i.index(first_num), i.index(second_num)
                    i[b], i[a] = i[a], i[b]
                    found_violation = True
        if not found_violation:
            break
    corrected_updates.append(i)

total_mid_num = 0
for i in corrected_updates:
    mid_index = (len(i) -1)//2
    result = i[mid_index]
    total_mid_num += result

print(total_mid_num)



