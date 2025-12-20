#Reactor needs to communicate with server rack
#List of devices and outputs
#Each line gives the name of the device, list of outputs to which outputs are attached
#PATH
#Data flows forward, not backward
#Start with devices starting with YOU
#End with devices ending with OUT
#Find every path from YOU to OUT
#Graph algorithm
#Recursion

#Read in the file as a dictionary

dict = {}
with open('input', 'r') as f:
    for line in f:
        key, value = line.strip().split(': ', 1)
        dict[key] = value

dict = {k: v.split() for k, v in dict.items()}

#Function
def my_func(i):
    path_count = 0
    #Base case
    for value in dict[i]:
        if value == "out":
            path_count += 1
        #Recursive case
        else:
            path_count += my_func(value)
    return path_count


answer = my_func("you")
print(answer)