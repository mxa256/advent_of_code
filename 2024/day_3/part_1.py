#Computer memory is corrupted
#Need to multiply numbers
#Many invalid characters that need to be ignored

with open('input', 'r') as file:
    input = file.read()

#We need this pattern:
#mul(
#Number
#Comma
#Number
#Parentheses

import re

string="mul\(\d{1,3},\d{1,3}\)"

result = re.findall(string, input)

total = 0

for i in result:
    num_1 = int(re.findall("\d+", i)[0])
    num_2 = int(re.findall("\d+", i)[1])
    product = num_1*num_2
    total += product

print(total)

