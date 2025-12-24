#Problem dampener
#Tolerates a single bad level in what would otherwise be a safe report


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


def is_safe(report):
    if not check_direction(report):
        return False
    for num_1, num_2 in zip(report, report[1:]):
        if not safe_rule(num_1, num_2):
            return False
    return True


safe_count = 0
for report in clean_input:
    if is_safe(report):
        safe_count+=1
    else:
        for idx in range(len(report)):
            modified = report[:idx] + report[idx + 1:]
            if is_safe(modified):
                safe_count+=1
                break

print(safe_count)

