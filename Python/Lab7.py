from typing import TypeVar, Generic, List
T = TypeVar('T')  # Declare a type variable 'T'

class Stack(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def push(self, item: T) -> None:
        """Push an item onto the stack."""
        self.items.append(item)

    def pop(self) -> T:
        """Pop an item from the stack and return it."""
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self) -> T:
        """Return the top item on the stack without removing it."""
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self.items)

print('')
stack_of_integers = Stack[int]()
stack_of_strings = Stack[str]()

int_list = input('Enter integers separated by spaces: ').split()
for item in int_list:
    stack_of_integers.push(int(item))
print('\tInt Stack Size:', stack_of_integers.size())

str_list = input('\nEnter strings separated by spaces: ').split()
for item in str_list:
    stack_of_strings.push(item)
print('\tInt Stack Size:', stack_of_strings.size())

print('\nLETS TAKE A PEEK')
print('\tYour Integer Stack:', stack_of_integers.peek())
print('\tYour String Stack:', stack_of_strings.peek())

print('\nLETS POP INT STACK')
while not stack_of_integers.is_empty():
    print('\tPOPPED - ', stack_of_integers.pop())
print('Int Stack Size:', stack_of_integers.size())

print('\nLETS POP STRING STACK')
while not stack_of_strings.is_empty():
    print('\tPOPPED - ', stack_of_strings.pop())
print('String Stack Size:', stack_of_strings.size())

print('\nLETS TRY TO POP EMPTY STACKS')
try:
    print('Your Integer Stack:', stack_of_integers.pop())
except IndexError as e:
    print('\tError:', e)

print('\nLETS TRY TO PEEK EMPTY STACKS')
try:
    print('Your String Stack:', stack_of_strings.peek())
except IndexError as e:
    print('\tError:', e)