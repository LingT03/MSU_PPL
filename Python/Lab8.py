'''
Ling Thang

To my surprise the pseudo code that I wrote for the imperative was almost 
perfect if the aid of Co-pilot I was able to debug the syntax errors. The declarative 
was a bit more difficult to write because in my pseudocode I had assumed that python 
would have a simple way to achieve the result. surprisingly after debugging 
syntax errors my code pseudo were shockingly close! 
'''

# Slice Imperative
def slice_imperative(lst, start, end):
    result = []
    for i in range(start, end):
        if i < len(lst):
            result.append(lst[i])
    return result

# Slice Declarative
def slice_declarative(lst, start, end):
    return lst[start:end]

# Search Imperative
def search_imperative(lst, target):
    for item in lst:
        if item == target:
            return True
    return False

# Search Declarative
def search_declarative(lst, target):
    return target in lst

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


print("Slicing (Imperative):", slice_imperative(my_list, 2, 6))
print("Slicing (Declarative):", slice_declarative(my_list, 2, 6))

print("Search (Imperative):", search_imperative(my_list, 5))
print("Search (Declarative):", search_declarative(my_list, 0))