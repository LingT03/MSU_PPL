"""
Lab06 - Lambda Functions
Author: Ling Thang
Date: 08/12/2023
Class: PPL 
"""

"""Returns common elements in two mix-type arrarys using lambda function"""
# Question 1
def intersections(a, b):
    return list(filter(lambda x: x in a, b))    

"""Returns the number of times there is an even and odd number in a given arrary of int with lambda function"""
# Question 2
def num_count(a):
    even = 0
    odd = 0
    for i in a:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

def prompt():
    print("\nWhich program would you like to run?")
    print("1. Intersections")
    print("2. Even-Odd Count")
    print("q. Quit")

if __name__ == "__main__":
    while True:
        prompt()
        choice = (input("\n Enter your choice: "))
    
        if choice == "1":
            # two arrays to test for common elements
            a = ['b', 2, 'a', 4, 5]
            b = [2, 4, 6, 'a', 10]
            
            print ("\n Array 1: ", a)
            print (" Array 2: ", b)
            print("\n The common elements are: ", intersections(a, b))
            print("\n=============================================")

        elif choice == "2":
            # array to test for even-odd count
            a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            
            even, odd = num_count(a)
            print ("\n Array: ", a)
            print("\n Number of even numbers: ", even)
            print(" Number of odd numbers: ", odd)
            print("\n=============================================")

        elif choice == "q":
            break