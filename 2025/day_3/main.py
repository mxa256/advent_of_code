#Batteries have a joltage rating 1-9
#Batteries are arranged into banks, each line of digits is a bank
#In each bank, you need to turn on two batteries
#Joltage of each bank is equal to the number formed by the digits on the batteries you've turned on
#Need largest possible joltage rating for each bank
#Sum them to get total output

test = [987654321111111, #Largest joltage is 98
811111111111119, #Largest is 89
234234234234278, #Largest is 78
818181911112111] #Largest is 92

#Approach
#This requires a search algorithm
#Turn list of banks into a string
#We want to search for 9, then 8, then 7, etc.
#Return position of first highest number
#Depending on where we find that highest number, we want to do a second search at that position

#Turn it to a string
#test = [str(num) for num in test]

#Our list to search are numbers 0 to 9
numbers = list(range(0, 10))
search_string = [str(num) for num in numbers]
#Reverse the list so we search high to low
search_string = search_string[::-1]

joltage = []
def my_func(inputs):
    for bank in inputs:
        num_found = False
        for num in search_string:
            first_position = bank.find(num)
            if first_position >= 0:
                for num in search_string:
                    substr_bank = bank[(first_position+1):]
                    second_position = substr_bank.find(num)
                    if second_position >= 0:
                        actual_second_position = (first_position+second_position+1)
                        new_joltage = (bank[first_position] + bank[actual_second_position])
                        joltage.append(new_joltage)
                        num_found = True
                        break
            if num_found:
                break
    return joltage


#Open our input file, comma separate, remove newline characters
with open('input.txt', 'r') as f:
    my_input = f.readlines()

my_input = [line.strip() for line in my_input]

result = my_func(my_input)
result = [int(x) for x in result]
final_result = sum(result)
print(final_result)
