#One report per line
#List of numbers called levels, separated by spaces
#Column = level
#Row = report
#Find safe reports, gradually increasing or gradually decreasing
#Any two adjacent levels differ by 1-3
#How many reports are safe?

with open('input', 'r') as file:
    input = list(file)

input = [line.strip() for line in input]
input = [line.split(" ") for line in input]

clean_input = []
for i in input:
    i = list(map(int, i))
    clean_input.append(i)

def check_direction(list):
    if list[0] > list[1]:
        direction = "descending"
    else:
        direction = "ascending"
    if direction == "descending":
        for i, j in zip(list, list[1:]):
            if i < j:
                return False
        return True
    if direction == "ascending":
        for i, j in zip(list, list[1:]):
            if i > j:
                return False
        return True

def safe_rule(i,j):
    if abs(i - j) >= 1 and abs(i - j) < 4:
        return True
    else:
        return False

safe_count = 0
safe_levels = 0

for i in clean_input:
    safe_levels =0
    if check_direction(i):
        for num_1, num_2 in zip(i, i[1:]):
            if safe_rule(num_1, num_2):
                safe_levels+=1
                if safe_levels == (len(i)-1):
                    safe_count+=1

print(safe_count)

