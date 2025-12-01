# DAY 4 ASSIGNMENT
# MINI PROJECT: SIMPLE CALCULATOR

print("\nSimple Calculator in Python\n")

# Takes user's input numbers & operator
num1 = float(input("Enter first number: "))
operator = input ("Enter operator(+, -, *, /): ")
num2 = float (input ("Enter second operator: "))

# Performs calculations
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else: result = "\nInfinite"
else: result = "\nInvalid operator!"
print("\nANS:=", result)