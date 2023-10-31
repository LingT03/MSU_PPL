expression = "3 * (x + 2) - y/4"

x = 2
y = 6.0

result = eval(expression)
print("Evaluate the expression: ", result)

print("=============================================")

variables = set(x for x in expression if x.isalpha())
constants = set(x for x in expression if x.isdigit() or x == ".")

print("Q2 - variables: ", variables)
print("Q2 - constants: ", constants)

print("=============================================")

x_value = 5
y_value = 8

expression_with_values = expression.replace("x", str(x_value)).replace("y", str(y_value))

result_with_values = eval(expression_with_values)

print("Substitution reslt:", result_with_values)

print("=============================================")

equivalent_expression = "3 * (x + 2) - y / 4.0"

are_equivalent = expression == equivalent_expression
print ("Are equivalent: ", are_equivalent)

print("=============================================")
q7expression = "3 * (x + 2) - y / 0"
try:
    result = eval(q7expression)
except ZeroDivisionError as e:
    print("Cannot divide by zero")
except Exception as e:
    print("Error: ", e)

print("=============================================")

x = True
y = False

result = 3 * (x + 2) - y / 4
print("Q9 - Truth Value Analysis: ", result)

print("=============================================")

x = 0
y = 0

result = 3 * (x + 2) - y / 4
print("Q10 - Truth Value Analysis: ", result)