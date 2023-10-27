def my_accumlator():
    # initialize the sum
    sum = 0 
    def add(adder):
        # nonlocal sum
        nonlocal sum
        sum += adder
        return sum
    return add

def gen_h():
    i = 1
    while True:
        num = i
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        if num == 1:
            yield i
        i += 1

def validate_password(func):
    def check(password):
        # check if password begins with 'cs3' ignoring case
        if password[:3].lower() != "cs3":
            raise ValueError("Password must begin with 'cs3'")
        # check if password contains at least one capital letter
        if password.islower():
        # check if password contains at least one number aside from the first three characters
            raise ValueError("Password must contain at least one capital letter")
        if password[3:].isalpha():
            raise ValueError("Password must contain at least one number aside from the first three characters")
        return func(password)
    return check

@validate_password
def accept_new_password(accept_new_pas):
    print(f"Password accepted: {accept_new_pas}")

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

                acc = my_accumlator()
                add1 = int(input("\n Enter a number to add: "))
                print("\n The sum is: ", acc(add1))
                add1 = int(input("\n Enter a number to add: "))
                print("\n The sum is: ", acc(add1))

                acc2 = my_accumlator()
                add2 = int(input("\n Enter a number to add: "))            
                print("\n The sum is: ", acc2(add2))

                acc3 = acc2
                add2 = int(input("\n Enter a number to add: "))
                print("\n The sum is: ", acc3(add2))
            
                # break out 
                print("\n            DEMONSTRATION COMPLETE!")
                break            
                
        elif choice == "2":
            print("\n\t\t  Generator")
            print("=============================================")

            rangeof = int(input("\n Enter a range: "))
            values = gen_h()
            
            generated_num = [next(values) for _ in range(rangeof)]
            print("\n The generated numbers are: ", generated_num)
            print("\n            DEMONSTRATION COMPLETE!")

        elif choice == "3":
            print("\n\t\t  Decorator")
            print("=============================================")
            print ("\n\t\t  Password Checker")

            print("Requirements:")
            print("1. Must begin with 'cs3'")
            print("2. Must contain at least one capital letter")
            print("3. Must contain at least one number aside from the first three characters")

            while True:
                try:
                    password = input("\nEnter a password: ")
                    accept_new_password(password)
                    break
                except ValueError as e:
                    print(e)
                    continue

        elif choice == "q":
            break