# Control flow and loops in python
# if-else statements
#if condition
    #Code block
#elif condition2:
    #code block
#else:
    #code block
#loops
#for loop
list_numbers=[1,2,3,4,5]
sum=0
for number in list_numbers:
    sum+=number #sum=sum+number
print("The sum of thre numbers in the list is: {sum}")

#Aalternative
list_numbers=[1,2,3,4,5]

    sum+=number #sum=sum+number
print("The sum of thre numbers in the list is: {sum}")

#while loop special statements - break, continue, pass

day=int(input("Enter day number(1-7): "))
if day==1:
    print("Monday")