#puzzle input is a diskmap
#digits alternate between length of file and length of free space
#each file also has an id number based on the order of the files as they appear before they are rearranged, starting with ID 0
#move file blocks one at a time from end of the disk to the left most spot
#final step is to check sum


with open('input', 'r') as file:
    test = file.read()

file_expanded = list()
file_id_position = 0

for i, j in enumerate(test):
    if i % 2 == 0:
        file_expanded += int(j) * [file_id_position]
        file_id_position+=1
    elif i % 2 != 0:
        file_expanded += ["."] * int(j)

new_file = list(file_expanded)

left = 0
right = len(new_file) - 1

while left < right:
    while left < right and new_file[left] != ".":
        left += 1
    while left < right and new_file[right] == ".":
        right -= 1
    if left < right:
        new_file[left] = new_file[right]
        new_file[right] = "."
        left += 1
        right -= 1


check_sum = 0

for i, j in enumerate(new_file):
    if j == ".":
        pass
    else:
        to_add = i * int(j)
        check_sum += to_add

print(check_sum)