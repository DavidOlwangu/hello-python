#Variables, data types and operations

a=10
b=3
sum = a + b
print(sum) # Prints sum of a & b

print(a - b) # Prints 7

print (a%b) # Prints 1 as a remainder, that is, modulus of 10/3

print (a*b) # Multiplies a by b
print (a**b) # 10^3, prints 1000

print (a/b) # Divides & prints 3.33...

"""Divides & rounds off the result into a whole number
    instead of 3.333..., prints 3 """
print (a//b) 

if a>b:
    print ("a is greater than b") # True, prints text in brackets
if b<a:
    print("b is less than a") # True, prints text in brackets
if b>a:
    print("b is greater than a") #False, doesn't print

""" MINI EXERCISE: Simple Calculator;
    Find it in simplecalc.py file
"""