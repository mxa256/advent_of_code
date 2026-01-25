#Sum of the test values from just the equations that could possibly be true
#Test result is 3749
import math
from itertools import product

with open('input', 'r') as file:
    input = file.read().splitlines()

def add_numbers(num1, num2):
  return num1 + num2


def multiply_numbers(num1, num2):
  return num1 * num2


result = 0

for i in input:
    splits = i.split(": ")
    target = int(splits[0])
    operators = list(map(int, splits[1].split()))
    combination = list(product(['+', '*'], repeat=(len(operators)-1)))
    for j in combination:
        running_result = operators[0]
        for op, num in zip(j, operators[1:]):
            if op == "+":
                running_result = running_result + num
            elif op == "*":
                running_result = running_result * num
        if running_result == target:
            result += target
            break
    else:
        continue

print(result)








