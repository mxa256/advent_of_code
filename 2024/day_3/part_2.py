
with open('input', 'r') as file:
    input = file.read()

#Additional instructions
#Do enables future mul instructions
#Dont disables future mul instructions

#Only most recent instruction applies

#Enabled at the start


import re

string = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

result = re.findall(string, input)

enabled = True

total = 0

for i in result:
    if i=="do()":
        enabled=True
    elif i=="don't()":
        enabled=False
    else:
        if enabled==True:
            num_1 = int(re.findall("\d+", i)[0])
            num_2 = int(re.findall("\d+", i)[1])
            product = num_1 * num_2
            total += product

print(total)