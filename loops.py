# for loop... while...range..nested loops
# Loops
# For loop
fruits = ["apple","banana","mango"]
for fruit in fruits:
    print("I like", fruit)
# Loop with range()
for i in range(1,6):
    print("count:", i)


list_numbers=[1,2,3,4,5]
sum=0
for number in list_numbers:
    sum+=number #sum=sum+number
print(f"\nThe sum of thre numbers in the list is: {sum}")

#Alternative
list_numbers=[1,2,3,4,5]
sum+=number #sum=sum+number
print(f"\nThe sum of thre numbers in the list is: {sum}")

# While loop
# While the condition is true the value will print
count = 1
while count<= 5:
    print("Number:", count)
    count += 1 # Increase number to avoid infinite loop


# break - stops the loop

for number in range(1, 10):
    if number == 5:
        break #Stops at 5, prints up to 1 to 4
    print(number)

# Continue - skips and proceeds
for number in range(1, 10):
    if number == 3:
        continue # Skips 3 and continues to print upto 10
    print(number)

# Pass - Do nothing
for i in range(5):
    pass #Don't do anything

# Loop with else
for i in range(1, 5):
    print(i)
else:
    print("Loop finished succesfully")

# Looping dictionaries, sets, tuples
# Logical operators (and, or, not)
# Operators and their operations
# Understanding of append.tasks
# List comprehension; examples and their explanation
# Condition expressions (ternary conditional operator)
# More examples on for i in range() and examples with explanation
# 
