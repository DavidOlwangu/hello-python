# Student Grade Evaluator
# This program asks fro marks, checks the range & assign a grade

# Ask user to enter their marks
marks = float(input("\nEnter your marks(1-100): "))

if marks >= 80 and marks <= 100:
    grade = "A"
    message = "Excellent"
elif marks >= 65:
    grade = "B"
    message = "Great work"
elif marks >= 50:
    grade = "C"
    message = "Can do better"
elif marks >= 30:
    grade = "D"
    message = "Put in more effort"
elif marks >= 0:
    grade = "E"
    message = "Failed!"
else:
    grade = "invalid"
    message = "Marks should be between 0 and 100."

print(grade)
print (message)
