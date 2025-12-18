def greet():
    print("\nHello")
greet() #Calls the function greet

# 'Amina' is passed to name in the function & printed as ''Hello Dave'
def greet(name):
    print(f"\nHello {name}")
greet("Dave") # Calls the function & passes name 'Dave'

# No value is passed to name in the function, friend is greeted 'Hello friend'
def greet(name="friend"): # Friend is treated as a default value
    print(f"Hello {name}!")
greet()

#Values a b are collected first 
def add(a, b):
    return a + b
result = add(5, 3)
print(result)

#Default arguments (parameters)