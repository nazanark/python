# Task 1: Number info
# Description:
#  Ask the user to enter a number. Your program should:
# Check if the number is positive, negative, or zero
# Check if the number is even or odd
# Print both results

inputNum = int(input("Enter a number: "))

print("Positive even number" if inputNum > 0 and inputNum%2==0 
else "Positive odd number" if inputNum > 0 
else "Negative even number" if inputNum < 0 and inputNum%2==0
else "Negative odd number" if inputNum < 0 
else "The number is ZERO" if inputNum==0 else "" )
