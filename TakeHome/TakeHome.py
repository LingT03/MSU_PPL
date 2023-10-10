# Referenced W3 Schools for help with Python syntax

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# copy of list to be used for function calls because lists are mutuable
Numlist = numbers.copy()

# Function to add 1 to all even numbers in the list
def Adder(num_list):
    # Loop through the list
    for i in range(len(num_list)):
        # Check if the number is even
        if num_list[i] % 2 == 0:
            # Add 1 to the even number
            num_list[i] += 1
        else:
            # Do nothing if the number is odd
            num_list[i] = num_list[i]
    return num_list

# Function to multiply odd numbers by 2 in the list
def Multiplier(num_list):
    # Loop through the list
    for i in range(len(num_list)):
        # Check if the number is odd
        if num_list[i] % 2 != 0:
            # Multiply the odd number by 2
            num_list[i] *= 2
        else:
            # Do nothing if the number is even
            num_list[i] = num_list[i]
    return num_list

# Higher Order Function 
def HigherOrder(num_list, operation_func):
    return operation_func(num_list)

# Display the original list
print("Original List:", numbers, "\n")

# Display the results of all possible function calls
result1 = HigherOrder(numbers, Adder)
print("Add 1 to Even Numbers: ", result1, "\n")

result2 = HigherOrder(Numlist, Multiplier)
print("Multiply Odd Numbers by 2: ", result2, "\n")

result3 = HigherOrder(result1, Multiplier)
print("Add 1 to Even Then Multiply Odd by 2: ", result3, "\n")

result4 = HigherOrder(result2, Adder)
print("Multiply Odd by 2 Then Add 1 to Even: ", result4)