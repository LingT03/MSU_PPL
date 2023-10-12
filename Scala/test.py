def MATHIT(number, operation):
    return operation(number)


def double(num):
    return num * 2

def square(num):
    return num * num

numberToCube = 3
resultDouble = MATHIT(numberToCube, double)
resultSquare = MATHIT(numberToCube, square)
print(f"The double of {numberToCube} is {resultDouble}")
print(f"The square of {numberToCube} is {resultSquare}")