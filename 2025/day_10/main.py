#Data structure: one machine per line
#Each line has a single indidcator light diagram (square brackets)
#One or more button wiring schematics (parentheses)
#Joltage requirements (curly braces)

#All switches start OFF
#We have a target pattern to match (indicator lights)
# . means off and # means on
#We have button wiring schematics in parentheses, which can control multiple buttons
#We have joltage requirements in curly brackets which can be ignored
#Determine FEWEST total presses required to correctly get to the pattern

#Read it and remove joltages (probably for Part 2)
with open('input', 'r') as f:
    input = f.readlines()

#Remove joltage
input = [line.split('{')[0] for line in input]
#Remove trailing whitespace
input = [line.strip() for line in input]

#It only ever makes sense to push a button once
#Button will be pushed 0 times or 1 time
#Order buttons pushed doesn't matter
#Count how many times a button is pushed at a position

import ast
import itertools

total = 0
for i in input:
    i = i.split(" ")
    target = i[0][1:-1]
    buttons = i[1:]
    buttons = [list(ast.literal_eval(s if ',' in s else s.replace(')', ',)')))
               for s in buttons]
    target_on = []
    for index, element in enumerate(target):
        if element=="#":
            index = index
            target_on.append(index)
    found = False
    for s in range(len(buttons)+1):
        if found:
            break
        for combo in itertools.combinations(buttons, s):
            toggles_per_position = [0] * len(target)
            for button in combo:
                for position in button:
                    toggles_per_position[position] += 1
            result_on = []
            for position, count in enumerate(toggles_per_position):
                if count % 2 == 1:
                    result_on.append(position)
            if result_on == target_on:
                total += s
                found = True
                print(total)
                break

