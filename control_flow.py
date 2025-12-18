# Conditional Statements (IF logic) in python

# if statement

age = 20
if age >= 18:
    print("\nRegister for ID")

# if-else statement
age = 20 # Default age value
if age >= 18:
    print("\nAllowed to vote") # Prints allowed to vote
else:
    print("\nNot allowed to vote")

# if...else statement
# Ex.2: User enters the age value

age = int(input("\nEnter your age: ")) # Asks user to enter age
if age >= 18 and age <= 120: # Checks if entered age is within parameters
    result = "Eligible to vote"
    message = " Queue to vote"
else:
    result = "Out of equation" #Age below 18 and above 120 won't participate
    message = "Sorry!"
print(result)
print(message)

# if...elif...else statement
age = int(input("\nEnter your age: ")) # Asks user to enter age
if age >= 18 and age <= 120: # Checks if entered age is within parameters
    result = "\nEligible to vote"
    message = " Queue to vote"
elif age >= 1 and age < 18:
    result = "\nYou are a minor"
    message = "Not allowed to vote"
elif age > 120:
    result = "\nToo old"
    message = "Not allowed to participate"
else:
    result = "\nInvalid!"
    message = "Enter a valid whole number(18 - 120)"
print(result)
print(message)


# Nested if
# Both conditions are checked if true or false
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("You can enter")
    else:
        print("You need an ID")
else:
    print("You are under age")
