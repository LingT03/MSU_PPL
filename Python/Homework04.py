def my_accumlator(adder):
    # initialize the sum
    sum = 0
    sum =+ adder
    return sum

def gen_h(input):
#Produce iterator of ints that only have factors in {2, 3, 5}.
    i = int(input)
    while True:
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            yield i
        i += 1

def validate_password(password):
    # check if password begins with 'cs3'
    if password[0:3] != 'cs3':
        return False
    # check if password contains at least one capital letter
    if password.islower():
        return False
    # check if password contains at least one number aside from the first three characters
    if password[3:].isalpha():
        return False
    return True

@validate_password
def accept_new_password(password):
    print("Password accepted")

def prompt():
    print("\nWhich program would you like to run?")
    print("1. Higher Order Functions")
    print("2. Generator")
    print("3. Decorator")
    print("q. Quit")

if __name__ == "__main__":
    while True:
        prompt()
        choice = (input("\n Enter your choice: "))
        if choice == "1":
            while True:
                print("\n            Higher Order Functions")            
                print("=============================================")
                print("\n\t\t  Accumulator")

                adder = int(input("\n Enter a number to add: "))
                print("\n The sum is: ", my_accumlator(adder))

                acc2 = my_accumlator
                adder = int(input("\n Enter a number to add: "))            
                print("\n The sum is: ", acc2(adder))

                acc3 = acc2
                adder = int(input("\n Enter a number to add: "))
                print("\n The sum is: ", acc3(adder))
            
                # break out 
                choice = input("\n Would you like to continue (y/n)? ")
                if choice == "n":
                    break
        elif choice == "2":
            print("\n\t\t  Generator")
            print("=============================================")

            range = int(input("\n Enter a number: "))
            print("\n The iterator is: ", gen_h(range))


        elif choice == "3":
            print("\n\t\t  Decorator")
            print("=============================================")
            print ("\n\t\t  Password Checker")

            print("Requirements:")
            print("1. Must begin with 'cs3'")
            print("2. Must contain at least one capital letter")
            print("3. Must contain at least one number aside from the first three characters")

            password = input("\n Enter a password: ")
            accept_new_password(password)

        elif choice == "q":
            break