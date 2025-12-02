#We have product ID ranges
#These are integer ranges (first-last, first-last, etc.)
#Invalid IDs are any ID where a sequence of digits is repeated twice


#Approach
#Expand the range into a list of ints
#Turn the numbers into strings
#Match string patterns with regex
#Identify invalid IDs in each group
#Exclude them, put them in a list
#Turn final list of bad codes back to integers
#Sum them for the final answer

import re

with open('input.txt', 'r') as file:
    test = list(file)

test = [line.strip() for line in test]

cleaned = []

#We have to clean our data
for group in test:
    parts = group.split(",")
    parts = [p.strip() for p in parts if p.strip()]
    cleaned.extend(parts)

def create_range(r):
    start, end = map(int, r.split("-"))
    return list(range(start, end+1))

list_of_lists = []
for i in cleaned:
    result = create_range(i)
    list_of_lists.append(result)

def find_invalid_codes(n):
    s = str(n)
    pattern = re.compile(r'^(\d+)\1$')
    m = re.findall(pattern, s)
    if m:
        return s
    else:
        return None

bad_codes = []
for list in list_of_lists:
    for i in list:
        i = str(i)
        bad_codes.append(find_invalid_codes(i))

final_list = [item for item in bad_codes if item is not None]

final_sum = 0
for i in final_list:
    i = int(i)
    final_sum += i

print(final_sum)